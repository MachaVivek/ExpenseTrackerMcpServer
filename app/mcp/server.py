from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP(
    name="Expense Tracker MCP",
)

# Import tools AFTER creating mcp
from app.mcp.tools import expense_tools