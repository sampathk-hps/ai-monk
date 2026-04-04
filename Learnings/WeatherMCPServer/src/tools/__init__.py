"""Weather MCP Tools - Auto-registered with FastMCP.

All tools decorated with @mcp.tool() are automatically registered
when this module is imported.
"""

from .get_alerts import get_alerts
from .get_forecast import get_forecast

__all__ = ["get_alerts", "get_forecast"]