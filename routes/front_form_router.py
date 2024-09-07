from fastapi import APIRouter,Form,Depends,status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from db.deps import get_conection
from db.model import Notes
from schema.user_schema import User_schema,User_Schema_Output
from schema.notes_schema import Note_Schema
from use_case.user_use_cases import User_use_cases
from use_case.notes_use_cases import Notes_Use_Case

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

@front_router.post("/notes")
def post_note(title:str=Form(...),note:str=Form(...),db_session:Session = Depends(get_conection)):
    notation = Note_Schema(title=title,text=note)
    uc= Notes_Use_Case(db_session=db_session)
    uc.post_not(notation)
    return RedirectResponse(url="/front/notes", status_code=status.HTTP_303_SEE_OTHER)

@front_router.get("/notes")
def read_notes(request:Request,db_session:Session = Depends(get_conection)):
    notes = db_session.query(Notes).all()
    return templates.TemplateResponse("oi.html",{"request":request,"notes":notes})

    


    
