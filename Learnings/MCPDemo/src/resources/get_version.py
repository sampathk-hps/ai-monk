from src.server import mcp

@mcp.resource("config://version")
def get_version():
    return "1.0.0"