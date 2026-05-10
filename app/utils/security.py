from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()
# JWT configuration
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

# Password hashing configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# hash password before storing it in db
def hash_password(password: str):
    return pwd_context.hash(password)


# verify whether the entered password is matches with the password hash present in db
def verify_password( plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict):
    to_encode = data.copy() # it creates a new dict copied from data
    expire = datetime.now(timezone.utc) + timedelta(days=7) # 7 days expiry
    to_encode.update({
        "exp": expire
    })
    # encode the data using jwt
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

