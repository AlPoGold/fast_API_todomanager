from pydantic import BaseModel

# Base Schema (shared fields)
class TaskBase(BaseModel):
    id: int
    title: str
    description: str = None
    completed: bool = False




# Create Schema (inherits from TaskBase)
class TaskCreate(TaskBase):
    pass


# Read Schema (inherits from TaskBase)
class Task(TaskBase):
    id: int  # Include ID when returning data

    # Configuration to support ORM models
    class Config:
        orm_mode = True
