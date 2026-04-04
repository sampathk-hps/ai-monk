# MCP Demo - Three Connection Types

A demonstration of Model Context Protocol (MCP) server implementation with three different connection methods: STDIO, HTTP, and Remote deployment.

## Overview

This project showcases a FastMCP server with:
- **3 Tools**: `add`, `multiply`, `summarize`
- **2 Resources**: `config://version`, `user://{user_id}/profile`
- **3 Connection Types**: STDIO, Local HTTP, Remote (FastMCP Cloud)

## Project Structure

```
MCPDemo/
├── clients/                    # Client implementations
│   ├── client_local_stdio.py   # STDIO transport client
│   ├── client_local_http.py    # HTTP transport client
│   └── client_remote.py        # Remote MCP client
├── src/
│   ├── server/
│   │   └── server.py           # FastMCP server instance
│   ├── tools/                  # MCP tools
│   │   ├── add.py              # Addition tool
│   │   ├── multiply.py         # Multiplication tool
│   │   └── summarize.py        # Resource summarization tool
│   └── resources/              # MCP resources
│       ├── get_version.py      # Static version resource
│       └── get_profile.py      # Dynamic user profile resource
├── server_local_stdio.py       # STDIO server entrypoint
├── server_local_http.py        # HTTP server entrypoint
└── server_remote.py            # Remote deployment entrypoint
```

## Connection Types

### 1. STDIO (Standard Input/Output)

Direct process communication - client spawns server as subprocess.

**Run:**
```bash
python clients/client_local_stdio.py
```

**Use Case**: Local development, IDE integrations, desktop applications

---

### 2. Local HTTP

Server runs as HTTP endpoint, client connects via URL.

**Run:**
```bash
# Terminal 1 - Start server
python server_local_http.py

# Terminal 2 - Run client
python clients/client_local_http.py
```

**Server URL**: `http://127.0.0.1:8000/mcp`

**Use Case**: Local testing, microservices, containerized environments

---

### 3. Remote (FastMCP Cloud)

Deploy to FastMCP Cloud and access from anywhere.

**Deploy:**

1. Go to [https://fastmcp.cloud](https://fastmcp.cloud) and sign in with GitHub
2. Create a new project:
   - Select your GitHub repo (demo-mcp-server)
   - Specify entrypoint: `server_remote.py:mcp`
3. Wait for build and deployment (few minutes)
4. Note your unique URL (e.g., `https://your-project.fastmcp.cloud/mcp`)

**Run:**
```bash
# Update DEPLOYED_URL in client_remote.py
python clients/client_remote.py
```

**Use Case**: Production deployments, shared services, cloud-native applications

## Available Tools

- **add(a: int, b: int)**: Add two numbers
- **multiply(a: float, b: float)**: Multiply two numbers
- **summarize(uri: str)**: Summarize content from an MCP resource URI

## Available Resources

- **config://version**: Returns server version (1.0.0)
- **user://{user_id}/profile**: Returns user profile data (dynamic)

## Installation

```bash
# Install dependencies
uv sync

# Or with pip
pip install fastmcp python-dotenv
```

## Requirements

- Python >= 3.13.9
- fastmcp >= 2.14.3
- python-dotenv >= 1.2.1

## FastMCP Concepts

### Tools

FastMCP tools are simple Python functions that you decorate with @mcp.tool. You can add as many as you like.

### Resources

Resources in MCP represent read-only data that clients can access. You can create static resources or dynamic templates that take parameters. For example, you might expose a version number or a user profile.

### Using Context in Tools

FastMCP allows you to access the session context within any tool, resource, or prompt by including a ctx: Context parameter. The context gives you powerful capabilities like logging, LLM sampling, progress tracking, and resource access.

```python
@mcp.tool
async def summarize(uri: str, ctx: Context):
    await ctx.info(f"Reading resource from {uri}")
    data = await ctx.read_resource(uri)
    summary = await ctx.sample(f"Summarize this: {data.content[:500]}")
    return summary.text
```

This tool logs a message, reads a resource, and then asks the client's language model to summarise it. Context makes your MCP tools smarter and more interactive.
This tool logs a message, reads a resource, and then asks the client’s language model to summarise it. Context makes your MCP tools smarter and more interactive.