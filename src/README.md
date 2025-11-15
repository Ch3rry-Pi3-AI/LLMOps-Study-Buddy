# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
It includes the foundational modules responsible for configuration, logging, error handling, typed Pydantic schemas, LLM prompt templates, and now the Groq client used for model execution.
As the project grows, this directory will expand to include pipelines, agent logic, retrieval workflows, orchestration layers, and evaluation modules.

At this stage, the `src/` directory includes:

* `common/` — shared reliability utilities
* `config/` — global configuration and environment loading
* `models/` — typed schemas for structured question data
* `prompts/` — LangChain prompt templates for question generation
* `llm/` — Groq LLM client for executing model calls

Future modules (pipelines, agents, retrieval systems, evaluators, data loaders) will be added as development continues.

## 📁 Folder Overview

```text
src/
├─ common/      # Core utilities for reliability (exceptions, logging)
├─ config/      # Global project configuration (environment + settings)
├─ models/      # Typed data schemas for study questions
├─ prompts/     # Prompt templates for LLM-driven question generation
└─ llm/         # Groq language model client and future LLM utilities
```

# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides the core modules that support consistent, predictable system behaviour.
Its reusable utilities ensure robust error handling and reliable logging across the project.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py   # Detailed, standardised error handling
└─ logger.py             # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Defines a detailed `CustomException` that includes file name, line number, and traceback context.

* **`logger.py`**
  Implements a timestamped, daily-rotating logging system for consistent observability.

These utilities provide a strong foundation for debugging, monitoring, and error transparency.

# ⚙️ `config/` — Global Configuration Layer

The `config/` directory contains all configuration values and environment-driven settings used across StudyBuddy.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py     # Loads environment variables and defines global runtime parameters
```

### Functionality

* Loads environment variables with `dotenv`.

* Provides a strongly typed `Settings` class defining:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`

* Exposes a global `settings` instance for use in any module.

### Example

```python
from config.settings import settings
print(settings.MODEL_NAME)
```

# 🧠 `models/` — Typed Question Schemas

The `models/` directory defines the Pydantic models used to enforce structure and validation across all question-related data in StudyBuddy.

### Contains

```text
src/models/
├─ __init__.py
└─ question_schemas.py     # MCQ and fill-in-the-blank question models
```

### Functionality

* **`MCQQuestion`**
  Structured representation of an MCQ with option validation and normalisation.

* **`FillBlankQuestion`**
  Structured representation of fill-in-the-blank questions with placeholder handling.

These schemas support downstream operations such as:

* Question generation
* Study session workflows
* Evaluation pipelines
* RAG transformations
* Dataset ingestion and parsing

# 🎨 `prompts/` — LLM Prompt Templates

The `prompts/` folder contains reusable LangChain prompt templates designed to produce strictly structured JSON output.

### Contains

```text
src/prompts/
├─ __init__.py
└─ templates.py      # Prompt templates for MCQ + fill-in-the-blank generation
```

### Functionality

* Enforces strict JSON output format
* Ensures compatibility with `MCQQuestion` and `FillBlankQuestion` schemas
* Provides reusable templates for question-generation workflows

These templates ensure consistent, LLM-compatible question generation across the system.

# ⚡ `llm/` — Groq Language Model Client

The `llm/` directory contains the Groq client used to execute model calls in StudyBuddy.
It centralises LLM configuration and ensures all model invocations use the same settings.

### Contains

```text
src/llm/
├─ __init__.py
└─ groq_client.py     # Factory function returning a configured Groq Chat model
```

### Functionality

* Provides `get_groq_llm()` for creating a configured `ChatGroq` client
* Uses settings defined in `config/settings.py`
* Ensures consistent model behaviour across all modules

This folder will grow as the system expands to include:

* LLM pipelines
* Retry mechanisms
* Response post-processing
* Model selection tools

# ✅ Summary

* `src/` is the central codebase for the StudyBuddy application.
* `common/` handles reliability with robust logging and exception tools.
* `config/` centralises all environment and runtime configuration.
* `models/` defines validated structures for question data.
* `prompts/` provides structured templates for question generation.
* `llm/` contains the Groq client for model interaction.

The directory is now well-positioned to support upcoming modules such as pipelines, tutoring agents, retrieval integration, and evaluation workflows.
