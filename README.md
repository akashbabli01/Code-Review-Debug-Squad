# 🤖 Code Review & Debug Squad

### AI-Powered Multi-Agent Python Code Review Assistant

Code Review & Debug Squad is an AI-powered Python code-review assistant that helps developers identify potential bugs, improve code quality, suggest code corrections, and generate automated test cases.

The application uses **Streamlit, Groq, LangChain LCEL, and ChromaDB** to provide an interactive code-review experience using four specialized AI agents.

---

## 🎯 Project Objectives

- Identify potential bugs and runtime errors in Python code.
- Improve code readability and maintainability.
- Suggest corrected versions of Python code.
- Generate pytest test cases for different input conditions.
- Retrieve relevant coding guidelines using Retrieval-Augmented Generation (RAG).
- Provide an easy-to-use interface for reviewing Python programs.

---

## 🧠 AI Agents

The project consists of four specialized AI agents:

### 1. Bug-Finder Agent
- Identifies possible syntax and logical errors.
- Detects runtime risks and edge cases.
- Explains potential problems in the submitted code.

### 2. Style/Lint Agent
- Reviews Python coding conventions.
- Checks variable naming and formatting.
- Suggests improvements in readability and maintainability.
- Considers Python PEP 8 guidelines.

### 3. Fixer Agent
- Suggests corrected Python code.
- Attempts to preserve the original intended functionality.
- Explains the changes made to improve the code.

### 4. Test-Writer Agent
- Generates pytest test cases.
- Covers normal inputs and boundary conditions.
- Suggests tests for invalid inputs and exceptional situations.

**Note:** The Test-Writer generates test code. It does not automatically execute the generated tests in this prototype.

---

## 🏗️ System Architecture

The application follows this workflow:

1. **User Input:** The user submits Python code through the Streamlit interface.
2. **Intent Selection:** The user selects a review task or requests a full review.
3. **RAG Retrieval:** ChromaDB retrieves relevant coding guidelines.
4. **Prompt Construction:** LangChain combines the agent's instructions, user intent, submitted code, and retrieved guidance.
5. **AI Processing:** Groq processes the prompts using the configured language model.
6. **Agent Response:** The selected AI agents generate their respective results.
7. **Output:** Streamlit displays the generated code-review results.

### Architecture Flow

```text
           USER
             |
             v
       STREAMLIT UI
             |
             v
      INTENT SELECTION
             |
             v
     CHROMADB (RAG)
             |
             v
    LANGCHAIN LCEL CHAIN
             |
             v
          GROQ LLM
             |
             v
      SELECTED AI AGENTS
             |
      +------+------+------+
      |      |      |      |
    BUG   STYLE   FIXER  TEST
   FINDER  LINT  AGENT  WRITER
      |      |      |      |
      +------+------+------+
             |
             v
       FINAL AI OUTPUT
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Interactive web interface |
| Groq API | Language model inference |
| LangChain | Prompt and model integration |
| LangChain LCEL | Connects prompts, models and output parsers |
| ChromaDB | Vector database for coding guidelines |
| Pytest | Python automated testing framework |

---

## 🔍 Key Concepts Demonstrated

### 1. Large Language Model (LLM) Integration
Uses Groq's ChatGroq integration to communicate with a language model and generate code-review responses.

### 2. Prompt Engineering
Uses specialized system prompts to assign different responsibilities to the four AI agents.

### 3. LangChain LCEL
Uses LangChain Expression Language to connect the prompt, language model, and output parser:

```python
prompt | model | StrOutputParser()
```

### 4. Retrieval-Augmented Generation (RAG)
Uses ChromaDB to store coding guidelines, retrieve relevant documents through similarity search, and include the retrieved information in the AI prompt.

### 5. Intent-Based Agent Routing
The application selects the appropriate agent based on the user's chosen task. A full review invokes all four agents.

### 6. Vector Database
Uses ChromaDB's persistent collection and embedding function to store and retrieve coding guideline documents.

---

## 📁 Project Structure

```text
Code-Review-Debug-Squad/
│
├── app.py
├── agents.py
├── rag_store.py
├── divide_utils.py
├── test_divide.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later (use a version compatible with the project dependencies).
- Git.
- A Groq API key.

### Step 1: Clone the repository

```bash
git clone https://github.com/akashbabli01/Code-Review-Debug-Squad.git
```

### Step 2: Open the project folder

```bash
cd Code-Review-Debug-Squad
```

### Step 3: Create a virtual environment

```powershell
python -m venv venv
```

### Step 4: Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Configure the Groq API key

Create your local `.env` file using:

```powershell
copy .env.example .env
```

Open `.env` and configure:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=your_supported_model_name
```

Replace the example values with your actual credentials and supported model.

**Security:** Never upload your `.env` file or expose your API key on GitHub.

---

## ▶️ Run the Application

Start the Streamlit application:

```powershell
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

Enter Python code, select the required review task, and view the AI-generated results.

---

## 🧪 Testing

The project includes a Python division utility and pytest test cases.

Run the tests using:

```powershell
python -m pytest test_divide.py -v
```

### Test Results

The four test cases successfully passed:

| Test Case | Result |
|---|---|
| Normal division | PASSED |
| Float division | PASSED |
| Division by zero | PASSED |
| Invalid input | PASSED |

**Test execution result: 4 passed.**

These tests validate the division utility. They are separate from the Test-Writer agent's generated test suggestions.

---

## ⚠️ Limitations

This project is an educational prototype developed to demonstrate multi-agent AI concepts.

- AI-generated suggestions may not always be correct.
- Generated test cases are not automatically executed by the application.
- Submitted code is not automatically executed or modified.
- The system is not a replacement for professional code auditing or security analysis.
- Production deployment would require sandboxed execution, stronger error handling, authentication, evaluation, and logging.

---

## 🚀 Future Enhancements

- Integrate automated test execution in a secure sandbox.
- Add support for additional programming languages.
- Integrate static-analysis tools such as Pylint and Flake8.
- Add code-quality scoring.
- Support GitHub repository integration.
- Maintain review history and reports.
- Improve agent coordination and evaluation.

---

## 👨‍💻 Author

**Akash Babli**

GitHub: [akashbabli01](https://github.com/akashbabli01)

**Project:** Code Review & Debug Squad

**Domain:** Artificial Intelligence | Agentic AI | Python Development

---

## 📌 Conclusion

Code Review & Debug Squad demonstrates how multiple specialized AI agents can assist developers in reviewing and improving Python code.

By combining Groq, LangChain LCEL, Streamlit, and ChromaDB, the project provides an interactive prototype for bug identification, code-quality review, code correction suggestions, and test-case generation.

The project demonstrates practical applications of Large Language Models, prompt engineering, RAG, vector databases, and multi-agent task routing.
