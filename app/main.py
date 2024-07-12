from fastapi import FastAPI
from app.routes.road import create_road_router


def create_app() -> FastAPI:

    app = FastAPI()
    road_router = create_road_router()
    app.include_router(road_router)
    return app


app = create_app()
