from fastmcp import FastMCP
import random
import json


mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers.
    Args:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The sum of a and b numbers.
    
    """
    return a + b


@mcp.tool
def random_number(min_value: int=1, max_value: int=100) -> int:
    """Generate a random number between min_value and max_value.
    Args:
    min_value : Minimum value default is 1.
    max_value : Maximum value default is 100.
    Returns:
    int: A random integer between min_value and max_value.
    
    """
    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info()->str:
    """Get information about the server."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A simple server that provides basic calculator functions and random number generation.",
        "tools": ["add", "random_number"],
        "author": "Haseeb"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)