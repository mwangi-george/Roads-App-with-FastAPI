from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


def create_home_router() -> APIRouter:
    home_router = APIRouter()

    templates = Jinja2Templates(directory="templates")

    @home_router.get("/", response_class=HTMLResponse)
    def home(request: Request):
        return templates.TemplateResponse(request=request, name="index.html")

    return home_router
