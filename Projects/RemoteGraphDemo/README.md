# RemoteGraphDemo

A LangGraph-based joke generator application that demonstrates remote graph execution using NVIDIA AI endpoints. The application creates jokes on any given topic using a state-based graph workflow.

## Features

- **LangGraph Integration**: Uses LangGraph for building and executing AI workflows
- **NVIDIA AI Endpoints**: Leverages NVIDIA's AI services for joke generation
- **Multiple Interfaces**: CLI application and REST API server
- **State Management**: Proper state handling with TypedDict schemas
- **Input Validation**: Pydantic models for request validation

## Prerequisites

- Python >= 3.13
- UV package manager
- NVIDIA API key

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Environment configuration**:
   ```bash
   cp .env.example .env
   # Edit .env and add your NVIDIA_API_KEY
   ```

## Usage

### Running the Server

Start the LangGraph development server:
```bash
uv run langgraph dev --config langgraph.json
```

The server will be available at `http://localhost:2024`

### CLI Application

Run the interactive CLI:
```bash
uv run python -m app.cli.cli_remote_graph_call
```

Enter topics when prompted, or type `exit`, `quit`, or `bye` to stop.

### API Access

Generate jokes via REST API:
```bash
curl -X POST http://localhost:2024/runs/stream \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "joke_generator",
    "input": {
      "topic": "Python programming"
    }
  }'
```

## Project Structure

```
├── agents/           # LangGraph agent definitions
├── app/cli/         # CLI application
├── constants/       # Application constants
├── core/           # Core LLM configurations
├── nodes/          # Graph node implementations
├── prompts/        # System prompts
├── schema/         # Pydantic schemas
├── state/          # State definitions
├── langgraph.json  # LangGraph configuration
└── pyproject.toml  # Project dependencies
```

## Dependencies

- `langchain>=1.2.0` - LangChain framework
- `langchain-nvidia-ai-endpoints>=1.0.0` - NVIDIA AI integration
- `langgraph-cli[inmem]>=0.4.11` - LangGraph CLI tools

## Configuration

The application uses:
- `langgraph.json` for graph configuration
- `.env` for environment variables (NVIDIA_API_KEY, HOST, PORT)
- `joke_generator` as the assistant ID for API calls