from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.CarBrandServices import CarBrandServices
from schemas.user import CarBrandRequest

car_brand_router = APIRouter()

@car_brand_router.get('/car-brand', tags=['car-brand'], response_model=List[CarBrandRequest], status_code=201)
def get_car_brands() -> List[CarBrandRequest]:
     db = Session()
     result = CarBrandServices(db).get_car_brands()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@car_brand_router.get ('/car-brand/{id}', tags=['car-brand'], response_model= CarBrandRequest)
def get_car_brand (id:int =Path(ge=1, le=2000)) -> CarBrandRequest:
    db = Session()
    result = CarBrandRequest(db).get_car_brand(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@car_brand_router.post('/car-brand', tags=['car-brand'], response_model=dict, status_code=201)
def create_brand(car_brand_request: CarBrandRequest) -> dict:
    db = Session()
    CarBrandServices(db).create_car_brand(car_brand_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la marca de vehiculo"})


@car_brand_router.put('/car-brand/{brand_id}', tags=['car-brand'], response_model=dict, status_code=200)
def update_brand(brand_id: int, car_brand_request: CarBrandRequest) -> dict:
    db = Session()
    car_brand_service = CarBrandServices(db)

    car_brand_service.update_car_brand(brand_id, car_brand_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado la marca de vehiculo"})

@car_brand_router.delete('/car-brand/{brand_id}', tags=['car-brand'], response_model=dict, status_code=200)
def delete_movie(brand_id: int) -> dict:
    db = Session()
    car_brand_service = CarBrandServices(db)
    car_brand_service.delete_car_brand(brand_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la marca de vehiculo"})


