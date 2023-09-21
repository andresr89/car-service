from pydantic import BaseModel

class User(BaseModel):
    email:str
    password:str


class CarBranchRequest (BaseModel):
    id : int
    name : str
    is_active: bool

class CarModelRequest (BaseModel):
    id : int
    name : str
    is_active: bool
    car_brand_id : int