from fastapi import FastAPI
from database import engine,Base
from models import task_model

from routes.task_router import task_router

app = FastAPI()
app.include_router(task_router)

Base.metadata.create_all(bind = engine)


@app.get("/")
def root():
    return {"message":"HR management system running"}