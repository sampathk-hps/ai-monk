# Weather MCP Server

A Model Context Protocol (MCP) server providing weather data tools using the National Weather Service API.

## Architecture

```
src/
├── server.py          # Singleton FastMCP instance
├── tools/             # MCP tools (auto-registered)
│   ├── get_alerts.py
│   └── get_forecast.py
├── utils/             # Helper functions
└── constants/         # Configuration
```

## Available Tools

- `get_alerts(state)` - Get weather alerts for a US state
- `get_forecast(latitude, longitude)` - Get weather forecast for coordinates

## Usage

### Run the server
```bash
fastmcp run main.py
```

### Test locally
```bash
python client.py
```

### Inspect with MCP Inspector
```bash
npx @modelcontextprotocol/inspector python main.py
```

## Adding New Tools

1. Create tool file in `src/tools/`
2. Decorate function with `@mcp.tool()`
3. Export in `src/tools/__init__.py`
4. Auto-registered on import