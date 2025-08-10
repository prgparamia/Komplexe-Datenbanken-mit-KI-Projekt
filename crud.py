from sqlalchemy.orm import Session
from typing import List

# Nur benötigte Klassen importieren
from models import Question, Option
from schemas import QuestionCreate

# Repository-Klasse für Fragen
class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session  # SQLAlchemy-Session speichern

    def create_question(self, question: QuestionCreate) -> Question:
        # Neue Frage anlegen
        db_question = Question(question_text=question.question_text)
        self.session.add(db_question)
        self.session.commit()
        self.session.refresh(db_question)

        # Antwortoptionen hinzufügen
        for opt in question.options:
            db_option = Option(
                text=opt.text,
                is_correct=opt.is_correct,
                question_id=db_question.id
            )
            self.session.add(db_option)

        self.session.commit()
        self.session.refresh(db_question)
        return db_question

    def get_all_questions(self) -> List[Question]:
        # Alle Fragen abrufen
        return self.session.query(Question).all()


# Repository-Klasse für Antworten
class AntwortRepository: 
    def __init__(self, session: Session):
        self.session = session  # SQLAlchemy-Session speichern

    def check_answer(self, question_id: int, selected_option_ids: List[int]) -> dict:
        # Alle korrekten Optionen zur Frage laden
        correct_options = self.session.query(Option).filter(
           Option.question_id == question_id,
           Option.is_correct==True
        ).all()

        correct_ids = {opt.id for opt in correct_options}
        selected_ids = set(selected_option_ids)

        # Prüfung: sind die ausgewählten Optionen genau die richtigen?
        is_correct = correct_ids == selected_ids

        return {
            "correct": is_correct,
            "correct_option_ids": list(correct_ids)
        }
