from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


class CarBrand(Base):

    __tablename__ = "car_brand"
 

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
  

class CarModel(Base):

    __tablename__ = "car_model"


    id = Column (Integer, primary_key= True, autoincrement=True)
    name = Column (String)
    is_active = Column(Boolean)
    car_brand_id = Column(Integer)
 


class SpareService(Base):

    __tablename__ = "spare_service"

    id = Column(Integer, primary_key = True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    service_id = Column(Integer)
 


class SpareModel(Base):  

    __tablename__ = "spare_model"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    is_active = Column(Boolean)
    car_model_id = Column(Integer)  
    # car_model = relationship("CarModel", back_populates="spare_models") error mapper

class Service(Base):

    __tablename__ = "service"


    id = Column (Integer, primary_key= True, autoincrement=True)
    name = Column (String)
    is_active = Column(Boolean)
    spare_service_id = Column (Integer)    

class ServiceCarModel(Base):
        
    __tablename__ = "service_car_model"

    id = Column (Integer, primary_key= True, autoincrement=True)
    car_model_id = Column (Integer)




