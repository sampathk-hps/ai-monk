uv run langgraph dev --config langgraph.json

uv run python -m app.cli_remote_graph_call



curl -X POST http://localhost:2024/runs/stream \
  -H "Content-Type: application/json" \
  -d '{
    "assistant_id": "joke_generator",
    "input": {
      "topic": "Python programming"
    }
  }'