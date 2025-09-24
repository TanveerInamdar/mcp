import argparse

from fastmcp import FastMCP

app = FastMCP("MockMCP1")
mock_profiles = {
        "1": {"name": "Alice", "age": 25, "role": "Engineer"},
        "2": {"name": "Bob", "age": 30, "role": "Designer"},
    }

