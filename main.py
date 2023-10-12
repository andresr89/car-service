from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from utils.jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.car_brand import car_brand_router
from routers.car_model import car_model_router
from routers.spare_service import spare_service_router
from routers.spare_model import spare_model_router
from routers.service import service_router
from routers.service_car_model import service_car_model_router
from routers.user import user_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.title = "Car Service FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(car_brand_router)
app.include_router(car_model_router)
app.include_router(spare_service_router)
app.include_router(spare_model_router)
app.include_router(service_router)
app.include_router(service_car_model_router)
app.include_router(user_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Reemplaza con la URL de tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


