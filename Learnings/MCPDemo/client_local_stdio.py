from fastmcp import Client
import asyncio

async def async_main():
    async with Client("main.py") as client:  # Loads main.py locally via STDIO
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)

        print("="*30)

        # Call the 'add' tool
        add_result = await client.call_tool("add", {"a": 5, "b": 7})
        print("Add result:", add_result.content[0].text)

        print("="*30)

        # Call the 'multiply' tool
        multiply_result = await client.call_tool("multiply", {"a": 3.5, "b": 2.0})
        print("Multiply result:", multiply_result.content[0].text)

        print("="*30)

        # Read a resource
        version = await client.read_resource("config://version")
        print("Version:", version)

        print("="*30)

        # Read a dynamic resource
        profile = await client.read_resource("user://123/profile")
        print("Profile:", profile)

        print("="*30)

        # Call the 'summarize' tool on a resource
        summary_result = await client.call_tool("summarize", {"uri": "config://version"})
        print("Summary result:", summary_result.content)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()