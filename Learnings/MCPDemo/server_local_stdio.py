from src.server import mcp
import src.resources
import src.tools

def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()