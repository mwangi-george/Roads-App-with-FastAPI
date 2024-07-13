from fastapi import FastAPI
from app.routes import create_home_router, create_road_router, create_location_router
from fastapi.staticfiles import StaticFiles


def create_app() -> FastAPI:

    app = FastAPI(
        title="A Backend infrastructure for Road Networks in Kenya",
        description="Provides API endpoint for performing CRUD operations on the Roads Database"
    )

    app.mount(path="/static",
              app=StaticFiles(directory="static"), name="static")

    home_router = create_home_router()
    road_router = create_road_router()
    loction_router = create_location_router()

    app.include_router(road_router)
    app.include_router(loction_router)
    app.include_router(home_router)
    return app


app = create_app()
