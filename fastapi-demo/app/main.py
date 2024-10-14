import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response, HTMLResponse, StreamingResponse
from starlette.staticfiles import StaticFiles

app = FastAPI(
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Optional: Middleware for Loguru logging
class LoguruMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)
        logger.info(f"Response: {response.status_code}")
        return response


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request received: {request.method} {request.url.path}")
    response: Response = await call_next(request)
    logger.info(f"Response sent: {response.status_code}")
    return response


@logger.catch
@app.get("/")
async def redirect_to_swagger(request: Request) -> Response:
    return RedirectResponse(url="/docs")
