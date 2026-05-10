from pydantic import BaseModel
from typing import Optional

class RegisterSchema(BaseModel):
    username: str
    email: str
    password: str
    fullName: Optional[str] = None

class LoginSchema(BaseModel):
    email: str
    password: str