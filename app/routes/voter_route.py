from fastapi import APIRouter
from app.schemas.voter_schema import VoterCreate

router = APIRouter()

@router.post("")
async def create_voter(voter_data: VoterCreate):
  return ''

@router.get("")
async def get_all_voters():
  return ''

@router.get("/{id}")
async def get_voter_by_id(id: int):
  return ''

@router.delete("/{id}")
async def delete_voter_by_id(id: int):
  return ''
