from pydantic import BaseModel, EmailStr
from typing import Optional

class CandidateBase(BaseModel):
    name: str
    party: Optional[str] = None

class CandidateCreate(CandidateBase):
    pass

class CandidateOut(CandidateBase):
    id: int
    votes: int

    # class Config:
    #     orm_mode = True
