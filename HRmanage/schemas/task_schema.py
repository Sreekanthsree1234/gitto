from pydantic import BaseModel
from datetime import date
from enum import Enum

class TaskStatus(str,Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class Taskcreate(BaseModel):
    title:str
    description:str
    assigned_to:int
    assigned_by: int
    deadline:date

class Taskresponse(BaseModel):
    id:int
    title:str
    description:str
    assigned_to:int
    assigned_by:int
    deadline:date
    status:TaskStatus
    class Config:
        from_attributes = True

