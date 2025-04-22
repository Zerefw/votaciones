from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Modelo para definir la estructura de la tabla votantes
class Voter(Base):
    __tablename__ = "voter"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    has_voted = Column(Boolean, default=False)

    # Relacion del voto con el votante
    vote = relationship("Vote", back_populates="voter", uselist=False)