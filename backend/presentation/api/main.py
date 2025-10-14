from fastapi import FastAPI
from routes.main import api_router
from application.settings import Settings
import uvicorn
from application.logging.loguru_logger import LoguruLogger 
from application.logging.db_sink import database_sink

# IGNORE: strict pylance type checking on Pydantic Settings due to Pylance bug
# https://github.com/pydantic/pydantic/pull/3972
settings = Settings() # type: ignore
app_settings = settings.get_app_settings()
database_settings = settings.get_db_settings()

app = FastAPI(title=app_settings["title"],version=app_settings["version"])

logger = LoguruLogger(app_settings)

app.include_router(api_router,prefix=app_settings["prefix"])

if __name__ == "__main__":
    uvicorn.run("presentation.api.main:app",host=app_settings["host"],port=app_settings["port"])


