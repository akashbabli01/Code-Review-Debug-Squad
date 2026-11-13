# Code Review & Debug Squad

A prototype multi-agent Python code-review assistant built with Streamlit, Groq, LangChain LCEL and ChromaDB.

## Agents
1. Bug-Finder Agent – identifies possible bugs, edge cases and runtime risks.
2. Style/Lint Agent – reviews readability and Python conventions.
3. Fixer Agent – suggests corrected code and explains changes.
4. Test-Writer Agent – generates pytest test cases (generation only; tests are not executed in this prototype).

## Architecture
Streamlit UI → intent selection → agent prompt → LangChain LCEL chain → Groq LLM.
The app retrieves relevant coding guidelines from ChromaDB and includes them in the agent prompt (RAG).

## Setup (Windows PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
```
Edit `.env` and add your Groq API key. Never commit `.env`.

## Run
```powershell
streamlit run app.py
```

## Demonstrated assignment concepts
- LLM integration: Groq ChatGroq.
- GUI: Streamlit.
- Prompt engineering: role-specific system prompts and task-specific user context.
- LangChain core: ChatPromptTemplate and LCEL (`prompt | model | StrOutputParser`).
- RAG: retrieve coding guidelines from ChromaDB and add them to the prompt.
- Intent routing: user-selected task routes to the relevant agent(s).
- Vector database: ChromaDB persistent collection.

## Limitations
This is a time-boxed educational prototype. It generates code review and test suggestions but does not execute arbitrary user code. Do not treat its output as a security audit. A production implementation should add isolated sandbox execution, automated test execution, authentication, robust error handling, evaluation and logging.
