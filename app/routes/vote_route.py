from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.database import get_db
from app.models.vote_model import Vote
from app.models.voter_model import Voter
from app.models.candidate_model import Candidate
from app.schemas.vote_schema import VoteCreate, VoteOut

router = APIRouter(prefix="/votes", tags=["Votos"])

@router.post("/", response_model=VoteOut)
def create_vote(vote: VoteCreate, db: Session = Depends(get_db)):
    # Verificar si el votante existe
    voter = db.query(Voter).filter(Voter.id == vote.voter_id).first()
    if not voter:
        raise HTTPException(status_code=404, detail="Votante no encontrado")

    # Verificar si el candidato existe
    candidate = db.query(Candidate).filter(Candidate.id == vote.candidate_id).first()
    if not candidate:
        raise HTTPException(status_code=404, detail="Candidato no encontrado")

    # Verificar que el votante no haya votado ya
    existing_vote = db.query(Vote).filter(Vote.voter_id == vote.voter_id).first()
    if existing_vote:
        raise HTTPException(status_code=400, detail="El votante ya ha emitido un voto")

    # Registrar el voto
    new_vote = Vote(**vote.dict())
    db.add(new_vote)

    # Incrementar los votos del candidato
    candidate.votes += 1

    db.commit()
    db.refresh(new_vote)
    return new_vote

@router.get("/", response_model=list[VoteOut])
def get_votes(db: Session = Depends(get_db)):
    return db.query(Vote).all()

@router.get("/statistics")
def vote_statistics(db: Session = Depends(get_db)):
    total_votes = db.query(func.count(Vote.id)).scalar()
    total_voters = db.query(func.count(func.distinct(Vote.voter_id))).scalar()

    candidate_votes = db.query(
        Candidate.name,
        Candidate.votes
    ).all()

    stats = []
    for name, votes in candidate_votes:
        percentage = (votes / total_votes * 100) if total_votes else 0
        stats.append({
            "name": name,
            "votes": votes,
            "percentage": round(percentage, 2)
        })

    return {
        "total_votes": total_votes,
        "total_voters_who_voted": total_voters,
        "candidates": stats
    }