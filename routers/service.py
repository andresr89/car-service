from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.ServiceServices import ServiceServices
from schemas.user import ServiceRequest


service_router = APIRouter()

@service_router.get('/services', tags=['service'], response_model=List[ServiceRequest], status_code=201)
def get_services() -> List[ServiceRequest]:
     db = Session()
     result = ServiceServices(db).get_services()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@service_router.get ('/service/{id}', tags=['service'], response_model= ServiceRequest)
def get_service (id:int =Path(ge=1, le=2000)) -> ServiceRequest:
    db = Session()
    result = ServiceRequest(db).get_service(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@service_router.post('/service/', tags=['service'], response_model=dict, status_code=201)
def create_service(service_request: ServiceRequest) -> dict:
    db = Session()
    ServiceServices(db).create_service(service_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el tipo de servicio"})


@service_router.put('/service/{service_id}', tags=['service'], response_model=dict, status_code=200)
def update_service(service_id: int, service_request: ServiceRequest) -> dict:
    db = Session()
    service_service = ServiceServices(db)

    service_service.updatupdate_service_spare_model(service_id, service_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado el tipo de servicio"})

@service_router.delete('/service/{service_id}', tags=['service'], response_model=dict, status_code=200)
def delete_service(service_id: int) -> dict:
    db = Session()
    service_service = ServiceServices(db)
    service_service.delete_service(service_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado tipo de servicio"})

