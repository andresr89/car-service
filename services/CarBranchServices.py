from models.models import CarBranch
from schemas.user import CarBranchRequest


class CarBranchServices():
    
    def __init__(self, db) -> None:
        self.db = db

    
    
    def create_car_branch(self, car_branch_request: CarBranchRequest):
        new_branch = CarBranch(**car_branch_request.dict())
        self.db.add(new_branch)
        self.db.commit()
        return
    
    def update_car_branch (self, id:int, data :CarBranch):
        update_branch = self.db.query(CarBranch).filter(CarBranch.id == id).first()
        update_branch.name = data.name
        update_branch.is_active = data.is_active
        self.db.commit()
        return
    
    def delete_car_branch (self,id):
        self.db.query(CarBranch).filter(CarBranch.id == id).delete()
        self.db.commit()
        return
    
    