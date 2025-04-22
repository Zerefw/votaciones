from fastapi import APIRouter
from app.schemas.candidate_schema import CandidateCreate

router = APIRouter()

@router.post("")
async def create_candidate(candidate_data: CandidateCreate):
  return ''

@router.get("")
async def get_all_candidates():
  return ''

@router.get("/{id}")
async def get_candidate_by_id(id: int):
  return ''

@router.delete("/{id}")
async def delete_candidate_by_id(id: int):
  return ''
