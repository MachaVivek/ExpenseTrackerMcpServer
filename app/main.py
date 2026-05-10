from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.database.prisma import db
from app.auth.routes import router as auth_router

from app.auth.dependencies import get_current_user
from fastapi import Depends

from app.mcp.server import mcp

# Create MCP ASGI app
mcp_app = mcp.http_app(path="/")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # handles application setup and shutdown
    await db.connect() # connect prisma client to the database
    print("Database connected")

    # Start MCP lifespan
    async with mcp_app.lifespan(app):
        yield # app keeps running

    await db.disconnect() # safely disconnect prisma client
    print("Database disconnected")

# fastapi application instance
app = FastAPI(
    title="Expense Tracker MCP",
    lifespan=lifespan
)

app.include_router(auth_router)
app.mount("/mcp", mcp_app)

# app.mount("/mcp", mcp.http_app())

# Health check route
@app.get("/")
async def root():
    return {
        "message": "Expense Tracker MCP Running"
    }

@app.get("/me")
async def get_me(current_user = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username
    }
