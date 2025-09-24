import argparse

from fastmcp import FastMCP

app = FastMCP("MockMCP2")
mock_profiles = {
        "1": {"name": "Alice", "age": 25, "role": "Engineer"},
        "2": {"name": "Bob", "age": 30, "role": "Designer"},
    }

@app.tool()
def get_user_name(user_id: str):
    "Give the user ID to get the name of the person. Pass the ID as a string like 1 or 2"
    x = mock_profiles.get(user_id)
    return x["name"]
def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    args = parser.parse_args()

    # Use None for stdio (Claude), or pass transport for Ollama
    app.run(transport=None if args.transport == "stdio" else args.transport)

if __name__ == "__main__":
    main()

