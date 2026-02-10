from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Task
from auth import get_current_user

router = APIRouter()

@router.post("/tasks")
def create_task(
    title: str,
    description: str,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    task = Task(
        title=title,
        description=description,
        user_id=user.id
    )
    db.add(task)
    db.commit()
    return {"message": "Task created"}

@router.get("/tasks")
def get_tasks(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return db.query(Task).filter(Task.user_id == user.id).all()

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user.id
    ).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
