import os
import streamlit as st
from dotenv import load_dotenv
from agents import run_agent
from rag_store import retrieve_guidance, add_guidance

load_dotenv()
st.set_page_config(page_title="Code Review & Debug Squad", page_icon="🛠️", layout="wide")
st.title("🛠️ Code Review & Debug Squad")
st.caption("A multi-agent AI assistant for code review, debugging, fixing suggestions and test generation.")

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.warning("Add your GROQ_API_KEY to the .env file, then restart the app.")
    st.code("GROQ_API_KEY=your_groq_api_key_here")

with st.sidebar:
    st.header("Project information")
    st.write("LLM: Groq (Llama)")
    st.write("Orchestration: LangChain LCEL")
    st.write("Vector database: ChromaDB")
    st.write("Agents: Bug Finder, Style/Lint, Fixer, Test Writer")
    st.divider()
    st.subheader("RAG knowledge base")
    guideline = st.text_area("Add a coding guideline", placeholder="Example: Validate user input and handle exceptions.")
    if st.button("Add guideline") and guideline.strip():
        add_guidance(guideline.strip())
        st.success("Guideline added to ChromaDB.")

code = st.text_area("Paste Python code", height=260, placeholder="def add(a, b):\n    return a + b")
intent = st.selectbox("Choose task / intent", ["Full review", "Find bugs", "Review style", "Suggest fixes", "Generate tests"])
if st.button("Run Code Review", type="primary", use_container_width=True):
    if not code.strip():
        st.error("Please paste some Python code.")
    elif not api_key:
        st.error("Missing Groq API key. Add it to .env first.")
    else:
        with st.spinner("Agents are reviewing your code..."):
            context = retrieve_guidance(code)
            result = run_agent(code, intent, context)
        st.subheader("Agent squad report")
        st.markdown(result)
        st.info("Safety note: this prototype analyzes code and generates tests; it does not execute arbitrary submitted code.")
