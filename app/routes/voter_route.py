from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.voter_model import Voter
from app.schemas.voter_schema import VoterCreate, VoterOut

router = APIRouter(prefix="/voters", tags=["Votantes"])

@router.post("/", response_model=VoterOut, status_code=status.HTTP_201_CREATED)
def create_voter(voter: VoterCreate, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.email == voter.email).first()
    if db_voter:
        raise HTTPException(status_code=400, detail="El correo ya está registrado")
    
    new_voter = Voter(**voter.dict())
    db.add(new_voter)
    db.commit()
    db.refresh(new_voter)
    return new_voter

@router.get("/", response_model=list[VoterOut])
def get_voters(db: Session = Depends(get_db)):
    return db.query(Voter).all()

@router.get("/{id}", response_model=VoterOut)
def get_voter(id: int, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    return voter

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_voter(id: int, db: Session = Depends(get_db)):
    voter = db.query(Voter).filter(Voter.id == id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")
    db.delete(voter)
    db.commit()