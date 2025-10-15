from fastapi import FastAPI
from routes.main import api_router
from application.dependency_container import get_settings,get_seeder_service

import uvicorn

# IGNORE: strict pylance type checking on Pydantic Settings due to Pylance bug
# https://github.com/pydantic/pydantic/pull/3972
settings = get_settings() # type: ignore
app_settings = settings.get_app_settings()

app = FastAPI(title=app_settings["title"], version=app_settings["version"])
app.include_router(api_router, prefix=app_settings["prefix"])

if __name__ == "__main__":
    # get_seeder_service().seed(num_invoices=30,num_payments=30)
    uvicorn.run("presentation.api.main:app", host=app_settings["host"], port=app_settings["port"])


