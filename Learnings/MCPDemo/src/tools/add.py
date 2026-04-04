from src.server import mcp

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers and return the result"""
    return a + b