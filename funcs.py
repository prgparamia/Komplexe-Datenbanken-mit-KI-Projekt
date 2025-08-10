
import streamlit as st
import requests
import time
from typing import List
# === Backend API URL ===
API_URL = "http://127.0.0.1:8000/quiz"

# === Funktion: Holt alle Fragen ===
def get_questions():
    try:
        response = requests.get(f"{API_URL}/questions")
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Fehler beim Laden der Fragen.")
            return []
    except Exception as e:
        st.error(f"Verbindungsfehler: {e}")
        return []

# === Funktion: Antwort prüfen ===
def check_answer(question_id: int, selected_option_ids: List[int]):
    try:
        response = requests.post(
            f"{API_URL}/questions/{question_id}/check",
            json={"selected_option_ids": selected_option_ids}
        )
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Fehler bei der Antwortüberprüfung.")
            return {}
    except Exception as e:
        st.error(f"Fehler: {e}")
        return {}

# === Funktion: Countdown-Timer ===
def countdown_timer_sidebar():
    with st.sidebar:
        timer_placeholder = st.empty()
        time_limit = st.session_state.get("time_limit",120)
        start_time = st.session_state.get("start_time", time.time())
        elapsed = int(time.time() - start_time)
        remaining = max(0, time_limit - elapsed)
        minutes, secs = divmod(remaining, 60)

        if remaining > 0:
            timer_placeholder.markdown(f"⏳ **Verbleibende Zeit: {minutes:02d}:{secs:02d}**")
            time.sleep(1)
            st.rerun()
        else:
            timer_placeholder.markdown("🛑 **Zeit abgelaufen!**")
            if not st.session_state.submitted:
                st.session_state.submitted = True
                st.rerun()

# === Funktion: Kirschblüten-Effekt ===
def flower_shower():
    blossom_css = """
    <style>
    @keyframes fall {
        0% {
            transform: translateY(-100px) rotate(0deg);
            opacity: 1;
        }
        100% {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }

    .blossom {
        position: fixed;
        top: -50px;
        font-size: 24px;
        pointer-events: none;
        animation-name: fall;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }

    .b1 { left: 10%; animation-duration: 6s; animation-delay: 0s; }
    .b2 { left: 25%; animation-duration: 7s; animation-delay: 1s; }
    .b3 { left: 40%; animation-duration: 5.5s; animation-delay: 2s; }
    .b4 { left: 60%; animation-duration: 6.5s; animation-delay: 0.5s; }
    .b5 { left: 75%; animation-duration: 7.2s; animation-delay: 1.5s; }
    .b6 { left: 90%; animation-duration: 6.8s; animation-delay: 0.8s; }
    </style>

    <div class="blossom b1">🌸</div>
    <div class="blossom b2">🌸</div>
    <div class="blossom b3">🌸</div>
    <div class="blossom b4">🌸</div>
    <div class="blossom b5">🌸</div>
    <div class="blossom b6">🌸</div>
    """
    st.markdown(blossom_css, unsafe_allow_html=True)

# === Funktion: Ergebnisse auswerten ===
def evaluate_quiz(questions, selected_answers):
    score = 0
    total = len(selected_answers)

    for question in questions:
        question_id = question["id"]
        selected_ids = selected_answers.get(question_id, [])
        result = check_answer(question_id, selected_ids)

        if result:
            correct = result["correct"]
            correct_ids = result["correct_option_ids"]
            option_map = {opt["id"]: opt["text"] for opt in question["options"]}

            if correct:
                st.success(f"Frage {question_id}: ✅ Richtig!")
                score += 1
            else:
                st.error(f"Frage {question_id}: ❌ Falsch.")
                correct_texts = [option_map[oid] for oid in correct_ids]
                st.info(f"✔️ Richtige Antwort(en): {', '.join(correct_texts)}")

    st.success(f"🎯 Dein Score: {score} / {total}")
    st.session_state.quiz_active = False
    st.session_state.result_shown = True

    flower_shower()  # Kirschblüten am Ende