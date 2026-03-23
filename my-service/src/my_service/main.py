from dotenv import load_dotenv

from fastapi import FastAPI, Request, Response
from prometheus_client import generate_latest
from typing import Dict, List
import uvicorn
from my_service.logger import logger
from my_service.metrics import request_counter
from my_service.tracing import setup_tracing

load_dotenv()

app = FastAPI(title="My Service")
setup_tracing(app)

@app.middleware("http")
async def add_logging_context(request: Request, call_next):
    extra = {
        "path": request.url.path,
        "method": request.method
    }
    
    response = await call_next(request)
    
    logger.info("request processed", extra=extra)
    return response

@app.get("/health")
def health_check(request: Request) -> Dict[str, str]:
    logger.info("health endpoint called", extra={"path": request.url.path, "method": request.method})
    request_counter.labels(path="/health").inc()
    return {"status": "ok"}

@app.get("/items")
def get_items() -> List[Dict[str, str | int]]:
    return [
        {"id": 1, "name": "Item A", "description": "This is item A"},
        {"id": 2, "name": "Item B", "description": "This is item B"},
    ]

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")

@app.get("/")
def read_root():
    return {"message": "Welcome to My Service"}


def main():
    uvicorn.run("my_service.main:app", host="0.0.0.0", port=8000)