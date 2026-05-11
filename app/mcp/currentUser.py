from fastapi import HTTPException
from fastmcp import Context

from app.mcp.auth import get_user_from_token

# Authenticate current MCP user using Authorization metadata.
async def get_current_mcp_user(
    ctx: Context
):
    # Read Authorization header
    request = ctx.request_context.request
    auth_header = request.headers.get("Authorization")

    # Check token existence
    if not auth_header:
        raise HTTPException(
            status_code=401,
            detail="Missing token"
        )

    # Extract JWT token
    token = auth_header.replace(
        "Bearer ",
        ""
    )

    # Verify JWT and return user
    return await get_user_from_token(
        token
    )

