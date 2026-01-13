---
title: Fast Api Demo
emoji: 👀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
short_description: 'Demo of FastAPI AI application deployment '
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## Project Overview

A production-ready FastAPI application with LangChain-powered AI agents, supporting multiple LLM providers (NVIDIA, Google Gemini). Includes a weather agent with tool-calling capabilities.

## Folder Structure

```
FastAPIDemo/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   └── weather_agent.py          # Weather agent with tool integration
│   ├── constants/
│   │   └── constants.py               # Application constants
│   ├── core/
│   │   └── llm/
│   │       ├── providers/
│   │       │   ├── __init__.py
│   │       │   ├── gemini.py          # Google Gemini provider
│   │       │   └── nvidia.py          # NVIDIA NIM provider
│   │       ├── __init__.py
│   │       ├── base.py                # Base LLM interface
│   │       ├── client.py              # LLM client
│   │       └── factory.py             # LLM factory pattern
│   ├── prompts/
│   │   ├── __init__.py
│   │   └── system_prompt.py           # System prompts
│   ├── server/
│   │   ├── endpoints/
│   │   │   ├── chat/
│   │   │   │   ├── models.py          # Pydantic models
│   │   │   │   └── routes.py          # Chat endpoints
│   │   │   └── __init__.py
│   │   └── main.py                    # FastAPI app
│   └── tools/
│       ├── __init__.py
│       └── weather_tool.py            # Weather tool implementation
├── .env.example                       # Environment variables template
├── .gitignore
├── Dockerfile                         # Docker configuration for HF Spaces
├── main.py                            # Application entry point
├── pyproject.toml                     # Project dependencies
├── uv.lock                            # Locked dependencies
└── README.md
```

## Local Testing

### Test Complete Application
```bash
uv run fastapi
```

### Test Agent Only
```bash
uv run weather-agent-test
```

### Test LLM Only
```bash
uv run llm-test
```

## Deploy to Hugging Face Spaces

### 1. Create a New Hugging Face Space with Docker SDK

- Go to [huggingface.co/new-space](https://huggingface.co/new-space)
- Choose your username/organization as the owner
- Enter a Space name (e.g., `fast-api-demo`)
- Select **Docker** as the SDK (critical — Gradio/Streamlit won't work for pure FastAPI)
- Choose hardware: Start with CPU basic (free); upgrade to GPU if your agent loads heavy local models
- Set visibility to Public (for a callable public API)

### 2. Push Directly from Your Local Repository

```bash
git init
git remote add hf https://huggingface.co/spaces/your-username/your-space-name
git add .
git commit -m "Huggingface initial commit"
git push hf main:main
```

### 3. Add Secrets for API Keys

- Go to Space → Settings → Secrets → Add secrets
- Add the following secrets (refer to `.env.example`):
  - `LLM_PROVIDER` (nvidia or google)
  - `LLM_MODEL`
  - `LLM_TEMPERATURE`
  - `NVIDIA_API_KEY` (if using NVIDIA)
  - `GOOGLE_API_KEY` (if using Google Gemini)
- Rebuild the Space (trigger via a new commit or manually)

### 4. Test and Go Live

- Once built successfully (green status), your public API is live
- Test Swagger UI: `https://your-username-your-space-name.hf.space/docs`
- API endpoint: `https://your-username-your-space-name.hf.space/api/v1/chat`

## API Usage

### Chat Endpoint

**POST** `/api/v1/chat`

**Request Body:**
```json
{
    "message": "What's the weather like in New York?",
    "thread_id": "session-123"
}
```

**Response:**
```json
{
    "response": "Weather information from the agent",
    "thread_id": "session-123"
}
```

## Environment Variables

Refer to `.env.example` for all required environment variables:

- `LLM_PROVIDER`: Choose between `nvidia` or `google`
- `LLM_MODEL`: Model name (e.g., `meta/llama-3.1-405b-instruct`)
- `LLM_TEMPERATURE`: Temperature for LLM responses (0.0 - 1.0)
- `NVIDIA_API_KEY`: Your NVIDIA API key
- `GOOGLE_API_KEY`: Your Google API key
- `API_HOST`: Host address (default: `0.0.0.0`)
- `API_PORT`: Port number (default: `8000`)

