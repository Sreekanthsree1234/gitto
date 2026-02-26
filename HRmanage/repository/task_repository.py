from sqlalchemy.orm import Session
from models.task_model import Task
from schemas.task_schema import Taskcreate

class TaskRepsitory:
    @staticmethod
    def create_task(db:Session,task_data:Taskcreate):
        print("✅ Repository Hit")
        task = Task(
            title = task_data.title,
            description = task_data.description,
            assigned_to = task_data.assigned_to,
            assigned_by = task_data.assigned_by,
            deadline = task_data.deadline

        )
        db.add(task)
        print("✅ Before Commit")
        db.commit()
        print("✅ After Commit")
        db.refresh(task)
        return task