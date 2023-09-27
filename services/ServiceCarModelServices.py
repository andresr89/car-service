from models.models import ServiceCarModel
from schemas.user import ServiceCarModelRequest


class ServiceCarModelServices():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_service_car_models(self):
        result = self.db.query(ServiceCarModel).all()
        return result
    
    def get_service_car_model(self,id):
        result =self.db.query(ServiceCarModel) .filter (ServiceCarModel.id ==id).first()
        return result 

    def create_service_car_model(self, car_model_request: ServiceCarModelRequest):
        new_model= ServiceCarModel(**ServiceCarModelRequest.dict())
        self.db.add(new_model)
        self.db.commit()
        return
    
    def update_service_car_model (self, id:int, data :ServiceCarModel):
        update_model = self.db.query(ServiceCarModel).filter(ServiceCarModel.id == id).first()
        update_model.car_model_id = data.is_active
        self.db.commit()
        return
    
    def delete_service_car_model (self,id):
        self.db.query(ServiceCarModel).filter(ServiceCarModel.id == id).delete()
        self.db.commit()
        return
    
    