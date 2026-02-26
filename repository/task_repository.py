from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import Taskcreate

class TaskRepsitory:
    @staticmethod
    def create_task(db:Session,task_data:Taskcreate,manager_id:int):
        task = Task(
            title = task_data.title,
            description = task_data.description,
            assigned_to = task_data.assigned_to,
            assigned_by = manager_id,
            deadline = task_data.deadline

        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task