from fastapi import FastAPI
from routers import motivos
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Reclamos API",
    description="Back end desarrollado para la aplicación de reclamos de la empresa Apromed S.A.S.",
    version="1.0.5",
    contact={
        "name": "Diego Carrera",
        "url": "http://loxasoluciones.com/",
        "email": "dfcarrera@outlook.com",
    }
)

# API endpoints
app.include_router(motivos.router)

# Allow all origins in CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)