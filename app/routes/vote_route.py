from fastapi import APIRouter
from app.schemas.vote_schema import VoteCreate

router = APIRouter()

@router.post("")
async def create_vote(vote_data: VoteCreate):
  return ''

@router.get("")
async def get_all_votes():
  return ''

@router.get("/statistics")
async def get_statistics(id: int):
  return ''
