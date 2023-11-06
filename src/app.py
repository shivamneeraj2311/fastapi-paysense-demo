from fastapi import FastAPI

from src.common_utils.logging import get_app_logger
from src.apps import user_router, org_router
logger = get_app_logger()
def get_app() -> FastAPI:
    fastapi_app: FastAPI = FastAPI(title="Paysense FastAPI BoilerPlate")
    fastapi_app.router.redirect_slashes = False
    fastapi_app.mount(path="/users", app=user_router.get_app())
    fastapi_app.mount(path="/orgs", app=org_router.get_app())
    @fastapi_app.get(path="/ping")
    def health():
        logger.info("Test")
        return "pong from here"

    return fastapi_app