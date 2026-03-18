from fastapi import FastAPI
from typing import Dict, List

app = FastAPI(title="My Service")

@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok"}

@app.get("/items")
def get_items() -> List[Dict[str, str | int]]:
    return [
        {"id": 1, "name": "Item A", "description": "This is item A"},
        {"id": 2, "name": "Item B", "description": "This is item B"},
    ]

@app.get("/")
def read_root():
    return {"message": "Welcome to My Service"}
