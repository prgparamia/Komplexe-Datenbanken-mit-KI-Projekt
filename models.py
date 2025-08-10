from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class BaseRepr:
    """ generischhe __repr__Methode
        alle Klassen, die von  BaseRepr erben, bekommen automatisch eine
        def __repr__-Methode
    """
    def __repr__(self):
        fields = ", ".join(
            f"{col.name}={getattr(self, col.name)!r}"
            for col in self.__table__.columns
        )
        return f"<{self.__class__.__name__}({fields})>"



# Das 'Question' Modell repräsentiert eine einzelne Frage im Quiz
class Question(Base,BaseRepr):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)  # Primärschlüssel für Frage
    question_text = Column(String, nullable=False)  # Text der Frage

    # Eine Frage kann mehrere Optionen haben, die mit dem 'Option' Modell verknüpft sind
    options = relationship("Option", back_populates="question", cascade="all, delete")



# Das 'Option' Modell repräsentiert eine mögliche Antwort auf eine Frage

class Option(Base):
    __tablename__ = "options"
    id = Column(Integer, primary_key=True, index=True)  # Primärschlüssel für Option
    question_id = Column(Integer, ForeignKey("questions.id"))  # Fremdschlüssel, um die Option mit der Frage zu verbinden
    text = Column(String, nullable=False)  # Text der Option
    is_correct = Column(Boolean, default=False)  # Flag, das angibt, ob die Option korrekt ist

    # Rückbeziehung zur 'Question' Tabelle
    question = relationship("Question", back_populates="options")
