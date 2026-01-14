from fastmcp import Client
import asyncio

async def async_main():
    try:
        async with Client("main.py") as client:
            tools = await client.list_tools()
            print("\nAvailable tools:")
            for tool in tools:
                print(f"  - {tool.name}: {tool.description}")
                print("="*30)
            
            print("\nTesting add tool...")
            result = await client.call_tool("get_alerts", {"state": "NY"})
            print(f"Result: {result.content[0].text}") # type: ignore

    except Exception as e:
        print(f"Error: {e}")

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
