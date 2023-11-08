from fastapi import FastAPI

from src.common_utils.logging import get_app_logger
from src.routes import user_router, org_router
from src.config import settings

logger = get_app_logger()


def get_app() -> FastAPI:
    fastapi_app: FastAPI = FastAPI(title="Paysense FastAPI BoilerPlate")
    fastapi_app.router.redirect_slashes = False
    fastapi_app.router.prefix = settings.service_base_prefix
    fastapi_app.include_router(prefix="/users", router=user_router.router)
    fastapi_app.include_router(prefix="/orgs", router=org_router.router)

    @fastapi_app.get(path="/ping")
    def health():
        logger.info("Logger Test")
        return "pong from here"

    return fastapi_app
