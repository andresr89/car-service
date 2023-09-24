from models.models import CarModel
from schemas.user import CarModelRequest


class CarModelServices():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_car_models(self):
        result = self.db.query(CarModel).all()
        return result
    
    def get_car_model(self,id):
        result =self.db.query(CarModel) .filter (CarModel.id ==id).first()
        return result 

    def create_car_model(self, car_model_request: CarModelRequest):
        new_model= CarModel(**car_model_request.dict())
        self.db.add(new_model)
        self.db.commit()
        return
    
    def update_car_model (self, id:int, data :CarModel):
        update_model = self.db.query(CarModel).filter(CarModel.id == id).first()
        update_model.name = data.name
        update_model.is_active = data.is_active
        update_model.car_brand_id = data.is_active
        self.db.commit()
        return
    
    def delete_car_model (self,id):
        self.db.query(CarModel).filter(CarModel.id == id).delete()
        self.db.commit()
        return
    
    