from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = "postgresql+psycopg://postgres:adminpass@127.0.0.1:5432/app_db"

engine = create_engine(DB_URL,pool_pre_ping=True)

session = sessionmaker(bind=engine)



        

