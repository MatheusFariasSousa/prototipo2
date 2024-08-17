from fastapi import APIRouter,Response
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


front_router = APIRouter(prefix="/front")



templates = Jinja2Templates(directory="templates")


@front_router.get("/")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")
