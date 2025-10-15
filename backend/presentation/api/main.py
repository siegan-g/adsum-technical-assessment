from fastapi import FastAPI
from presentation.api.routes.main import api_router
from application.dependency_container import get_settings

# IGNORE: strict pylance type checking on Pydantic Settings due to Pylance bug
# https://github.com/pydantic/pydantic/pull/3972
settings = get_settings()  # type: ignore
app_settings = settings.get_app_settings()

app = FastAPI(title=app_settings["title"], version=app_settings["version"])
app.include_router(api_router, prefix=app_settings["prefix"])
