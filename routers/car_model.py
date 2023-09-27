from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.CarModelServices import CarModelServices
from schemas.user import CarModelRequest


car_model_router = APIRouter()

@car_model_router.get('/car-model', tags=['car-model'], response_model=List[CarModelRequest], status_code=201)
def get_car_branchs() -> List[CarModelRequest]:
     db = Session()
     result = CarModelServices(db).get_car_models()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@car_model_router.get ('/car-model/{id}', tags=['car-model'], response_model= CarModelRequest)
def get_car_model (id:int =Path(ge=1, le=2000)) -> CarModelRequest:
    db = Session()
    result = CarModelServices(db).get_car_model(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@car_model_router.post('/car-model', tags=['car-model'], response_model=dict, status_code=201)
def create_model(car_model_request: CarModelRequest) -> dict:
    db = Session()
    CarModelServices(db).create_car_model(car_model_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el modelo de vehiculo"})


@car_model_router.put('/car-model/{model_id}', tags=['car-model'], response_model=dict, status_code=200)
def update_model(model_id: int, car_model_request: CarModelRequest) -> dict:
    db = Session()
    car_model_service = CarModelServices(db)

    car_model_service.update_car_model(model_id, car_model_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado el modelo de vehiculo"})

@car_model_router.delete('/car-model/{model_id}', tags=['car-model'], response_model=dict, status_code=200)
def delete_model(model_id: int) -> dict:
    db = Session()
    car_model_service = CarModelServices(db)
    car_model_service.delete_car_model(model_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el modelo de vehiculo"})

