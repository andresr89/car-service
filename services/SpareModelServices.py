from models.models import SpareModel
from schemas.user import SpareModelRequest


class SpareModelServices():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_spare_models(self):
        result = self.db.query(SpareModel).all()
        return result
    
    def get_spare_model(self,id):
        result =self.db.query(SpareModel) .filter (SpareModel.id ==id).first()
        return result 

    def create_spare_model(self, spare_model_request: SpareModelRequest):
        new_model= SpareModel(**spare_model_request.dict())
        self.db.add(new_model)
        self.db.commit()
        return
    
    def update_spare_model (self, id:int, data :SpareModel):
        update_spare = self.db.query(SpareModel).filter(SpareModel.id == id).first()
        update_spare.name = data.name
        update_spare.is_active = data.is_active
        update_spare.car_model_id = data.is_active
        self.db.commit()
        return
    
    def delete_spare_model (self,id):
        self.db.query(SpareModel).filter(SpareModel.id == id).delete()
        self.db.commit()
        return
    
    