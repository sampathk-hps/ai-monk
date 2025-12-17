# LegalDocReview

LegalDocReview is a Retrieval-Augmented Generation (RAG) application designed to assist in reviewing legal documents. It leverages NVIDIA's AI endpoints to ingest PDF documents, create embeddings, and allow users to query the content using natural language.

## Features

- **PDF Document Loading**: Ingests legal documents from a local directory.
- **Vector Search**: Utilizes FAISS and NVIDIA Embeddings for semantic search.
- **Contextual Q&A**: Uses ChatNVIDIA to answer questions based on the retrieved document context.
- **Source Citations**: Provides references to the specific files used to generate the answer.

## Setup

1. **Environment Configuration**:
   Use `.env.example` to create your `.env` file.

2. **Navigate to the Project Directory**:
   ```bash
   cd ./Projects/LegalDocReview/
   ```

## Usage

### Running the Application

To run the main application in the Command Line Interface (CLI):

```bash
uv run python -m app.build_vector_store
uv run python -m app.main
```

### Testing Components

To run the project files (e.g., test LLM connection):

```bash
uv run python -m core.llm
```
