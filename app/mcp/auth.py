import os
from dotenv import load_dotenv

from jose import jwt, JWTError
from fastapi import HTTPException

from database.prisma import db

load_dotenv()
# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")


async def get_user_from_token(token: str):
    try:
        # Decode JWT token using secret key
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        # Extract user_id from JWT payload
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
    # Triggered when token is invalid, expired or malformed
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )




