# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
It includes the foundational modules responsible for configuration, logging, error handling, typed Pydantic schemas, LLM prompt templates, the Groq LLM client, and now the high-level question-generation service.
As the project evolves, this directory will expand to include pipelines, tutoring agents, retrieval workflows, orchestration layers, and evaluation modules.

At this stage, the `src/` directory includes:

* `common/` — shared reliability utilities
* `config/` — global configuration and environment loading
* `models/` — typed schemas for structured question data
* `prompts/` — LangChain prompt templates for question generation
* `llm/` — Groq client wrapper for executing model calls
* `generator/` — high-level service for generating structured study questions

## 📁 Folder Overview

```text
src/
├─ common/       # Core utilities for reliability (exceptions, logging)
├─ config/       # Global project configuration (environment + settings)
├─ models/       # Typed data schemas for study questions
├─ prompts/      # Prompt templates for LLM-driven question generation
├─ llm/          # Groq language model client and future LLM utilities
└─ generator/    # High-level question generation service
```

# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides the core modules that ensure consistent and predictable system behaviour.
Its reusable utilities support robust error handling and reliable logging across the entire project.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py     # Detailed, standardised error handling
└─ logger.py               # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Defines a `CustomException` enriched with filename, line number, and traceback.

* **`logger.py`**
  Implements a timestamped, daily-rotating logging system for structured observability.

These utilities underpin debugging, monitoring, and consistency across the StudyBuddy codebase.

# ⚙️ `config/` — Global Configuration Layer

The `config/` directory contains centralised configuration loaded from environment variables.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py            # Loads environment variables and defines global runtime parameters
```

### Functionality

* Loads environment variables using `dotenv`.

* Provides a strongly typed `Settings` class defining key parameters such as:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`

* Exposes a global `settings` object for easy import across modules.

# 🧠 `models/` — Typed Question Schemas

The `models/` directory defines Pydantic models used for validated question structures.

### Contains

```text
src/models/
├─ __init__.py
└─ question_schemas.py     # MCQ and fill-in-the-blank Pydantic models
```

### Functionality

* **`MCQQuestion`**
  Structured object with validation for multiple-choice questions.

* **`FillBlankQuestion`**
  Structured representation of fill-in-the-blank questions with placeholder enforcement.

These schemas ensure all generated questions follow a strict, predictable structure.

# 🎨 `prompts/` — LLM Prompt Templates

The `prompts/` directory contains reusable LangChain prompt templates for generating question JSON.

### Contains

```text
src/prompts/
├─ __init__.py
└─ templates.py           # MCQ + fill-in-the-blank prompt templates
```

### Functionality

* Enforces strict JSON output format.
* Ensures compatibility with Pydantic schemas.
* Provides reusable patterns for question-generation workflows.

# ⚡ `llm/` — Groq Language Model Client

The `llm/` directory contains the Groq client logic that initialises and configures the ChatGroq model.

### Contains

```text
src/llm/
├─ __init__.py
└─ groq_client.py         # Factory function returning a configured Groq Chat model
```

### Functionality

* Provides `get_groq_llm()` for initialising the Groq LLM
* Uses settings defined in `settings.py`
* Ensures consistent behaviour across all modules that invoke the LLM

# 🧪 `generator/` — Question Generation Service

The `generator/` directory contains the service responsible for orchestrating prompt templates, LLM calls, retries, and schema parsing to produce validated study questions.

### Contains

```text
src/generator/
├─ __init__.py
└─ question_generator.py     # High-level generator for MCQ + fill-blank questions
```

### Functionality

* Integrates:

  * Groq client
  * Prompt templates
  * Pydantic schemas
  * Retry logic
  * Structured logging

* Provides:

  * `generate_mcq(topic, difficulty)`
  * `generate_fill_blank(topic, difficulty)`

This module acts as the core engine for producing consistent and validated question objects.

# ✅ Summary

* `src/` is the central source directory for StudyBuddy.
* `common/` provides stable error handling and logging.
* `config/` manages global configuration and environment variables.
* `models/` defines validated data structures for questions.
* `prompts/` contains structured templates for LLM-based question generation.
* `llm/` encapsulates the Groq LLM client.
* `generator/` provides the unified service for generating structured questions.

The codebase is now ready to grow into pipelines, tutoring agents, retrieval systems, and advanced evaluation workflows.