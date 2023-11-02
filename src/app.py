from fastapi import FastAPI
from src.apps import user_router, org_router

def get_app() -> FastAPI:
    fastapi_app: FastAPI = FastAPI(title="Paysense FastAPI BoilerPlate")
    fastapi_app.router.redirect_slashes = False
    fastapi_app.mount(path="/users", app=user_router.get_app())
    fastapi_app.mount(path="/orgs", app=org_router.get_app())
    @fastapi_app.get(path="/ping")
    def health():
        return "pong from here"

    return fastapi_app