from fastapi import APIRouter,Form,Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from db.deps import get_conection
from schema.user_schema import User_schema,User_Schema_Output
from use_case.user_use_cases import User_use_cases

front_router = APIRouter(prefix="/front")



templates = Jinja2Templates(directory="templates")


@front_router.get("/")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="index.html")

@front_router.post("/result-form",response_model=User_Schema_Output)
def post_front(fname:str=Form(...),cpf:str= Form(...),password:str= Form(...),db_session:Session = Depends(get_conection)):
    person = User_schema(name=fname,cpf=cpf,password=password)
    uc = User_use_cases(db_session=db_session)
    uc.post_user(person)
    return person

@front_router.get("/notes")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="oi.html")
    
