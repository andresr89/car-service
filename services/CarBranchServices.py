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
        movie = self.db.query (CarBranch).filter(CarBranch.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def delete_car_branch (self,id):
        self.db.query(CarBranch).filter(CarBranch.id == id).delete()
        self.db.commit()
        return
    
    