import os
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
from jose import jwt, JWTError
# prisma client instance
from app.database.prisma import db


load_dotenv()
# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

# HTTPBearer automatically extracts token from: Authorization: Bearer <token>
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    # Extract raw JWT token
    token = credentials.credentials
    try:
        # Decode JWT token
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        # Extract user_id from token payload
        user_id = payload.get("user_id")
        if not user_id:
            # If token does not contain user_id then return invalid token
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        # Find user in database
        user = await db.user.find_unique(
            where={
                "id": user_id
            }
        )
        if not user:
            # if user not present in the db then throw exception
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )
        return user
    # Triggered when token is invalid, expired, or malformed
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

