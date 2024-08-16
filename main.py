from fastapi import FastAPI
from routes.user_routes import router

app = FastAPI()

@app.get("/")
def get_user():
    return "teste"

app.include_router(router=router)