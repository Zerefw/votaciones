from fastapi import FastAPI
from app.routes.voter_route import router as voter_router
from app.routes.candidate_route import router as candidate_router
from app.routes.vote_route import router as vote_router
from app.database import Base, engine

# Creamos todas las tablas para definir de forma correcta las relaciones
Base.metadata.create_all(bind=engine)

# Inicializamos la app con fastApi y traemos las rutas
app = FastAPI(title="API de votaciones", description="API para contabilizar votos de los candidatos que se registren", version="1.0")
app.include_router(voter_router)
app.include_router(candidate_router)
app.include_router(vote_router)

# Ruta base para indicar de que la api funciona o dar la bienvenida
@app.get("/")
def read_root():
    return {"message": "API de votaciones"}
