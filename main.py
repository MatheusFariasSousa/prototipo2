from fastapi import FastAPI
from routes.user_routes import router
from routes.front_form_router import front_router
from routes.notes_router import note_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()



@app.get("/")
def get_user():
    return "teste"

app.include_router(router=router)
app.include_router(router=front_router)
app.include_router(router=note_router)

app.mount("/static",StaticFiles(directory="static"),name="static")

