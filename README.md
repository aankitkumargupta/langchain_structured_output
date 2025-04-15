# 🧠 Learning Structured Outputs in LangChain

Welcome to this resource on working with **structured outputs** in LangChain! This repository provides various examples, from basic Pydantic and TypedDict usage to more complex JSON Schema integration. Whether you're new to LangChain or looking to understand how to model and extract structured data with large language models (LLMs), this repository is designed to be a step-by-step guide.

---

## 📘 What You'll Learn

✅ Basics of schema-based data modeling  
✅ How to define and use structured outputs in LangChain  
✅ Comparing `TypedDict`, `Pydantic`, and `JSON Schema`  
✅ Extracting structured data like summaries, sentiment, and pros/cons from text  
✅ Using `.with_structured_output()` in LangChain

---

## 🛠️ Prerequisites

Before getting started, ensure you have the following installed:

```bash
pip install langchain-openai pydantic python-dotenv
```

Set your environment variables in a `.env` file:

```plaintext
OPENAI_API_KEY=your-key-here
HUGGINGFACEHUB_API_TOKEN=your-token-if-applicable
```

---

## 📂 File-by-File Breakdown

### `pydantic_demo.py` – 🎓 Intro to Pydantic

This script introduces **Pydantic** for type-safe data validation.

- Defines a simple `Student` model with fields like name, email, CGPA.
- Demonstrates how defaults, field validation, and serialization (`model_dump_json`) work.

🧠 **Why important?**  
Understanding how Pydantic works is crucial because LangChain supports `Pydantic` for structured outputs.

---

### `typeddict_demo.py` – 🔤 Intro to TypedDict

A foundational look at **TypedDict** from Python’s typing module.

- Simple `Person` schema using `TypedDict`.
- Sets the stage for more advanced TypedDict usage with LangChain.

🧠 **Why important?**  
LangChain allows schemas defined using `TypedDict` to define output structures in a lightweight way.

---

### `structured_output_simple_typedict.py` – 🟢 Getting Started with TypedDict + LangChain

The simplest use of LangChain’s `with_structured_output()`.

- Defines a basic schema using `TypedDict` (only `summary` and `sentiment`).
- Passes a short paragraph and extracts structured results.

🧠 **Key takeaway:**  
Great starting point. Helps you grasp how LangChain converts unstructured text into structured Python objects.

---

### `structured_output_annotated_typedict.py` – ✍️ Annotated TypedDict for Better Prompts

Introduces **TypedDict with Annotations** (e.g. field descriptions).

- Adds richer metadata to fields using `Annotated`.
- Useful when you want the LLM to better understand what each field means.

Schema includes:
- `key_themes`: Key themes or topics that are present in the given text, helping you understand the main points.
- `summary`: A short, concise overview or summary of the content.
- `sentiment`: The emotional tone or sentiment of the text, such as positive, negative, or neutral.
- `pros`: Positive aspects or benefits mentioned in the text.
- `cons`: Negative aspects or drawbacks mentioned in the text.

🧠 **Why use Annotated?**  
More explicit prompts to guide LLMs can improve output quality and accuracy.

---

### `structured_output_pydantic.py` – ⚙️ LangChain + Pydantic for Structured Output

Demonstrates using **Pydantic BaseModel directly with LangChain**.

- Pydantic gives detailed validation and field control.
- Useful in production workflows where data integrity matters.

Adds:
- Schema validation with types and optional fields
- Better IDE and runtime support for structured fields

🧠 **Why choose Pydantic over TypedDict?**  
Better validation, default handling, and model serialization.

---

### `structured_output_json.py` – 🧾 Using Raw JSON Schema

This example shows how to define structured outputs using a **JSON Schema** dictionary.

- Mirrors real-world scenarios where schemas come from external JSON files or APIs.
- Useful for working with tools that expect standard schema definitions.

Schema includes:
- `key_themes`: Major themes or important concepts from the text.
- `summary`: A concise summary that encapsulates the main message.
- `sentiment`: The tone or emotional feeling conveyed in the text.
- `pros`: Positive points or advantages mentioned in the content.
- `cons`: Negative points or disadvantages mentioned in the content.
- `name`: A specific title or identifier for the text content, useful when labeling.

🧠 **Why use JSON Schema?**  
Most flexible and widely supported schema format, especially for interoperability.

---

### `json_schema.json` – 📄 Sample Schema File

A sample JSON schema defining a `student` object with `name` and `age`.

🧠 Use this as a blueprint to create and load JSON schema files dynamically.

---

## 🧪 Running the Examples

Pick any script and run it individually to test and learn:

```bash
python structured_output_pydantic.py
```

Observe the output in structured format like a dictionary or JSON.

---

## 🔍 Comparison Summary

| Approach       | Validation | Flexibility | IDE Support | Best Use Case                         |
|----------------|------------|-------------|-------------|----------------------------------------|
| `TypedDict`    | Basic      | Light       | Medium      | Quick prototypes and simple use cases |
| `Annotated`    | Moderate   | Medium      | Medium      | Descriptive prompts                   |
| `Pydantic`     | Strong     | High        | Excellent   | Production pipelines                  |
| `JSON Schema`  | High       | Very High   | External    | Schema-driven or API integration      |

---

## 🕹️ When to Use

### `TypedDict`
- **When to use:**  
  Use `TypedDict` when you only need basic structure reinforcement without data validation. It is ideal when you trust the LLM to return the correct answer and there’s no need for type enforcement.
  
- **Best for:**  
  - Quick prototypes
  - Simple schemas that don't require strict validation or defaults
  - When you rely on LLM's inherent structure without much control

### `Pydantic`
- **When to use:**  
  Use **Pydantic** when you need **data validation**. It's especially useful when the LLM might miss a field, and you want to ensure that missing values can be handled with defaults. Pydantic also helps with **automating type conversion** (e.g., from string to integer).
  
- **Best for:**  
  - Production environments where data integrity is key
  - Complex validation of fields
  - Default handling when LLM misses fields
  
### `JSON Schema`
- **When to use:**  
  Use **JSON Schema** when you need a **standardized, flexible schema** that can be used across multiple systems. JSON Schema is helpful when you are integrating with APIs or services that expect a particular schema definition. It's ideal for interoperability between systems.
  
- **Best for:**  
  - External API integrations
  - Working with tools that require standard schema definitions
  - When flexibility and extensive validation options are needed

---

## 🤝 Contributing

If you’d like to add new examples or extend this repo with new use cases (e.g., multiple outputs, nested schemas, real APIs), feel free to contribute!

---

## 👋 Final Words

This repo is more than just code; it’s a **learning path** to mastering structured outputs with LLMs. Start small, understand the differences, and level up your LangChain skills!

