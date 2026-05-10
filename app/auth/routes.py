from fastapi import APIRouter, HTTPException
from prisma.errors import UniqueViolationError

# prisma client instance
from database.prisma import db

# validation schemas
from auth.schemas import (
    RegisterSchema,
    LoginSchema
)

from utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

# seperate router for the autentication routes
router = APIRouter(
    prefix="/auth",
    tags=["Auth"] # group name in swagger
)

@router.post("/register")
async def register(data: RegisterSchema):
    # hash the password
    hashed_password = hash_password(data.password)
    try:
        user = await db.user.create(
            data={
                "username": data.username,
                "email": data.email,
                "password": hashed_password,
                "fullName": data.fullName
            }
        )
        return {
            "message": "User created successfully",
            "user_id": user.id
        }
    # trigged when the unique contraints are failed like unique username, unique email etc
    except UniqueViolationError:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )



@router.post("/login")
async def login(data: LoginSchema):
    # check whether the user exists in db
    user = await db.user.find_unique(
        where={
            "email": data.email
        }
    )
    if not user:
        # if user not exists throw excepton
        raise HTTPException(
            status_code=401,
            detail="User not exists"
        )

    # check whether the entered password is valid
    is_valid = verify_password(
        data.password,
        user.password
    )
    if not is_valid:
        # if password is not correct
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    # Generate JWT access token
    token = create_access_token({
        "user_id": user.id
    })
    # return access token
    return {
        "access_token": token
    }
