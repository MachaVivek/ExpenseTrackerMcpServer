import os
from dotenv import load_dotenv

from jose import jwt, JWTError
from fastapi import HTTPException

from app.database.prisma import db

load_dotenv()
# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")


async def verify_mcp_token(token: str):
    # Verify JWT token for MCP requests.
    try:
        # Decode JWT token using secret key
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        # Extract user_id from token payload
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        # Find user in database using id
        user = await db.user.find_unique(
            where={
                "id": user_id
            }
        )
        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )
        # Return authenticated user
        return user
    # Triggered when token is invalid or expired or malformed
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

