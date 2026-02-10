from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Task
from dependencies import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/tasks")
def create_task(
    title: str,
    description: str,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    task = Task(
        title=title,
        description=description,
        user_id=user_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return {"message": "Task created"}


@router.get("/tasks")
def get_tasks(
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Task).filter(Task.user_id == user_id).all()
