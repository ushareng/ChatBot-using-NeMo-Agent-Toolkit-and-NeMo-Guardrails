# ChatBot using NeMo Agent Toolkit and NeMo Guardrails

This project is a **command-line chatbot** that integrates:

- **NeMo Agent Toolkit (NAT)** for running agent workflows via `nat run`
- **NeMo Guardrails** for defining conversational policies and behavior rules
- A lightweight Python wrapper that applies **pre-execution safety checks** and routes valid queries to a NeMo Agent workflow

The chatbot demonstrates how to combine **agent execution** with **guardrails-style policy enforcement** in a simple, inspectable setup.

<img width="757" height="222" alt="Demo" src="https://github.com/user-attachments/assets/2e4c71b6-7504-4304-894a-7057deb4c4d9" />


---

## How it works

1. User enters a prompt in the terminal.
2. A policy gate blocks requests that reference secrets (e.g., API keys or passwords).
3. Allowed prompts are passed to the **NeMo Agent Toolkit** using:
   ```bash
   nat run --config_file nat_config.yml --input "<user prompt>"
   ```
4. The agent workflow executes and returns a result.
5. The Python app extracts and prints the agent’s final response.

---

## Repository structure

```
.
├── app.py
├── nat_config.yml
└── rails_config/
    ├── config.yml
    └── rails.co
```

---

## Prerequisites

- Python 3.10+
- NeMo Guardrails
- NeMo Agent Toolkit (`nat` CLI available)
- Configured LLM backend supported by NAT

---

## Installation

```bash
git clone https://github.com/ushareng/ChatBot-using-NeMo-Agent-Toolkit-and-NeMo-Guardrails.git
cd ChatBot-using-NeMo-Agent-Toolkit-and-NeMo-Guardrails
python -m venv .venv
source .venv/bin/activate
pip install nemoguardrails
```

Install NeMo Agent Toolkit according to its documentation.

---

## Run the chatbot

```bash
python app.py
```

Exit using `exit` or `quit`.

---

## License

This project is licensed under the MIT License.

