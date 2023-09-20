from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.car_branch import car_branch_router
from routers.user import user_router



app = FastAPI()
app.title = "Car Service FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(car_branch_router)
app.include_router(user_router)



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


