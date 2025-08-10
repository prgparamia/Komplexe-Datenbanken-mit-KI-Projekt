# main.py

from fastapi import FastAPI
from database import engine
from models import Base
from router import quiz_router  # Dein Quiz-Router

# FastAPI-App initialisieren
app = FastAPI(title="SmartQuiz API")

# Router registrieren
app.include_router(quiz_router)

# Datenbanktabellen erstellen
Base.metadata.create_all(bind=engine)

# Lokaler Startpunkt für die Entwicklung
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
