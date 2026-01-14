from src.server import mcp

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b
