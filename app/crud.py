from app import schemas
from app.database import database

async def get_tasks():
    query = "SELECT * FROM tasks"
    return await database.fetch_all(query)

async def get_task(task_id: int):
    query = "SELECT * FROM tasks WHERE id = :id"
    return await database.fetch_one(query, {"id": task_id})

async def create_task(task: schemas.TaskCreate):
    query = """
    INSERT INTO tasks (id, title, description, completed)
    VALUES (:id, :title, :description, :completed)
    RETURNING id, title, description, completed
    """
    values = task.dict()
    return await database.fetch_one(query, values)

async def delete_task(task_id: int):
    query = "DELETE FROM tasks WHERE id = :id"
    return await database.execute(query, {"id": task_id})
