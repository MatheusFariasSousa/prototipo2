from datetime import datetime,timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from db.deps import get_conection
from schema.token_schema import TokenData
from zoneinfo import ZoneInfo
from db.model import User
from jwt import encode, decode
from jwt.exceptions import DecodeError   


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/token")



SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encode_jwt = encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def get_current_user(db_session:Session = Depends(get_conection),token:str = Depends(oauth2_scheme)):
    try:
        payload = decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        token_data = TokenData(username=username)
    except DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    
    user = db_session.query(User).where(User.name==token_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    return user
    



    
                     