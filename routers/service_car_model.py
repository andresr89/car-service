from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.ServiceCarModelServices import ServiceCarModelServices
from schemas.user import ServiceCarModelRequest


service_car_model_router = APIRouter()

@service_car_model_router.get('/service-car-model', tags=['service-car-model'], response_model=List[ServiceCarModelRequest], status_code=201)
def get_service_car_models() -> List[ServiceCarModelRequest]:
     db = Session()
     result = ServiceCarModelServices(db).get_service_car_models()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@service_car_model_router.get ('/service-car-model/{id}', tags=['service-car-model'], response_model= ServiceCarModelRequest)
def get_service_car_model (id:int =Path(ge=1, le=2000)) -> ServiceCarModelRequest:
    db = Session()
    result = ServiceCarModelServices(db).get_service_car_model(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@service_car_model_router.post('/service-car-model', tags=['service-car-model'], response_model=dict, status_code=201)
def create_service_car_model(car_model_request: ServiceCarModelRequest) -> dict:
    db = Session()
    ServiceCarModelServices(db).create_service_car_model(car_model_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el selector de servicios"})


@service_car_model_router.put('/service-car-model/{model_id}', tags=['service-car-model'], response_model=dict, status_code=200)
def update_service_car_model(service_car_model_id: int, car_model_request: ServiceCarModelRequest) -> dict:
    db = Session()
    service_car_model_services = ServiceCarModelServices(db)

    service_car_model_services.update_service_car_model(service_car_model_id, car_model_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado el selector de servicios"})

@service_car_model_router.delete('/service-car-model/{model_id}', tags=['service-car-model'], response_model=dict, status_code=200)
def delete_service_car_model(service_car_model_id: int) -> dict:
    db = Session()
    service_car_model_services = ServiceCarModelServices(db)
    service_car_model_services.delete_service_car_model(service_car_model_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el selector de servicios"})

