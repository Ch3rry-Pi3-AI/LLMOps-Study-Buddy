# `llm/` README — Groq Language Model Client

The `llm/` directory contains the components responsible for connecting to and configuring the **Groq LLM** used throughout the LLMOps StudyBuddy project.
This folder isolates all LLM initialisation logic, ensuring that model configuration remains consistent, centralised, and easy to update as the project evolves.

At this stage, the folder includes a single module that constructs a configured Groq client.

## 📁 Folder Overview

```text
src/llm/
├── groq_client.py     # ⚡ Factory function returning a configured Groq Chat model
└── README.md          # 📚 Documentation for the llm module
```

## ⚡ `groq_client.py` — Groq LLM Client Factory

This module provides a single function, `get_groq_llm`, which returns an instance of the `ChatGroq` model configured using global settings from the `config/settings.py` file.

### What It Does

* Instantiates a Groq language model with:

  * API key
  * Model name
  * Temperature
* Ensures all LLM access goes through a single controlled entry point
* Keeps model configuration **centralised** and **synchronised** across the system

### Example Usage

```python
from llm.groq_client import get_groq_llm

llm = get_groq_llm()
response = llm.invoke("Explain recursion with an example.")
print(response)
```

This pattern prevents configuration drift and simplifies testing, maintenance, and future LLM upgrades.

## 🧩 How This Fits Into the StudyBuddy Project

The `llm/` folder acts as the **LLM abstraction layer**.
As the system grows, this folder will likely expand to include:

* LLM pipelines tailored to tasks (question generation, explanation synthesis, tutoring dialogue)
* Reusable wrappers for formatting model input/output
* Rate-limiting, error-handling, and retry logic
* Model-selection utilities for switching between Groq, OpenAI, Anthropic, etc. if needed

Centralising these behaviours ensures reliability and modularity across the StudyBuddy ecosystem.

## ✅ Summary

The `llm/` folder provides:

* A clean, single entry point for Groq model initialisation
* Consistent configuration via the global settings module
* A scalable abstraction layer for future LLM tooling