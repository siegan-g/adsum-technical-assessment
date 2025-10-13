from fastapi import FastAPI
from routes.main import api_router
from application.settings import Settings
import uvicorn

# IGNORE: strict pylance type checking on Pydantic Settings due to Pylance bug
# https://github.com/pydantic/pydantic/pull/3972
settings = Settings() # type: ignore
app_settings = settings.model_dump()["app"]
database_settings = settings.model_dump()["database"]   
app = FastAPI(title=app_settings["title"],version=app_settings["version"])

app.include_router(api_router,prefix=app_settings["prefix"])

if __name__ == "__main__":
    uvicorn.run("presentation.api.main:app",host=app_settings["host"],port=app_settings["port"])


