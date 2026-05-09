from fastmcp import FastMCP
import math

mcp = FastMCP("Calculator MCP")

@mcp.tool()
def add(a: float, b: float):
    return {
        "operation": "addition",
        "result": a + b
    }

@mcp.tool()
def subtract(a: float, b: float):
    return {
        "operation": "subtraction",
        "result": a - b
    }

@mcp.tool()
def multiply(a: float, b: float):
    return {
        "operation": "multiplication",
        "result": a * b
    }

@mcp.tool()
def divide(a: float, b: float):
    if b == 0:
        return {
            "error": "Division by zero is not allowed"
        }
    return {
        "operation": "division",
        "result": a / b
    }

@mcp.tool()
def power(base: float, exponent: float):
    return {
        "operation": "power",
        "result": base ** exponent
    }

@mcp.tool()
def square_root(number: float):
    if number < 0:
        return {
            "error": "Negative numbers are not allowed"
        }
    return {
        "operation": "square_root",
        "result": math.sqrt(number)
    }

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=8000
    )

