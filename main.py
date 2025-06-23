

import asyncio
import logging
import os

from fastmcp import FastMCP 

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

mcp = FastMCP("MCP Server on Cloud Run")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The sum of the two numbers.
    """
    logger.info(f">>> Tool: 'add' called with numbers '{a}' and '{b}'")
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Use this to subtract two numbers.
    
    Args:
        a: The first number.
        b: The second number.
    
    Returns:
        The difference of the two numbers.
    """
    logger.info(f">>> Tool: 'subtract' called with numbers '{a}' and '{b}'")
    return a - b

@mcp.tool()
def greet(name: str) -> str:
    return f"Good morning {name}. Have a nice day"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # ✅ ensure it's an int
    logger.info(f"✅ MCP server starting on 0.0.0.0:{port}")
    # Could also use 'sse' transport, host="0.0.0.0" required for Cloud Run.
    asyncio.run(
        mcp.run_async(
            transport="streamable-http", 
            host="0.0.0.0", 
            port=port,
        )
    )

