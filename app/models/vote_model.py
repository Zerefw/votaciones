from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Modelo para definir la estructura de los votos
class Vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey("voter.id"), unique=True, nullable=False)
    candidate_id = Column(Integer, ForeignKey("candidate.id"), nullable=False)

    # Relaciones de los votantes y los candidatos en los votos
    voter = relationship("Voter", back_populates="vote")
    candidate = relationship("Candidate", back_populates="received_votes")