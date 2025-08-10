# routers/quiz.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from crud import QuestionRepository, AntwortRepository
from schemas import QuestionCreate, QuestionRead, AnswerRequest, AnswerResponse
from models import Question

quiz_router = APIRouter(prefix="/quiz", tags=["quiz"])

# Neue Frage anlegen
@quiz_router.post("/questions", response_model=QuestionRead)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    repo = QuestionRepository(db)
    return repo.create_question(question)

# Alle Fragen abrufen
@quiz_router.get("/questions", response_model=List[QuestionRead])
def list_questions(db: Session = Depends(get_db)):
    repo = QuestionRepository(db)
    return repo.get_all_questions()

# Antwort prüfen
@quiz_router.post("/questions/{question_id}/check", response_model=AnswerResponse)
def check_answer(question_id: int, answer: AnswerRequest, db: Session = Depends(get_db)):
    repo = AntwortRepository(db)
    result = repo.check_answer(question_id, answer.selected_option_ids)
    return AnswerResponse(
        correct=result["correct"],
        correct_option_ids=result["correct_option_ids"]
    )
