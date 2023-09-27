from models.models import CarBrand
from schemas.user import CarBrandRequest


class CarBrandServices():
    
    def get_car_brands(self):
        result = self.db.query(CarBrand).all()
        return result
    
    def get_car_brand(self,id):
        result =self.db.query(CarBrand) .filter (CarBrand.id ==id).first()
        return result
   


    def __init__(self, db) -> None:
        self.db = db

    
    
    def create_car_brand(self, car_brand_request: CarBrandRequest):
        new_brand = CarBrand(**car_brand_request.dict())
        self.db.add(new_brand)
        self.db.commit()
        return
    
    def update_car_brand (self, id:int, data :CarBrand):
        update_brand = self.db.query(CarBrand).filter(CarBrand.id == id).first()
        update_brand.name = data.name
        update_brand.is_active = data.is_active
        self.db.commit()
        return
    
    def delete_car_brand (self,id):
        self.db.query(CarBrand).filter(CarBrand.id == id).delete()
        self.db.commit()
        return
    
    