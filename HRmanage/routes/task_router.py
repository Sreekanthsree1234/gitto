from fastapi  import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from service.task_service import TaskService
from schemas.task_schema import Taskcreate,Taskresponse


task_router = APIRouter(prefix="/tasks",tags=["Tasks"])
@task_router.post("/create",response_model = Taskresponse)
def create_task(
    task_data:Taskcreate,
    db:Session = Depends(get_db),
    # current_user = Depends(get_current_user)
    ):
    print("✅ Router Hit")
    return TaskService .create_task(
        db = db,
        task_data = task_data,
        # current_user = current_user
    )