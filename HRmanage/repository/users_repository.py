from sqlalchemy.orm import Session
from models.users_model import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    @staticmethod
    def create_user(db:Session,user):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    @staticmethod
    def get_user_by_username(db:Session,username:str):
        return db.query(User).filter(User.username == username).first()

    @staticmethod

    def get_user_by_id(db:Session,user_id:int):
        return db.query(User).filter(User.id == user_id).first()