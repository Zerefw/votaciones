from pydantic import BaseModel
from typing import Optional

class VoteBase(BaseModel):
    voter_id: int
    candidate_id: int

class VoteCreate(VoteBase):
    pass

class VoteOut(VoteBase):
    id: int

    class Config:
        orm_mode = True