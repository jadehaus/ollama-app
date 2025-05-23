### 사용 가이드

먼저 `ollama`를 실행합니다. Ollama 설치 및 실행 방법은 [Ollama 공식 사이트](https://ollama.com/)에서 확인해주세요.   
Ollama 설치가 끝났다면, 아래와 같이 `ollama` 서버를 실행해주세요.

```bash
ollama serve
```

Ollama는 기본 설정상 `http://localhost:11434`에서 호스트됩니다.  

Ollama 실행이 끝났다면, 터미널에서 다음 명령을 실행하여 웹서비스를 실행합니다.

```bash
streamlit run app.py
```


### 구현 기능 목록 및 필요 기술 스택

| 기능 | 설명 | 구현 여부 (현재 버전) | 구현 파일 | 참고 문헌, 필요 기술 스택 및 링크 |
|---|---|---|---|---|
| 단일 응답 생성 | 주어진 질문에 대한 단일 답변을 생성하는 언어모델을 불러옵니다. | ✔ | `pages/simple_chat.py` | - |
| Multi-turn 응답 생성 | 채팅 형식으로 대화를 계속 이어나갑니다. | ✔ | `pages/simple_chat.py`| - |
| 시스템 프롬프트 변경 | 언어모델의 시스템 프롬프트를 변경하여, 모델의 행동 양식을 조절하고 변경합니다. | ✔ | `pages/simple_chat.py` | - |
| 멀티 에이전트 토론 | 여러 언어모델을 불러와서, 서로 토론을 하도록 합니다. | ✘ | `pages/debate.py` | [예제1](https://wikidocs.net/234162) |
| 검색증강생성 (RAG) | 주어진 문서 혹은 인터넷 검색을 활용해, 언어모델이 불러온 정보를 참고하여 답변을 생성합니다. | ✘ | `pages/rag_chat.py` | [예제1](https://velog.io/@cathx618/Ollama-Python%EC%97%90%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0), [예제2](https://velog.io/@cathx618/Ollama%EC%99%80-LangChain%EC%9C%BC%EB%A1%9C-RAG-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-with-Python), [예제3](https://velog.io/@judy_choi/LLaMA3-%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-RAG-%EA%B5%AC%EC%B6%95-Ollama-%EC%82%AC%EC%9A%A9%EB%B2%95-%EC%A0%95%EB%A6%AC), [예제4](https://medium.com/@vndee.huynh/build-your-own-rag-and-run-it-locally-langchain-ollama-streamlit-181d42805895) |
| 모델 자동 다운로드 및 실행 | Ollama에서 기본으로 제공하는 모델을 웹앱에서 선택하면 자동으로 다운로드 받은 후 실행하도록 합니다. | ✘ | - | [예제1](https://github.com/TsLu1s/talknexus/tree/main) |
| Ollama Huggingface 모델 연동 | Ollama에서 기본으로 제공하는 모델 외에도, Huggingface를 통해 불러온 모델을 Ollama에 연동하여 작동합니다. | ✘ | - | - |
| 온라인 API 호스팅 | 로컬 환경 (e.g. 본인의 컴퓨터) 실행 코드를 온라인 주소를 통해 접근할 수 있도록 호스팅합니다. | ✘ | - | [예제1](https://lsjsj92.tistory.com/685), [예제2](https://memoryhub.tistory.com/entry/%EB%A1%9C%EC%BB%AC-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C-API-%ED%98%B8%EC%8A%A4%ED%8C%85%EC%9D%84-%EC%9C%84%ED%95%9C-Ollama-%EC%84%A4%EC%A0%95-%EC%A2%85%ED%95%A9-%EA%B0%80%EC%9D%B4%EB%93%9C), [Ngrok](https://ngrok.com/) |