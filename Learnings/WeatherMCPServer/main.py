from src.server import mcp
import src.tools  # Auto-registers all tools via @mcp.tool() decorators

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
