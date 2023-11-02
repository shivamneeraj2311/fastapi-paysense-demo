from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.apps.org_service import orgs

def get_app() -> FastAPI:
    api_app: FastAPI = FastAPI(title="Org Service Router")
    api_app.router.redirect_slashes = False
    api_app.include_router(
        prefix="/base", router=orgs.router, tags=["Orgs Base"]
    )
    api_app.add_middleware(
        CORSMiddleware,
        allow_origin_regex=".*",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["X-Request-ID"],
    )

    @api_app.get(path="/ping")
    def health():
        return "pong"

    return api_app