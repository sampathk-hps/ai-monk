from fastmcp import Context
from src.server import mcp

@mcp.tool
async def summarize(uri: str, ctx: Context):
    """Summarize the content of a given MCP resource URI"""
    await ctx.info(f"Reading resource from {uri}")
    data = await ctx.read_resource(uri)
    # For demo, simulate a summary (in real use, you could call an LLM here)
    summary = f"Summary of {uri}: {str(data)}"
    return summary