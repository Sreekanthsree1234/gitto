from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from repository.task_repository import TaskRepsitory
from schemas.task_schema import Taskcreate
from database import get_db

class TaskService:
    @staticmethod
    def create_task(db:Session,task_data:Taskcreate):
        print("✅ Service Hit")
        return TaskRepsitory.create_task(
            db = db,
            task_data = task_data
           )
   
    