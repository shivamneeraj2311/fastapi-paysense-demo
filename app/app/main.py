from fastapi import FastAPI
from app.api.api_v1.endpoints.dummy import dummy_router
from app.db.session import engine

app = FastAPI()
app.include_router(dummy_router, prefix="/dummy_user", tags=["dummy_user"])

@app.get(path="/ping")
def health():
    return "pong"