# Code Review & Debug Squad

## Multi-Agent AI Code Review and Debugging Assistant

### 1. Introduction
Code Review & Debug Squad is an AI-powered application that analyses Python code using multiple specialised AI agents. It identifies programming errors, reviews coding style, suggests corrections and generates test cases.

### 2. Problem Statement
Manual code review takes time and developers may miss logical errors, runtime risks and coding-standard violations. This project uses multiple AI agents to automate and simplify the code-review process.

### 3. Objectives
- Detect programming errors.
- Review Python coding standards.
- Suggest corrected code.
- Generate test cases.
- Provide an interactive AI-based code-review interface.

### 4. AI Agents

**1. Bug-Finder Agent**
- Identifies logical errors and possible runtime risks.
- Detects edge cases.

**2. Style/Lint Agent**
- Checks code readability.
- Reviews naming conventions and coding practices.

**3. Fixer Agent**
- Suggests corrected Python code.
- Explains recommended changes.

**4. Test-Writer Agent**
- Generates test cases.
- Suggests normal and edge-case testing.

### 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend |
| Streamlit | User interface |
| Groq LLM | AI model integration |
| LangChain | Prompt templates and LCEL |
| ChromaDB | Vector database |
| Python-dotenv | Environment configuration |

### 6. System Workflow
1. User enters Python code.
2. The application receives the selected task.
3. Intent routing selects the relevant AI agent.
4. The agent retrieves relevant coding guidelines from ChromaDB.
5. The LLM analyses the submitted code.
6. The application displays the review and suggestions.

### 7. Agentic AI Concepts
- Large Language Model integration
- Prompt Engineering
- Intent Detection and Routing
- Retrieval-Augmented Generation (RAG)
- Vector Database
- LangChain Expression Language (LCEL)
- Multi-Agent Architecture

### 8. Installation

```bash
git clone https://github.com/akashbabli01/Code-Review-Debug-Squad.git
cd Code-Review-Debug-Squad
python -m venv venv
```

Activate on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Groq API key in a private `.env` file.

### 9. Run the Application

```bash
streamlit run app.py
```

### 10. Future Enhancements
- Automated code execution in an isolated sandbox.
- Advanced bug detection.
- More programming-language support.
- Detailed code-quality reports.
- Improved multi-agent collaboration.

### 11. Author
Akash Babli

**Project:** Agentic AI – Assignment 1  
**Title:** Code Review & Debug Squad            
