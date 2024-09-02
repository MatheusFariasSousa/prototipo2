from fastapi import HTTPException,status

from sqlalchemy.orm import Session

from db.model import Notes

from schema.notes_schema import Note_Schema


class Notes_Use_Case:
    def __init__(self,db_session:Session):
        self.db_session = db_session


    def post_not(self,notes:Note_Schema):
        notation = Notes(notes.title,notes.text)
        self.db_session.add(notation)
        try:
            self.db_session.commit()
        except:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        
        
        
