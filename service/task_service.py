from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from repository.task_repository import TaskRepsitory
from schemas.task_schema import Taskcreate
from database import get_db

class TaskService:
    @staticmethod
    def create_task(db:Session,task_data:Taskcreate,current_user):
        if current_user.role != "MANAGER":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,detail="only managers can create tasks"
            )
        return TaskRepsitory.create_task(
            db = db,
            task_data = task_data,
            manager_id = current_user.id
            )