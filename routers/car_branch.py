from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.CarBranchServices import CarBranchServices
from schemas.user import CarBranchRequest

car_branch_router = APIRouter()


@car_branch_router.post('/car-branch', tags=['car-branch'], response_model=dict, status_code=201)
def create_branch(car_branch_request: CarBranchRequest) -> dict:
    db = Session()
    CarBranchServices(db).create_car_branch(car_branch_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la marca de vehiculo"})


@car_branch_router.put('/car-branch/{branch_id}', tags=['car-branch'], response_model=dict, status_code=200)
def update_branch(branch_id: int, car_branch_request: CarBranchRequest) -> dict:
    db = Session()
    car_branch_service = CarBranchServices(db)

    car_branch_service.update_car_branch(branch_id, car_branch_request)
    
    return JSONResponse(status_code=201, content={"message": "Se ha modificado la marca de vehiculo"})

@car_branch_router.delete('/car-branch/{branch_id}', tags=['car-branch'], response_model=dict, status_code=200)
def delete_movie(branch_id: int) -> dict:
    db = Session()
    car_branch_service = CarBranchServices(db)
    car_branch_service.delete_car_branch(branch_id,)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado la marca de vehiculo"})


