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
def create_movie(car_branch_request: CarBranchRequest) -> dict:
    db = Session()
    CarBranchServices(db).create_car_branch(car_branch_request)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})
   


# @car_branch_router.post('/movies', tags=['movies'], response_model=dict, status_code=201)
# def create_movie(movie: Movie) -> dict:
#     db = Session()
#     car_branchService(db).create_movie(movie)
#     return JSONResponse(status_code=201, content={"message": "Se ha registrado la película"})
   
# @car_branch_router.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
# def update_movie(id: int, movie: Movie)-> dict:
#     db = Session()
#     result = MovieService (db).get_movie(id)
#     if not result:
#         return JSONResponse(status_code=404, content={'message': "No encontrado"})
    
#     MovieService(db).update_movie(id, movie)

#     return JSONResponse(status_code=200, content={"message": "Se ha modificado la película"})


# @car_branch_router.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
# def delete_movie(id: int)-> dict:
#     db = Session()
#     result = db.query(MovieModel).filter(MovieModel.id == id).first()
#     if not result:
#         return JSONResponse(status_code=404, content={'message': "No encontrado"})
#     MovieService(db).delete_movie(id)
#     db.commit()
   
#     return JSONResponse(status_code=200, content={"message": "Se ha eliminado la película"})