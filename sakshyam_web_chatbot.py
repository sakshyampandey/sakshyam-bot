import streamlit as st
import random
from datetime import datetime
st.markdown("<style>body{background-color:#f4f4f4;}</style>", unsafe_allow_html=True)

greetings = ["hello", "hi", "hey", "namaste", "good morning", "good evening"]

responses = {
    "hello": ["Hey nigga! I'm sakshyam 😊", "Hello! How can I help you?", "Hi, good to see you!"],
    "how are you": ["I'm doing great, thanks for asking!", "Feeling awesome today!", "All good! How about you?"],
    "your name": ["I'm sakshyam Bot, yaur friendly male assistant.", "People call me sakshyam dona 😊", "I'm sakshyam — your AI friend."],
    "what can you do": ["I can chat, answer questions, and make your day better!", "I can talk with you and learn more!"],
    "bye": ["Goodbye, friend!", "See you soon!", "Take care!"],
    "who made you": ["I was created by a student sakshyam using Python.", "A smart and asthetic Nepali coder built me 😎."],
}

def get_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")

st.set_page_config(page_title="sakshyam Bot", page_icon="🤖", layout="centered")
st.title("🤖 sakshyam Bot - Your Friendly Male Chat Assistant")
st.markdown("Talk with sakshyam! Type your message below 👇")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    message = user_input.lower().strip()
    reply = "Hmm... nasodh yesto malai auuna balla sikdai xu!"

    if "time" in message:
        reply = f"It's {get_time()} right now."
    elif message in greetings:
        reply = random.choice(responses["hello"])
    else:
        for key in responses.keys():
            if key in message:
                reply = random.choice(responses[key])
                break

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("sakshyam Bot", reply))

for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 {speaker}:** {msg}")
    else:
        st.markdown(f"**🤖 {speaker}:** {msg}")
