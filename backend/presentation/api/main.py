from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from presentation.api.routes.main import api_router
from application.dependency_container import get_settings

# IGNORE: strict pylance type checking on Pydantic Settings due to Pylance bug
# https://github.com/pydantic/pydantic/pull/3972
settings = get_settings()  # type: ignore
app_settings = settings.get_app_settings()

app = FastAPI(title=app_settings["title"], version=app_settings["version"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=app_settings['origins'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=app_settings["prefix"])
