import logging
from threading import Lock

from langchain.tools import BaseTool
from langchain_mcp_adapters.client import MultiServerMCPClient

from .connections import create_mcp_connection

logger = logging.getLogger(__name__)

_mcp_client: MultiServerMCPClient | None = None
_lock = Lock()

def get_mcp_client() -> MultiServerMCPClient:
    """Get or create the singleton MCP client instance."""
    global _mcp_client
    
    if _mcp_client is None:
        with _lock:
            if _mcp_client is None:
                _mcp_client = create_mcp_connection()
    
    return _mcp_client

async def get_mcp_tools() -> list[BaseTool]:
    """Load tools from MCP servers."""
    try:
        client = get_mcp_client()
        tools = await client.get_tools()
        logger.info(f"Loaded {len(tools)} tools from MCP server")
        return tools
    except Exception as e:
        logger.error(f"Failed to load MCP tools: {e}")
        return []