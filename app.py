from typing import List
import streamlit as st
import requests
import time
from funcs import get_questions,check_answer,evaluate_quiz,countdown_timer_sidebar


# === Hauptfunktion ===
def main():
    st.set_page_config(page_title="SmartQuiz 🌸", page_icon="🧠", layout="centered")
    st.title("🧠 SmartQuiz")

    # Initialisierung
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()
        st.session_state.time_limit = 60
        st.session_state.quiz_active = True
        st.session_state.submitted = False
        st.session_state.answers = {}
        st.session_state.result_shown = False

    questions = get_questions()
    if not questions:
        st.warning("❗ Keine Fragen verfügbar.")
        return

    if st.session_state.submitted:
        if not st.session_state.result_shown:
            evaluate_quiz(questions, st.session_state.answers)
        return

    selected_answers = {}

    for question in questions:
        st.subheader(question["question_text"])
        options = question.get("options", [])
        selected_option_ids = []

        for option in options:
            key = f"q{question['id']}_opt{option['id']}"
            if key not in st.session_state:
                st.session_state[key] = False

            if st.checkbox(option["text"], key=key):
                selected_option_ids.append(option["id"])

        selected_answers[question["id"]] = selected_option_ids

    st.session_state.answers = selected_answers

    if st.button("✅ Antworten abgeben"):
        st.session_state.submitted = True
        st.rerun()

    countdown_timer_sidebar()

# === App starten ===
if __name__ == "__main__":
    main()
