# `config/` README — Project Configuration (Settings Module)

The `config/` directory provides the **central configuration layer** for the **LLMOps StudyBuddy** project.
It defines project-wide settings such as API keys, model parameters, and operational behaviour.
By keeping configuration isolated, the project remains clean, maintainable, and easy to adapt across different environments.

## 📁 Folder Overview

```text
src/config/
├─ __init__.py        # Marks the directory as a package
└─ settings.py        # Centralised configuration for API keys and model behaviour
```

## ⚙️ `settings.py` — Global Configuration

### Purpose

The `settings.py` module defines all global settings used throughout the StudyBuddy system.
It loads sensitive values from environment variables and exposes structured configuration attributes through a `Settings` class.

### What It Provides

* Secure loading of credentials from a `.env` file.
* Centralised management of API keys, model name, temperature, retry limits, and other global parameters.
* A single `settings` object that can be imported anywhere in the codebase.

### Example Usage

```python
from config.settings import settings

print(settings.MODEL_NAME)
print(settings.GROQ_API_KEY)
```

### Example Output

```
llama-3.1-8b-instant
sk_groq_****************************
```

## 🔑 Environment Variables

This module expects values to be defined in your `.env` file.
For example:

```
GROQ_API_KEY="your_api_key_here"
```

These values are automatically loaded when the module imports.

## ✅ Summary

* `settings.py` provides a unified configuration source for the entire StudyBuddy project.
* All environment variables and model parameters are stored safely and consistently.
* The `config/` folder ensures separation of concerns between configuration, logic, and utilities.