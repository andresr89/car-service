from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


class CarBranch(Base):

    __tablename__ = "car_branch"
 

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    car_models = relationship("CarModel", back_populates="car_branch")

class CarModel(Base):

    __tablename__ = "car_model"


    id = Column (Integer, primary_key= True, autoincrement=True)
    name = Column (String)
    is_active = Column(Boolean)
    car_brand_id = Column(Integer, ForeignKey('car_branch.id'))
    car_branch = relationship("CarBranch", back_populates="car_models")

class SpareService(Base):

    __tablename__ = "spare_service"

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    spare_model_id = Integer


class SpareModel(Base):  

    __tablename__ = "spare_model"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    car_model_id = Column(Integer, ForeignKey('car_model.id'))  
    car_model = relationship("CarModel", back_populates="spare_models") 






