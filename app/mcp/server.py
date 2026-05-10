# below three lines are deploy fix
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastmcp import FastMCP

# Create MCP server instance
mcp = FastMCP(
    name="Expense Tracker MCP",
)

# Import tools AFTER creating mcp
from app.mcp.tools import expense_tools