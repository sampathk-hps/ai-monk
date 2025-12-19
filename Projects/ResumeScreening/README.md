# Resume Screening App

AI-powered resume screening application using LangChain, NVIDIA AI endpoints, and ChromaDB vector store.

## Features

- Upload resumes in PDF, DOCX, or TXT format
- Analyze resume against job requirements using LLM
- Get suitability score and detailed analysis
- Store resumes in vector database for future retrieval
- Interactive chat to ask questions about the analysis
- Download analysis results

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Configure environment variables:
```bash
cp .env.example .env
# Add your NVIDIA API key to .env
```

## Run

From the project directory:
```bash
PYTHONPATH=. uv run streamlit run app/main.py
```

## Usage

1. Enter job requirements in the left panel
2. Upload a resume (PDF/DOCX/TXT) in the right panel
3. Click "Analyze" to get AI-powered screening results
4. View suitability score and detailed analysis
5. Use the chat interface to ask follow-up questions
6. Download the analysis report

## Sample Files

Sample resumes and job descriptions are available in the `data/` folder for testing.