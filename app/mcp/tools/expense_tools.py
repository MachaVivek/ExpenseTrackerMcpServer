from fastmcp import Context

from mcp.server import mcp
from database.prisma import db

from mcp.currentUser import (
    get_current_mcp_user
)


@mcp.tool()
async def add_transaction(
    ctx: Context,
    title: str,
    amount: float,
    category: str,
    transaction_type: str
):

    # Get authenticated MCP user
    current_user = await get_current_mcp_user(
        ctx
    )

    # Create transaction
    transaction = await db.transaction.create(
        data={
            "title": title,
            "amount": amount,
            "type": transaction_type,
            "userId": current_user.id,
            "category": category
        }
    )

    return {
        "message": "Transaction added",
        "transaction_id": transaction.id
    }

