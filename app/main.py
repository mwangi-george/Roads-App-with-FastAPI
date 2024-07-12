from fastapi import FastAPI
from app.routes.road import create_road_router
from app.routes.locations import create_location_router


def create_app() -> FastAPI:

    app = FastAPI(
        title="A Backend infrastructure for Road Networks in Kenya",
        description="Provides API endpoint for performing CRUD operations on the Roads Database"
    )

    road_router = create_road_router()
    loction_router = create_location_router()

    app.include_router(road_router)
    app.include_router(loction_router)
    return app


app = create_app()
