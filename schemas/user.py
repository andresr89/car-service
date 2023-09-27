from pydantic import BaseModel

class User(BaseModel):
    email:str
    password:str


class CarBrandRequest (BaseModel):
    id : int
    name : str
    is_active: bool

class CarModelRequest (BaseModel):
    id : int
    name : str
    is_active: bool
    car_brand_id : int

class SpareServiceRequest (BaseModel):
    id : int
    name : str
    is_active : bool
    spare_model_id :int

class SpareModelRequest (BaseModel):
    id : int
    name : str
    is_active : bool
    car_model_id : int

class ServiceRequest (BaseModel):
    id: int
    name: str
    is_active : bool
    spare_service_id :int

class ServiceCarModelRequest (BaseModel):
    id : int
    car_model_id : int
