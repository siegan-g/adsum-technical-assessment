from pydantic_settings import BaseSettings, SettingsConfigDict,PydanticBaseSettingsSource,TomlConfigSettingsSource
from pydantic import BaseModel
from typing import Any


class AppSettings(BaseModel):
    title: str = "OpenTax Backend API"
    version: str = "1.0"
    debug: bool = True
    prefix: str = "/api"
    max_limit: int = 100
    sink:str = "database"


class DatabaseSettings(BaseModel):
    protocol: str = "postgresql"
    database: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database:DatabaseSettings  = DatabaseSettings()
    model_config = SettingsConfigDict(toml_file="config.toml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


    def get_db_settings(self)->dict[str,Any]:
        settings = self.model_dump()['database']
        settings['url'] = f"{settings['protocol']}://{settings['user']}:{settings['password']}@{settings['host']}:{settings['port']}/{settings['database']}"
        return settings
    
    def get_app_settings(self)->dict[str,Any]:
        return self.model_dump()['app']
        
