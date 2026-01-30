import logging
import os

from langchain_mcp_adapters.client import MultiServerMCPClient

from constants.constants import DEFAULT_MCP_WEATHER_SERVER_URL

logger = logging.getLogger(__name__)

def create_mcp_connection() -> MultiServerMCPClient:
    """Create and configure MCP client connection."""
    server_url = os.getenv("MCP_WEATHER_SERVER_URL", DEFAULT_MCP_WEATHER_SERVER_URL)
    logger.info(f"Creating MCP connection to: {server_url}")
    
    return MultiServerMCPClient({
        "us_weather_mcp_server": {
            "transport": "streamable_http",
            "url": server_url,
        }
    })
