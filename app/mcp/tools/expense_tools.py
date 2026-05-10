from app.mcp.server import mcp

@mcp.tool()
async def hello_expense_tool():
    return {
        "message": "Expense MCP tool working"
    }