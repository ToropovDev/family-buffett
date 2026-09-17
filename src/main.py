from typing import Any

from fastapi import FastAPI
from sqlalchemy import text
from starlette.middleware.exceptions import ExceptionMiddleware

from src.infra.db.base import db_session
from src.schemas import OK

app = FastAPI(prefix="/api")

app.add_middleware(ExceptionMiddleware)


@app.get("/echo")
async def echo(message: str) -> dict[str, Any]:
    return {"message": message}


@app.get("/db/ready")
async def ready() -> OK:
    async with db_session() as session:
        await session.execute(text("SELECT 1"))

        return OK()
