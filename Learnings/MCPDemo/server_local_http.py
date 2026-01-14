from src.server import mcp
import src.resources
import src.tools

def main():
    mcp.run(transport="http", host="127.0.0.1", port=8000, path="/mcp")

if __name__ == "__main__":
    main()