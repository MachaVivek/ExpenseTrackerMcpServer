from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi import Depends


from app.database.prisma import db
from app.auth.routes import router as auth_router
from app.reports.routes import router as reports_router

from app.auth.dependencies import get_current_user

from app.mcp.server import mcp

# Create MCP ASGI app
mcp_app = mcp.http_app(path="/")

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    print("Database connected")
    async with mcp_app.lifespan(app):
        yield
    await db.disconnect()
    print("Database disconnected")

app = FastAPI(
    title="Expense Tracker MCP",
    lifespan=lifespan
)

app.include_router(auth_router)
app.include_router(reports_router)
app.mount("/mcp", mcp_app)

@app.get("/")
async def root():
    return {
        "message": "Expense Tracker MCP Running"
    }

@app.get("/me")
async def get_me(
    current_user = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "username": current_user.username
    }
