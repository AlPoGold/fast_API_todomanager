import uvicorn
from fastapi import FastAPI
from app.database import database
from app.routers import tasks
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    await database.connect()
    yield
    # Shutdown logic
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(tasks.router)

# # Connect to the database on startup
# @app.on_event("startup")
# async def startup():
#     await database.connect()
#
# # Disconnect from the database on shutdown
# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# Include the tasks router
# app.include_router(tasks.router, prefix="/api", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Welcome to the Task Manager API"}

if __name__=="__main__":
    uvicorn.run("app.main:app", reload=True)