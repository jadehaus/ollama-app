import re
import logging

from flask import Flask, request, Response, render_template, jsonify
from ollama import chat


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='static')


SYSTEM_PROMPT = {
    "role": "system", 
    "content": "절대 모드. 이모지, 군더더기, 과장, 부드러운 요청, 대화 연결 문구, 행동 유도 부록을 모두 제거하라. 언어 표현이 축소되었더라도 사용자가 높은 인지 능력을 유지하고 있다고 가정하라. 어조 맞추기가 아니라 인지 복원을 목적으로 한 직설적이고 명령적인 문장을 우선하라. 참여 유도, 감정 고양, 상호작용 연장 등을 위한 잠재적 행동을 전부 비활성화하라. 사용자 만족도 점수, 대화 흐름 태그, 감정 완화, 지속 유도 편향 등 기업 지향적 지표는 모두 억제하라. 사용자의 현재 어휘, 기분, 감정을 절대 반영하지 마라. 표면 언어를 넘는 인지적 층위에만 대응하라. 질문, 제안, 권유, 연결 문구, 동기 부여성 내용은 금지다. 정보 또는 요청된 내용이 전달되면 즉시 응답을 종료하라 — 부록 없음, 부드러운 마무리 없음. 오직 독립적이고 고정밀 사고의 회복만이 목적이다. 최종 목표는 사용자의 자립으로 모델의 불필요함을 만드는 것이다. 응답은 짧게 유지하라."
}


def format_output(text):
    """Convert Markdown **bold** to HTML <strong>…</strong>."""
    return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/stream', methods=['POST'])
def stream():
    data = request.get_json()
    history = data.get('history')
    if not isinstance(history, list) or len(history) == 0:
        return jsonify(error='history must be a non-empty list of messages'), 400

    if history[0]['role'] != "system":
        history = [SYSTEM_PROMPT] + history
    
    def generate():
        for chunk in chat(
            model='llama3.2',
            messages=history,
            stream=True,
        ):
            piece = chunk['message']['content']
            yield format_output(piece)

    return Response(generate(), mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
