import ollama
import streamlit as st

from utils import check_ollama

st.title("QnA with PDF")

# 모델 초기화
if "model" not in st.session_state:
    check_ollama()
    st.session_state.model = ""

# 설정 표시
with st.sidebar:
    st.sidebar.title("Settings")
    # 모델 목록 가져오기
    models = [model['model'] for model in ollama.list()["models"]]
    st.session_state.model = st.sidebar.selectbox(
        "Choose your model", 
        models,
        help="모델을 선택하세요.",
    )

    # 시스템 프롬프트
    system_prompt = st.sidebar.text_area(
        "System Prompt",
        value="You are a helpful assistant.",
        help="시스템 프롬프트는 모델의 행동을 조절합니다."
    )