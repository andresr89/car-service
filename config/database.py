import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


db_params = {
    'database': 'db_car_service',
    'user': 'postgres',
    'password': '2511',
    'host': 'localhost',  
    'port': '5432',       
}

# Construye la URL de conexión a PostgreSQL
db_url = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"

# Crea el motor de SQLAlchemy
engine = create_engine(db_url, echo=True)

# Crea una sesión
Session = sessionmaker(bind=engine)

# Declara la base de datos
Base = declarative_base()
