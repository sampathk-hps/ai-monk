from fastmcp import Client
from mcp.types import TextContent, TextResourceContents
import asyncio

async def async_main():
    async with Client("server_local_stdio.py") as client:  # Loads main.py locally via STDIO
        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)

        print("="*30)

        # Call the 'add' tool
        add_result = await client.call_tool("add", {"a": 5, "b": 7})
        if isinstance(add_result.content[0], TextContent):
            print("Add result:", add_result.content[0].text)
        else:
            print("Add result:", add_result.content)

        print("="*30)

        # Call the 'multiply' tool
        multiply_result = await client.call_tool("multiply", {"a": 3.5, "b": 2.0})
        if isinstance(multiply_result.content[0], TextContent):
            print("Multiply result:", multiply_result.content[0].text)
        else:
            print("Multiply result:", multiply_result.content)


        print("="*30)

        # Read a resource
        version = await client.read_resource("config://version")
        if isinstance(version[0], TextResourceContents):
            print("Version:", version[0].text)
        else:
            print("Version:", version)

        print("="*30)

        # Read a dynamic resource
        profile = await client.read_resource("user://123/profile")
        if isinstance(profile[0], TextResourceContents):
            print("Profile:", profile[0].text)
        else:
            print("Profile:", profile)

        print("="*30)

        # Call the 'summarize' tool on a resource
        summary_result = await client.call_tool("summarize", {"uri": "config://version"})
        if isinstance(summary_result.content[0], TextContent):
            print("Summary result:", summary_result.content[0].text)
        else:
            print("Summary result:", summary_result.content)

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()