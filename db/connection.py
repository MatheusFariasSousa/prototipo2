from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = "postgresql+psycopg://postgres:adminpass@127.0.0.1:5432/testando_db"

engine = create_engine(DB_URL)

session = sessionmaker(bind=engine)



        

