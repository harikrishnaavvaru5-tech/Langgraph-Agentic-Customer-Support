# Langgraph Agentic Customer Support

## 📝 Project Overview

This project implements an **intelligent customer support agent** using **LangGraph** and **Agentic AI** principles.  
It leverages **LangChain**, **Python**, and **OpenAI** models to provide automated, context-aware customer support.

**Key Features:**

- Multi-agent orchestration for handling queries
- Integration with OpenAI GPT models
- Modular architecture for easy extension
- Virtual environment setup for isolated dependency management

---

## 💻 Project Structure

Langgraph-Agentic-Customer-Support/
│
├── src/
│ ├── orchestrator.py # Entry point for running the agent
│ ├── agents/ # Individual agent modules
│ └── tools/ # Helper modules and utilities
│
├── venv/ # Python virtual environment (ignored in Git)
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Langgraph-Agentic-Customer-Support.git
```

cd Langgraph-Agentic-Customer-Support

2️⃣ Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # For Git Bash
```

3️⃣ Install dependencies

# Initialize uv project

```bash
uv init --python 3.11
```

```bash
uv pip install langgraph langchain langchain-openai python-dotenv
```

4️⃣ Add your API keys
Create a .env file in the root directory:

```ini
OPENAI_API_KEY=your_openai_api_key_here
```

▶️ Running the Project
Run the orchestrator module:

```bash
python -m src.orchestrator
```
