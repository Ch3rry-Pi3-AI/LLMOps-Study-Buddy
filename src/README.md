# `src/` README — Core Source Code Structure

The `src/` directory contains the **primary source code** for the LLMOps StudyBuddy project.
It includes the foundational modules for configuration, logging, reliability utilities, typed Pydantic schemas, prompt templates, the Groq LLM client, the question-generation engine, and now utility helpers used by the Streamlit UI and quiz logic.

As the project expands, this directory will grow to include pipelines, tutoring agents, retrieval workflows, orchestration layers, and evaluation modules.

At this stage, the `src/` directory includes:

* `common/` — shared reliability utilities
* `config/` — global configuration and environment loading
* `models/` — typed schemas for structured question data
* `prompts/` — LangChain prompt templates for question generation
* `llm/` — Groq client wrapper for executing model calls
* `generator/` — high-level service for generating structured study questions
* `utils/` — helpers for Streamlit UI and quiz management

## 📁 Folder Overview

```text
src/
├─ common/       # Core utilities for reliability (exceptions, logging)
├─ config/       # Global project configuration (environment + settings)
├─ models/       # Typed data schemas for study questions
├─ prompts/      # Prompt templates for LLM-driven question generation
├─ llm/          # Groq language model client and future LLM utilities
├─ generator/    # High-level question generation service
└─ utils/        # Streamlit helpers and quiz management tools
```

# 📦 `common/` — Shared Reliability Utilities

The `common/` folder provides low-level utilities that ensure consistent, predictable system behaviour.

### Contains

```text
src/common/
├─ __init__.py
├─ custom_exception.py     # Detailed, standardised error handling
└─ logger.py               # Centralised, timestamped logging system
```

### Functionality

* **`custom_exception.py`**
  Provides a `CustomException` including filename, line number, and traceback context.

* **`logger.py`**
  Implements structured, timestamped, daily-rotating logs for consistent observability.

These utilities underpin debugging and monitoring throughout the StudyBuddy codebase.

# ⚙️ `config/` — Global Configuration Layer

The `config/` directory centralises all configuration and environment-driven variables.

### Contains

```text
src/config/
├─ __init__.py
└─ settings.py            # Loads environment variables and defines global runtime parameters
```

### Functionality

* Loads environment variables via `dotenv`.
* Defines key configuration via a typed `Settings` class:

  * `GROQ_API_KEY`
  * `MODEL_NAME`
  * `TEMPERATURE`
  * `MAX_RETRIES`
* Exposes a global `settings` instance.

# 🧠 `models/` — Typed Question Schemas

This directory defines Pydantic models used throughout StudyBuddy for structured, validated question data.

### Contains

```text
src/models/
├─ __init__.py
└─ question_schemas.py     # MCQ and fill-in-the-blank schemas
```

### Functionality

* **`MCQQuestion`** — A structured, validated multiple-choice question model
* **`FillBlankQuestion`** — A validated fill-in-the-blank question model

These schemas ensure all generated questions follow strict, predictable rules.

# 🎨 `prompts/` — LLM Prompt Templates

This directory defines the reusable LangChain template objects used for question generation.

### Contains

```text
src/prompts/
├─ __init__.py
└─ templates.py            # MCQ + fill-in-the-blank templates
```

### Functionality

* Produces strict JSON output expected by the Pydantic schemas
* Provides reusable patterns for generating educational content

# ⚡ `llm/` — Groq Language Model Client

This folder contains the Groq client logic used to initialise the model.

### Contains

```text
src/llm/
├─ __init__.py
└─ groq_client.py          # Factory function returning a configured Groq Chat model
```

### Functionality

* Provides a consistent entry point for creating a Groq Chat model
* Ensures all LLM calls use centralised configuration from `settings.py`

# 🧪 `generator/` — Question Generation Service

This directory contains the high-level service that ties prompts, the LLM, and Pydantic models together.

### Contains

```text
src/generator/
├─ __init__.py
└─ question_generator.py     # MCQ + fill-blank generation with retries and validation
```

### Functionality

* Integrates:

  * Groq model
  * Prompt templates
  * Pydantic output parsers
  * Retry logic
  * Structured logging
* Provides:

  * `generate_mcq(topic, difficulty)`
  * `generate_fill_blank(topic, difficulty)`

# 🧰 `utils/` — Streamlit Helpers & Quiz Management

The `utils/` directory contains lightweight utility tools used by the Streamlit interface and quiz workflow.

### Contains

```text
src/utils/
├─ __init__.py
└─ helpers.py          # QuizManager + Streamlit rerun helper
```

### Functionality

* `rerun()` — toggles Streamlit session state to refresh UI
* `QuizManager` — generates quizzes, collects answers, evaluates correctness, and exports results

This folder supports the front-end experience and user interaction flow.

# ✅ Summary

* `src/` now contains configuration, reliability, schema, prompt, LLM, generation, and utility modules.
* `common/` and `config/` provide system stability and consistent configuration.
* `models/`, `prompts/`, and `generator/` form the core question-generation pipeline.
* `llm/` abstracts model access through a unified Groq client.
* `utils/` adds helpers and quiz management for the user-facing interface.

The structure is now ready for expansion into pipelines, tutoring agents, RAG systems, and evaluation workflows.
