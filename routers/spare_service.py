from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.SpareServiceServices import SpareServiceServices
from schemas.user import SpareServiceRequest


spare_service_router = APIRouter()

@spare_service_router.get('/spare-service', tags=['spare-service'], response_model=List[SpareServiceRequest], status_code=201)
def get_spares_service() -> List[SpareServiceRequest]:
     db = Session()
     result = SpareServiceServices(db).get_spares_service()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@spare_service_router.get ('/spare-service/{id}', tags=['spare-service'], response_model= SpareServiceRequest)
def get_spare_service (id:int =Path(ge=1, le=2000)) -> SpareServiceRequest:
    db = Session()
    result = SpareServiceServices(db).get_spare_service(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@spare_service_router.post('/spare-service', tags=['spare-service'], response_model=dict, status_code=201)
def create_spare_service(SpareServiceRequest: SpareServiceRequest) -> dict:
    db = Session()
    SpareServiceServices(db) .create_spare_service(SpareServiceRequest)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el articulo de recambio"})


@spare_service_router.put('/spare-service/{model_id}', tags=['spare-service'], response_model=dict, status_code=200)
def update_spare_service(model_id: int, SpareServiceRequest: SpareServiceRequest) -> dict:
    db = Session()
    car_brand_service = SpareServiceServices(db)

    car_brand_service.update_spare_service(model_id, SpareServiceRequest)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado el articulo de recambio"})

@spare_service_router.delete('/spare-service/{model_id}', tags=['spare-service'], response_model=dict, status_code=200)
def delete_spare_service(model_id: int) -> dict:
    db = Session()
    car_brand_service = SpareServiceServices(db)
    car_brand_service.delete_spare_service(model_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el articulo de recambio"})

