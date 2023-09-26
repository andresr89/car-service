from models.models import Service
from schemas.user import ServiceRequest


class ServiceServices():
    
    def __init__(self, db) -> None:
        self.db = db

    def get_services (self):
        result = self.db.query(Service).all()
        return result
    
    def get_service(self,id):
        result =self.db.query(Service) .filter (Service.id ==id).first()
        return result 

    def create_service(self, service_request: ServiceRequest):
        new_service= Service(**service_request.dict())
        self.db.add(new_service)
        self.db.commit()
        return
    
    def update_service(self, id:int, data :Service):
        update_service = self.db.query(Service).filter(Service.id == id).first()
        update_service.name = data.name
        update_service.is_active = data.is_active
        update_service.spare_serice_id = data.is_active
        self.db.commit()
        return
    
    def delete_service(self,id):
        self.db.query(Service).filter(Service.id == id).delete()
        self.db.commit()
        return
    
    