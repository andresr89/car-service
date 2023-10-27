from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.SpareModelServices import SpareModelServices
from schemas.user import SpareModelRequest


spare_model_router = APIRouter()

@spare_model_router.get('/spare-models/', tags=['spare-model'], response_model=List[SpareModelRequest], status_code=201)
def get_spare_models() -> List[SpareModelRequest]:
     db = Session()
     result = SpareModelServices(db).get_spare_models()
     return JSONResponse(status_code=200, content=jsonable_encoder(result))

@spare_model_router.get ('/spare-model/{id}', tags=['spare-model'], response_model= SpareModelRequest)
def get_spare_model (id:int =Path(ge=1, le=2000)) -> SpareModelRequest:
    db = Session()
    result = SpareModelServices(db).get_spare_model(id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@spare_model_router.get ('/spare-model/by-spare-service_id/{spare_service_id}',tags=['spare-model'], response_model= SpareModelRequest)
def get_spare_model_by_spare_service_id (spare_service_id : int =Path(ge=1, le=2000)) -> SpareModelRequest:
    db = Session()
    result = SpareModelServices(db).get_spare_model_by_spare_service_id(spare_service_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))    
                         
                         

@spare_model_router.post('/spare-model', tags=['spare-model'], response_model=dict, status_code=201)
def create_spare_model(spare_model_request: SpareModelRequest) -> dict:
    db = Session()
    SpareModelServices(db).create_spare_model(spare_model_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el modelo de articulo de recambio"})


@spare_model_router.put('/spare-model/{model_id}', tags=['spare-model'], response_model=dict, status_code=200)
def update_spare_model(model_id: int, spare_model_request: SpareModelRequest) -> dict:
    db = Session()
    spare_model_services = SpareModelServices(db)

    spare_model_services.update_spare_model(model_id, spare_model_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado el modelo de articulo de recambio"})

@spare_model_router.delete('/spare-model/{model_id}', tags=['spare-model'], response_model=dict, status_code=200)
def delete_spare_model(model_id: int) -> dict:
    db = Session()
    spare_model_services = SpareModelServices(db)
    spare_model_services.delete_spare_model(model_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el modelo de articulo de recambio"})

