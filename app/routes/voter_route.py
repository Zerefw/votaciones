from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.voter_schema import VoterCreate
from app.models.voter_model import Voter
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("")
async def create_voter(voter_data: VoterCreate):
  return ''

@router.get("")
async def get_all_voters(db: Session = Depends(get_db)):
   return db.query(Voter).all()

@router.get("/{id}")
async def get_voter_by_id(id: int):
  return ''

@router.delete("/{id}")
async def delete_voter_by_id(id: int):
  return ''
