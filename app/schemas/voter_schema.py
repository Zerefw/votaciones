from pydantic import BaseModel, EmailStr
from typing import Optional

class VoterBase(BaseModel):
    name: str
    email: EmailStr

class VoterCreate(VoterBase):
    pass

class VoterOut(VoterBase):
    id: int
    has_voted: bool

    class Config:
        orm_mode = True
        