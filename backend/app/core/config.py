from pydantic import BaseSettings


class Settings(BaseSettings):
    API_STR: str = "/api"

    SQLALCHEMY_DATABASE_URI: str = ""

    class Config:
        case_sensitive = True


settings = Settings()
