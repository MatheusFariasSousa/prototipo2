from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = "sqlite:///banco.db"

engine = create_engine(DB_URL)

session = sessionmaker(bind=engine)



        

