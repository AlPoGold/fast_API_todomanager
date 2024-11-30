from fastapi import APIRouter, HTTPException
from app import schemas, crud

router = APIRouter()

@router.get("/tasks/", response_model=list[schemas.Task])
async def read_tasks():
    return await crud.get_tasks()

@router.get("/tasks/{task_id}", response_model=schemas.Task)
async def read_task(task_id: int):
    task = await crud.get_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/tasks/", response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate):
    return await crud.create_task(task)

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = await crud.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
