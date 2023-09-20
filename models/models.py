from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class CarBranch(Base):

    __tablename__ = "car_branch"
 

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    