from fastapi import FastAPI

from src.config import get_settings
from src.router import router

settings = get_settings()


def setup_app():
    app = FastAPI(
        title=settings.app_name,
    )
    app.include_router(router)
    return app
