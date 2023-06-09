import functools

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field(default="Statgov info by BIN", env="PROJECT_NAME")


@functools.cache
def get_settings() -> Settings:
    return Settings()
