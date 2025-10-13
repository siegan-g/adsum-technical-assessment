from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from typing import Any


class AppSettings(BaseModel):
    title: str = "OpenTax Backend API"
    version: str = "1.0"
    debug: bool = True
    prefix:str = "/api"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    model_config = SettingsConfigDict(toml_file="config.toml")

    def get_settings(self)->dict[str,Any]:
        return self.model_dump()
