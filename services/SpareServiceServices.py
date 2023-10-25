from models.models import SpareService
from schemas.user import SpareServiceRequest


class SpareServiceServices():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_spares_service(self):
        result = self.db.query(SpareService).all()
        return result
    
    def get_spare_service(self,id):
        result =self.db.query(SpareService) .filter (SpareService.id ==id).first()
        return result 
    
    def get_spare_services_by_service_id(self,service_id):
        result =self.db.query(SpareService).filter (SpareService.service_id ==service_id).all()
        return result

    def create_spare_service(self, spare_service_request: SpareServiceRequest):
        new_service= SpareService(**spare_service_request.dict())
        self.db.add(new_service)
        self.db.commit()
        return
    
    def update_spare_service (self, id:int, data :SpareService):
        update_service = self.db.query(SpareService).filter(SpareService.id == id).first()
        update_service.name = data.name
        update_service.is_active = data.is_active
        update_service.service_id = data.is_active
        self.db.commit()
        return
    
    def delete_spare_service (self,id):
        self.db.query(SpareService).filter(SpareService.id == id).delete()
        self.db.commit()
        return
    
    