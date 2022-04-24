from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api_v1"

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./sql_app.db"

    class Config:
        case_sensitive = True


settings = Settings()
