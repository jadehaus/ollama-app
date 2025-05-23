#모듈 가져오기
import streamlit as st
from ollama import chat

# 페이지 제목과 아이콘 설정
st.set_page_config(
    page_title='NebulaX',
    # page_icon='./img/xlogo.png'
)


# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "intro"

def set_page(page_name):
    st.session_state.page = page_name

# 대화 저장 공간생성
if 'chated' not in st.session_state:
    st.session_state.chated = []
if 'conversation' not in st.session_state:
    st.session_state.conversation = {}
if 'freetalk' not in st.session_state:
    st.session_state.freetalked = []
if 'freetalk_history' not in st.session_state:
    st.session_state.freetalk_history = {}
if 'id' not in st.session_state:
    st.session_state.id = 1
if 'is_generating' not in st.session_state:
    st.session_state.is_generating = False

# 사이드바
# st.sidebar.image('./img/nxlogo.png')
st.sidebar.markdown("## 🚀 빠른 시작")
if st.sidebar.button("🏠 NebulaX 홈", key="intro", use_container_width=True):
    set_page("intro")

if st.sidebar.button("📝새 채팅 시작하기", key="new", use_container_width=True):
    set_page("new")

if st.sidebar.button("🔥새 AI토론(Experiment)", key="freetalk", use_container_width=True):
    set_page("freetalk")

st.sidebar.markdown("## 🗂️내 대화 목록")
for title in st.session_state.chated:
    if st.sidebar.button(title, key=title, use_container_width=True):
        set_page(title)

st.sidebar.markdown("## 🗂️내 토론 목록")
for talker in st.session_state.freetalked:
    if st.sidebar.button(talker, key=talker, use_container_width=True):
        set_page(talker)
################################################################ 홈 화면
if st.session_state.page == "intro":
    st.snow()
    st.title("🏠 환영합니다")
    
    st.write("#### NebulaX AI와 대화해보세요! 🤗")
    st.write("#### NebulaX AI는 당신의 질문에 답변해줄 수 있습니다.")

    # 설명 문단 추가
    st.markdown("---")
    st.write("💡 **AI 어시스턴트란?**")
    st.write("""
    AI 어시스턴트는 여러분의 다양한 질문에 똑똑하게 답변해주는 인공지능이에요! 🧠  
    공부하다가 궁금한 점이 생겼을 때, 일상 속에서 정보가 필요할 때,  
    언제든지 편하게 질문해보세요! ✨  

    - ❓ 궁금한 개념을 설명해줄 수 있어요  
    - 📚 학습 도우미로 활용할 수 있어요  
    - 💬 자연스러운 대화가 가능해요  

    지금 바로 NebulaX AI와 대화를 시작해보세요! 😊
    """)
    
    st.video('https://www.youtube.com/watch?v=Sxlz-r5FeCo')

################################################################ 새로운 대화 생성
if st.session_state.page == "new":
    # 새로운 대화 생성
    name = '📌NebulaX AI와 대화 ' + str(st.session_state.id)
    st.session_state.chated.append(name)
    st.session_state.conversation[name] = []
    st.session_state.id += 1
    set_page(name)
################################################################ AI토론
if st.session_state.page == "freetalk":
    st.title("🔥새 AI토론")
    st.write("### ✨AI토론을 시작해보세요!")
    txt_main = st.text_area("AI토론 주제를 입력하세요", "예) AI는 인류에게 도움이 될까?")
    if txt_main:
        st.session_state.freetalk_main = txt_main
        if st.button("🗝️토론 시작하기"):
            if txt_main not in st.session_state.freetalked:
                st.session_state.freetalked.append(txt_main)
                st.session_state.freetalk_history[txt_main] = []
                set_page(txt_main)
            else:  
                st.warning("이미 존재하는 토론입니다.")            


################################################################ 인공지능과 대화
for title in st.session_state.chated:
    if st.session_state.page == title:
        st.balloons()
        st.markdown("---")
        # 전체 대화 기록 출력
        if st.session_state.conversation[title]:
            for message in st.session_state.conversation[title]:
                if message['role'] == 'user':
                    st.write(f"### 😎 User")
                    st.write(message['content'])
                    st.markdown("---")
                elif message['role'] == 'assistant':
                    st.write(f"### ✨NebulaX")
                    st.write(message['content'])
                    st.badge("NebulaX")
                    st.markdown("---")


        #메인 페이지
        prompt = st.chat_input("Say something") #질문 입력창

        if prompt:
            st.balloons()
            # 대화 기록에 사용자 입력 추가
            st.session_state.conversation[title].append({'role': 'user', 'content': prompt})
            
            # 사용자 입력추가
            st.write(f"### 😎 User")
            st.write(prompt)
            st.markdown("---")
            
            # 인공지능 응답 추가
            st.write(f"### ✨NebulaX")
            stream = chat(
                model="DeepSeek-R1",
                messages= st.session_state.conversation[title],
                stream=True
            )
            placeholder = st.empty()
            response_text = ""

            for chunk in stream:
                response_text += chunk.message.content
                placeholder.markdown(f"<span style='font-size:18px'>{response_text}</span>", unsafe_allow_html=True)
            st.badge("NebulaX")
            sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
            selected = st.feedback("thumbs")
            # AI의 응답을 대화 기록에 추가
            st.session_state.conversation[title].append({'role': 'assistant', 'content': response_text})

################################################################ 인공지능과 토론
for title in st.session_state.freetalked:
    if st.session_state.page == title:
        st.balloons()
        st.markdown("---")
        # 전체 대화 기록 출력
        if st.session_state.freetalk_history[title]:
            for message in st.session_state.freetalk_history[title]:
                if message['role'] == 't1':
                    st.write(f"### ✅ 찬성하는 입장")
                    st.write(message['content'])
                    st.markdown("---")
                elif message['role'] == 't2':
                    st.write(f"### ❌ 반대하는 입장")
                    st.write(message['content'])
                    st.markdown("---")
        
        
        #메인 페이지
        st.session_state.freetalk_history[title].append({'role': 'user', 'content': f"{title}에 대하 찬성하는 이유만을 전에 나오지 않은 것을 기반으로 설명하시오"})
        st.write(f"### ✅ 찬성하는 입장")
        stream = chat(
            model="DeepSeek-R1",
            messages= st.session_state.freetalk_history[title],
            stream=True
        )
        placeholder = st.empty()
        response_text = ""

        for chunk in stream:
            response_text += chunk.message.content
            placeholder.markdown(f"<span style='font-size:18px'>{response_text}</span>", unsafe_allow_html=True)
        st.markdown("---")
        # AI의 응답을 대화 기록에 추가
        st.session_state.freetalk_history[title].append({'role': 't1', 'content': response_text})
        
        
        st.session_state.freetalk_history[title].append({'role': 'user', 'content': f"{title}에 대해 반대하는 이유만 전에 나오지 않은 것을 기반으로 설명하시오"})
        st.write(f"### ❌ 반대하는 입장")
        stream = chat(
            model="DeepSeek-R1",
            messages= st.session_state.freetalk_history[title],
            stream=True
        )
        placeholder = st.empty()
        response_text = ""

        for chunk in stream:
            response_text += chunk.message.content
            placeholder.markdown(f"<span style='font-size:18px'>{response_text}</span>", unsafe_allow_html=True)
        st.markdown("---")
        # AI의 응답을 대화 기록에 추가
        st.session_state.freetalk_history[title].append({'role': 't2', 'content': response_text})
            