from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Modelo para definir la estructura de la tabla candidatos 
class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    party = Column(String, nullable=True)
    votes = Column(Integer, default=0)

    # Definimos la relacion que tiene el candidato con los votos
    received_votes = relationship("Vote", back_populates="candidate")