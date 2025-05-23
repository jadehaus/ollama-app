import time
import uuid
import requests

import ollama
import streamlit as st

DEFAULT_OLLAMA_URL = "http://localhost:11434"


def check_ollama():
    with st.spinner(f"Checking Ollama at {DEFAULT_OLLAMA_URL}..."):
        try:
            time.sleep(1)
            resp = requests.get(f"{DEFAULT_OLLAMA_URL}/api/tags", timeout=5)
            resp.raise_for_status()
            ollama_url = DEFAULT_OLLAMA_URL
        except Exception:
            st.sidebar.error(f"Cannot connect to Ollama at {DEFAULT_OLLAMA_URL}. Please start Ollama.")
            if st.sidebar.button("Retry Connection"):
                st.rerun()
            st.stop()