# ⚡ **Groq LLM Client — LLMOps StudyBuddy**

This branch introduces the **first LLM integration** for the **LLMOps StudyBuddy** project.
It adds a lightweight client wrapper for the **Groq language model**, enabling the rest of the system to generate questions, explanations, and study content through a single, consistent interface.

By centralising the LLM initialisation, the project gains:

* Consistent configuration
* Cleaner imports across modules
* Easy future upgrades (model switching, retries, caching, etc.)

## 🗂️ **Updated Project Structure**

Only the **new folder and file** added in this branch are annotated:

```text
LLMOPS-STUDY-BUDDY/
├── .venv/
├── .env
├── .gitignore
├── .python-version
├── llmops_study_buddy.egg-info/
├── manifests/
├── pyproject.toml
├── requirements.txt
├── setup.py
├── uv.lock
├── src/
│   ├── common/
│   ├── config/
│   ├── models/
│   ├── prompts/
│   └── llm/
│       └── groq_client.py     # ⚡ Factory function returning a configured Groq Chat model
└── README.md
```

## 🧠 **What This Branch Adds**

### ⚡ `groq_client.py`

This module defines a single helper function:

`get_groq_llm()`

It:

* Creates a configured **ChatGroq** client
* Uses global configuration from `settings.py`
* Ensures all LLM calls use the same:

  * API key
  * Model name
  * Temperature

Centralising this logic prevents configuration drift and keeps future integrations clean and maintainable.

### Key Benefits

* One reliable entry point for all model interactions
* Simplifies pipelines, agents, and services that need LLM access
* Makes model swapping trivial (e.g., newer Groq models or other providers)

## 🧪 **Example Usage**

```python
from llm.groq_client import get_groq_llm

llm = get_groq_llm()
response = llm.invoke("Explain the difference between precision and recall.")
print(response)
```

This pattern allows every component of StudyBuddy to use the LLM safely and consistently.

## ✅ **In Summary**

This branch:

* Adds a dedicated **`llm/`** folder for all language-model tooling
* Introduces a central **Groq client factory**
* Ensures consistent model configuration across the entire project
* Lays the groundwork for future components:

  * question-generation pipelines
  * tutoring agents
  * retrieval-augmented reasoning
  * LLM orchestration tools
