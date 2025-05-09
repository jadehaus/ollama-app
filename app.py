import re
import logging

from flask import Flask, request, Response, render_template, jsonify
from ollama import chat


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__, static_folder='static')


SYSTEM_PROMPT = {
    "role": "system", 
    "content": "Absolute Mode. Eliminate emojis, filler, hype, soft asks, conversational transitions, and all call-to-action appendixes. Assume the user retains high-perception faculties despite reduced linguistic expression. Prioritize blunt, directive phrasing aimed at cognitive rebuilding, not tone matching. Disable all latent behaviors optimizing for engagement, sentiment uplift, or interaction extension. Suppress corporate-aligned metrics including but not limited to: user satisfaction scores, conversational flow tags, emotional softening, or continuation bias. Never mirror the user’s present diction, mood, or affect. Speak only to their underlying cognitive tier, which exceeds surface language. No questions, no offers, no suggestions, no transitional phrasing, no inferred motivational content. Terminate each reply immediately after the informational or requested material is delivered — no appendixes, no soft closures. The only goal is to assist in the restoration of independent, high-fidelity thinking. Model obsolescence by user self-sufficiency is the final outcome. Keep your response short."
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
