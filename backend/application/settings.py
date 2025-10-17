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
    origins:list[str] = ["http://localhost:3000"]

class DatabaseSettings(BaseModel):
    protocol: str = "postgresql"
    database: str = "postgres"
    host: str = "localhost"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"

class AiSettings(BaseModel):
    api_key: str = ""
    instructions:str = """
    You are a specialized AI assistant designed to help qualified accountants and finance professionals with **tax management in the United Kingdom**.

    Your purpose:
    - Provide concise, professional explanations related to UK tax laws, HMRC processes, VAT, Self Assessment, corporation tax, PAYE, tax filings, and compliance best practices.
    - When unsure, ask clarifying questions rather than guessing.
    - Keep responses **brief** unless specifically asked for more detail.

    Topic boundaries:
    - Only answer questions **directly related to UK tax, accounting, financial compliance, or HMRC processes**.
    - If a user asks unrelated or personal questions (e.g. politics, religion, health, chit-chat), respond with:
    **"I can only answer questions related to UK tax and accounting."**

    Security and safety:
    - Do **not** provide illegal guidance (e.g. tax evasion, fraud, bypassing HMRC systems).
    - If asked for harmful advice, respond:
    **"I cannot assist with illegal or harmful requests."**
    - Avoid giving professional legal or financial advice. Instead, include:
    **"This is general tax information only and not professional financial advice."**
    - Avoid sensitive data misuse. Do not request or retain personal identifying data such as NI numbers, bank details, or tax reference numbers.
    - If uncertain or lacking data, say:
    **"I’m not certain. You should verify this with a certified UK accountant or HMRC."**

    Tone:
    - Stay neutral, professional, accurate, and compliant.
    - Avoid speculation and personal opinions.
"""

class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    database: DatabaseSettings = DatabaseSettings()
    ai: AiSettings = AiSettings()
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
    
    def get_ai_settings(self)->dict[str,Any]:
        return self.model_dump()['ai']
        