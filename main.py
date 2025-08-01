# main.py — punkt wejścia aplikacji FastAPI
from fastapi import FastAPI
from app import routes
from dotenv import load_dotenv
import os

load_dotenv()

# Tworzenie instancji aplikacji
app = FastAPI(
    title="My FastAPI App",
    description="Prosta aplikacja FastAPI",
    version="0.1.0"
)

# Rejestracja tras
app.include_router(routes.router)

# Punkt startowy: uruchomienie serwera przez uvicorn
# > uvicorn main:app --reload
