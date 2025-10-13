from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel


class AppSettings(BaseModel):
    title: str = "OpenTax Backend API"
    version: str = "1.0"
    debug: bool = True
    prefix: str = "/api"
    host: str = "0.0.0.0"
    port: int = 8000


class DatabaseSettings(BaseModel):
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database:DatabaseSettings  = DatabaseSettings()
    model_config = SettingsConfigDict(toml_file="application/config.toml")
