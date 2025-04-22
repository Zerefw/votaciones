from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.candidate_model import Candidate
from app.models.voter_model import Voter
from app.schemas.candidate_schema import CandidateCreate, CandidateOut

# Definimos la ruta que se utilizará para los candidatos 
router = APIRouter(prefix="/candidates", tags=["Candidatos"])

# Crear un candidato
@router.post("/", response_model=CandidateOut, status_code=status.HTTP_201_CREATED)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    db_voter = db.query(Voter).filter(Voter.name == candidate.name).first()
    if db_voter:
        raise HTTPException(status_code=400, detail="El candidato ya esta registrado como votante")
        
    new_candidate = Candidate(**candidate.dict())
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate

# Obtener todos los candidatos
@router.get("/", response_model=list[CandidateOut])
def get_candidates(db: Session = Depends(get_db)):
    return db.query(Candidate).all()

# Obtener un candidato por su id
@router.get("/{candidate_id}", response_model=CandidateOut)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    return candidate

# Eliminar un candidato por su id
@router.delete("/{candidate_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(Candidate).filter(Candidate.id == candidate_id).first()
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")
    db.delete(candidate)
    # db.commit se utuliza para "guardar" los cambios en la db, ya que con db.delete se prepara lo que se quiere eliminar
    db.commit()