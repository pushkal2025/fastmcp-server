from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """This tool returns multiplication of two numbers"""
    return a * b

@mcp.tool()
def greet(name: str) -> str:
    return f"Good morning {name}. Have a nice day"

# This is only for local development
if __name__ == "__main__":
    mcp.run(transport="streamable-http")


