from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from databse import create_tables, delete_tables
from router import router as task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Очищена")
    await create_tables()
    print("Готово")
    yield
    print("Выключение")

 
app = FastAPI(lifespan=lifespan)
app.include_router(task_router)



if __name__ == "__main__":  
    uvicorn.run("main:app", reload=True)
