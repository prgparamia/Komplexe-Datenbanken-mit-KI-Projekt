from pydantic import BaseModel
from typing import List

# Eingabe für eine Option
class OptionCreate(BaseModel):
    text: str
    is_correct: bool

# Eingabe für eine Frage
class QuestionCreate(BaseModel):
    question_text: str
    options: List[OptionCreate]

# Option-Ausgabe
class OptionRead(BaseModel):
    id: int
    text: str
    is_correct: bool

    class Config:
        from_attributes= True

# Frage-Ausgabe
class QuestionRead(BaseModel):
    id: int
    question_text: str
    options: List[OptionRead]

    class Config:
        from_attributes = True

# Eingabe zur Antwortüberprüfung
class AnswerRequest(BaseModel):
    selected_option_ids: List[int]

# Antwort-Ausgabe
class AnswerResponse(BaseModel):
    correct: bool
    correct_option_ids: List[int]
