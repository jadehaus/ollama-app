import streamlit as st
from pathlib import Path


@st.cache_data
def load_readme() -> str:
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        return readme_path.read_text(encoding="utf-8")
    return "## README.md not found"


def main():
    st.set_page_config(page_title='충북교육연구정보원 정보영재교육원 AI')
    st.title("2025 사사B반 프로젝트 AI")

    readme_md = load_readme()
    st.markdown(readme_md, unsafe_allow_html=True)


if __name__ == "__main__":
    
    pg = st.navigation([
        st.Page(main, title="Home", icon="🏠"),
        st.Page("pages/debate.py", title="Debate", icon="🔥"),
        st.Page("pages/rag_chat.py", title="QnA with PDF", icon="📚"),
        st.Page("pages/simple_chat.py", title="Quick Start", icon="💬"),
    ])

    pg.run()
