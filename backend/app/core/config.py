import secrets
from typing import Optional

from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    API_STR: str = "/api"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SERVER_HOST: AnyHttpUrl = None
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    PROJECT_NAME: str = None

    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None

    EMAIL_TEMPLATES_DIR: str = "/backend/app/email-templates/build"

    class Config:
        case_sensitive = True


settings = Settings()
