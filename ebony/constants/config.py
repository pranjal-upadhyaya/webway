from pydantic_settings import BaseSettings
from typing import Optional


class AppConfig(BaseSettings):
    app_port: int
    app_host: str

    app_env: str

    db_host: Optional[str] = None
    db_port: Optional[int] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    db_name: Optional[str] = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


app_config = AppConfig()