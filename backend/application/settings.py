from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from typing import Any


class AppSettings(BaseModel):
    title: str = "OpenTax Backend API"
    version: str = "1.0"
    debug: bool = True
    prefix: str = "/api"
    host: str = "0.0.0.0"
    port: int = 8000


class DatabaseSettings(BaseModel):
    database: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database:DatabaseSettings  = DatabaseSettings()
    model_config = SettingsConfigDict(toml_file="application/config.toml")

    def get_db_settings(self)->dict[str,Any]:
        settings = self.model_dump()['database']
        settings['url'] = f"{settings['database']}://{settings['user']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
        return settings
        