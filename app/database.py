from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Variables para la conexion a la base de datos
DB_USER = "postgres"
DB_PASSWORD = "Demonologie2025++"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "votaciones"

# Creacion de la url para conectarnos a la base de datos
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Crear todo el sistema de conexion a la db y mantener la sesion
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener la DB en cada request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()