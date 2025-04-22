from fastapi import FastAPI
from app.routes.voter_route import router as voter_router
from app.routes.candidate_route import router as candidate_router
from app.routes.vote_route import router as vote_router

app = FastAPI(title="API de votaciones", description="API para contabilizar votos de los candidatos que se registren", version="1.0")
app.include_router(voter_router)
app.include_router(candidate_router, prefix="/candidate", tags=["Candidatos"])
app.include_router(vote_router, prefix="/votes", tags=["Votos"])

@app.get("/")
def read_root():
  return {"message": "API de votaciones"}
