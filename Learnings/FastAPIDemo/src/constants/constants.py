from pathlib import Path

# LLM Configuration
DEFAULT_LLM_PROVIDER = "nvidia"
DEFAULT_LLM_MODEL = "meta/llama-3.1-405b-instruct"
DEFAULT_LLM_TEMPERATURE = 0.2
DEFAULT_OLLAMA_BASE_URL = "http://localhost:11434"

# MCP Configuration
DEFAULT_MCP_WEATHER_SERVER_URL = "https://your-mcp-server-url/mcp"

# Path Configuration 
ROOT_DIR = Path(__file__).resolve().parents[2]

