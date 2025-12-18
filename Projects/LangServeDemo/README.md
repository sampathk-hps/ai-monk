# LangServe Demo - Joke Generator API

A production-ready demonstration of LangChain and LangServe integration, featuring a joke generator API with input validation, error handling, and structured logging.

## Components

```
LangServeDemo/
├── app/
│   └── client.py          # Client application with logging and error handling
├── core/
│   └── llm.py            # LLM configuration and initialization
├── servers/
│   └── server.py         # FastAPI server with production features
├── constants/
│   └── constants.py      # Application constants
├── prompts/
│   └── system.md         # System prompt templates
├── .env.example          # Environment variables template
└── pyproject.toml        # Project dependencies
```

## Requirements

Install dependencies using uv:
```bash
uv sync
```

## Configuration

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Configure your environment variables in `.env`:
```bash
NVIDIA_API_KEY=your_api_key_here
HOST=0.0.0.0
PORT=8080
```

## Running the Demo

### Start the Server
```bash
uv run python -m servers.server
```

### Use the Client
```bash
# Basic usage
uv run python -m app.client --topic Cricket

# Custom topic
uv run python -m app.client --topic "Machine Learning"
```

### Web Interfaces

**Interactive Playground:**
```
http://localhost:8000/joke-generator/playground/
```

**API Documentation:**
```
http://localhost:8000/docs
```

**Root Endpoint:**
```
http://localhost:8000/
```

## Production Features

- **Input Validation**: Topic length and character validation
- **Error Handling**: Comprehensive error handling with meaningful messages
- **Logging**: Structured logging with timestamps and performance metrics
- **Environment Configuration**: Configurable via environment variables
- **Security**: Input sanitization and validation
- **Monitoring**: Request timing and error tracking

## How It Works

This demo showcases production-ready LangChain and LangServe patterns:

- **Chains**: Input validator → Prompt template → LLM → Output parser
- **Deployment**: FastAPI server with LangServe integration
- **Client**: RemoteRunnable with error handling and logging
- **Configuration**: Environment-based configuration management
- **Validation**: Input validation and error handling throughout the pipeline

## API Usage

### Request Format
```json
{
  "topic": "your_topic_here"
}
```

### Response Format
```json
"Generated joke about your topic"
```

### Error Responses
- `400`: Invalid topic (empty, too long, or invalid characters)
- `500`: Server error (LLM initialization failure, etc.)