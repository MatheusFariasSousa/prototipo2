from sqlalchemy.orm import Session
from fastapi import Depends,APIRouter,status,HTTPException
from db.model import User
from db.deps import get_conection
from schema.user_schema import User_schema,User_Schema_Output
from use_case.user_use_cases import User_use_cases

router = APIRouter(prefix="/user",tags=["User"])

@router.post("/post")
def post_user(user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    uc.post_user(user=user)
    return status.HTTP_200_OK

@router.get("/get/{id}",response_model=User_Schema_Output)
def get_by_id(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    person = uc.get_by_id(id=id)
    return person

@router.get("/get")
def get_all(db_session:Session = Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.get_all()

@router.delete("/delete/{id}")
def delete(id:int,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.delete_user(id=id)

@router.put("/put/{id}",response_model=User_Schema_Output)
def put(id:int,user:User_schema,db_session:Session=Depends(get_conection)):
    uc = User_use_cases(db_session=db_session)
    return uc.put_user(id=id,user=user)


