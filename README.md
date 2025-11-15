# MCP Server for Claude Desktop

This repository contains a Model Context Protocol (MCP) server that provides user profile lookup tools for Claude Desktop.

## Overview

This MCP server exposes a `get_user_name` tool that retrieves user information from a mock database. It's built using the FastMCP framework and can be integrated with Claude Desktop.

## Prerequisites

- Python 3.9 or higher
- Claude Desktop application
- `fastmcp` Python package

## Installation

1. **Clone or download this repository**

2. **Install required Python packages:**

```bash
pip install fastmcp
```

3. **Verify Python installation:**

Make sure Python is installed and note its path. You can find it by running:

```bash
# On Windows
where python

# On macOS/Linux
which python3
```

## Configuration for Claude Desktop

### Step 1: Locate Claude Desktop Configuration File

The Claude Desktop configuration file is located at:

- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

### Step 2: Update Configuration

Open the `claude_desktop_config.json` file and add the MCP server configuration:

```json
{
  "mcpServers": {
    "MockMCP": {
      "command": "C:\\Python313\\python.exe",
      "args": [
        "-u",
        "C:\\MCPservertest\\mcp\\data.py",
        "--transport",
        "stdio"
      ],
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

**Important:** Update the paths in the configuration:
- Replace `C:\\Python313\\python.exe` with your actual Python executable path
- Replace `C:\\MCPservertest\\mcp\\data.py` with the full path to your `data.py` file

**Note for Windows users:** Use double backslashes (`\\`) in the JSON file paths.

### Step 3: Restart Claude Desktop

After updating the configuration file, completely quit and restart Claude Desktop for the changes to take effect.

## Usage

Once configured, you can use the MCP server tools in Claude Desktop:

### Available Tools

#### `get_user_name`
Retrieves the name of a user by their ID.

**Parameters:**
- `user_id` (string): The user ID (e.g., "1" or "2")

**Example usage in Claude:**
```
Can you get the user name for user ID "1"?
```

### Mock Data

The server includes two mock user profiles:

- **User ID "1"**: Alice, 25, Engineer
- **User ID "2"**: Bob, 30, Designer

## Troubleshooting

### MCP Server Not Showing Up

1. **Check the configuration file path:** Ensure you edited the correct `claude_desktop_config.json` file
2. **Verify Python path:** Make sure the Python executable path in the config is correct
3. **Verify script path:** Ensure the path to `data.py` is correct and uses absolute paths
4. **Check Python version:** Ensure you're using Python 3.9 or higher
5. **Restart Claude Desktop:** Completely quit and restart the application

### Tool Not Working

1. **Check dependencies:** Ensure `fastmcp` is installed: `pip install fastmcp`
2. **Test the script manually:**
   ```bash
   python mcp/data.py --transport stdio
   ```
3. **Check logs:** Look for error messages in Claude Desktop's developer console (if available)

### Windows Path Issues

On Windows, ensure you're using:
- Double backslashes (`\\`) in JSON configuration
- Full absolute paths (e.g., `C:\\Users\\YourName\\...`)

## Development

### Running Locally

To test the MCP server without Claude Desktop:

```bash
python mcp/data.py --transport stdio
```

### Adding New Tools

To add new tools to the MCP server, edit `mcp/data.py` and add new functions decorated with `@app.tool()`:

```python
@app.tool()
def your_new_tool(param: str):
    """Description of what your tool does"""
    # Your implementation here
    return result
```

### Modifying Mock Data

Edit the `mock_profiles` dictionary in `data.py` to add or modify user profiles:

```python
mock_profiles = {
    "1": {"name": "Alice", "age": 25, "role": "Engineer"},
    "2": {"name": "Bob", "age": 30, "role": "Designer"},
    "3": {"name": "Charlie", "age": 35, "role": "Manager"},  # New entry
}
```

## Technical Details

- **Framework:** FastMCP
- **Transport:** stdio (Standard Input/Output)
- **Protocol:** Model Context Protocol (MCP)
- **Language:** Python 3.x

## Resources

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP GitHub Repository](https://github.com/jlowin/fastmcp)
- [Claude Desktop Documentation](https://claude.ai/desktop)

## License

This project is provided as-is for demonstration purposes.

## Support

For issues related to:
- **MCP protocol:** Check the official MCP documentation
- **FastMCP:** Visit the FastMCP GitHub repository
- **Claude Desktop:** Contact Anthropic support

