from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey("voter.id"), unique=True, nullable=False)
    candidate_id = Column(Integer, ForeignKey("candidate.id"), nullable=False)

    voter = relationship("Voter", back_populates="vote")
    candidate = relationship("Candidate", back_populates="received_votes")