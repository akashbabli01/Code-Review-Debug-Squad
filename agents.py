import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

AGENTS = {
    "Bug-Finder Agent": "Find syntax risks, logical bugs, edge cases and runtime risks. Explain each finding.",
    "Style/Lint Agent": "Review naming, readability, formatting, maintainability and Python conventions.",
    "Fixer Agent": "Suggest a corrected version of the code. Preserve intended behavior and explain changes.",
    "Test-Writer Agent": "Create useful pytest test cases, including normal cases, boundary cases and invalid inputs. Do not claim tests were executed."
}

def _chain(system_prompt):
    model = ChatGroq(
        api_key=os.environ["GROQ_API_KEY"],
        model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
        temperature=0
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt + "\nUse the retrieved coding guidance when relevant. Be accurate; state uncertainty."),
        ("human", "User intent: {intent}\nRetrieved guidance:\n{context}\n\nPython code:\n```python\n{code}\n```")
    ])
    return prompt | model | StrOutputParser()

def run_agent(code, intent, context):
    tasks = {
        "Find bugs": ["Bug-Finder Agent"],
        "Review style": ["Style/Lint Agent"],
        "Suggest fixes": ["Fixer Agent"],
        "Generate tests": ["Test-Writer Agent"],
        "Full review": list(AGENTS.keys())
    }
    selected = tasks[intent]
    sections = []
    for name in selected:
        sections.append(f"## {name}\n" + _chain(AGENTS[name]).invoke({
            "intent": intent, "context": context or "No matching guidance found.", "code": code
        }))
    return "\n\n".join(sections)
