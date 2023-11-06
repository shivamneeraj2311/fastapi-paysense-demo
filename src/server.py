from src.app import get_app
from src.config import settings
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.starlette import StarletteIntegration

if settings.sentry_dsn is not None:
    _ = sentry_sdk.init(
        dsn=settings.sentry_dsn,
        environment=settings.environment,
        integrations=[
            StarletteIntegration(),
            FastApiIntegration(),
            LoggingIntegration(event_level=None, level=None),
        ],
    )


server = get_app()