import random
from datetime import datetime

import streamlit as st

# ---------- Styling ----------
st.markdown(
    """
    <style>
        :root {
            --bg: #0f172a;
            --panel: #111827;
            --card: #1f2937;
            --text: #e5e7eb;
            --muted: #9ca3af;
            --accent: #60a5fa;
            --accent-2: #34d399;
        }
        body {
            background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
            color: var(--text);
        }
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #111827 100%);
        }
        div[data-testid="stChatMessage"] {
            background: rgba(255,255,255,0.02);
            border-radius: 14px;
            padding: 0.5rem 0.75rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Config ----------
st.set_page_config(page_title="sakshyam Bot", page_icon="🤖", layout="wide")
st.title("🤖 sakshyam Bot")
st.caption("Your friendly chat assistant with quick replies, jokes, facts, and more.")

# ---------- Data ----------
welcome_messages = [
    "Hey there! I’m sakshyam Bot — happy to chat with you.",
    "Hello! What can I help you with today?",
    "Hi! Ask me for a joke, fact, quote, or just say hello!",
]

responses = {
    "hello": [
        "Hey! I’m sakshyam Bot 😊",
        "Hello! Nice to meet you.",
        "Hi there! How can I help?",
    ],
    "how_are_you": [
        "I’m doing great, thanks for asking!",
        "Feeling awesome today!",
        "I’m good — ready to chat with you!",
    ],
    "name": [
        "I’m sakshyam Bot, your friendly AI assistant.",
        "People call me sakshyam Bot 😎",
        "I’m sakshyam Bot — here to help and chat.",
    ],
    "help": [
        "I can chat casually, tell jokes, share facts, give quotes, check the time, and help you with quick ideas.",
        "Try asking for a joke, a fact, a quote, my name, the time, or just say hello.",
    ],
    "bye": [
        "Goodbye, friend! See you soon!",
        "Take care! Chat again anytime.",
        "Bye! Have a great day!",
    ],
    "thanks": [
        "You’re very welcome!",
        "My pleasure 😊",
        "Always happy to help!",
    ],
    "creator": [
        "I was created by a student named sakshyam using Python.",
        "A creative coder built me to make chatting more fun.",
    ],
    "time": [
        "It’s {time} right now.",
        "The current time is {time}.",
    ],
    "joke": [
        "Why do programmers prefer dark mode? Because light attracts bugs. 😄",
        "I told my computer I needed a break, and now it won’t stop sending me vacation ads.",
        "Why was the Python script so calm? Because it had good syntax. 🤓",
    ],
    "fact": [
        "A day on Venus is longer than a year on Venus.",
        "Octopuses have three hearts.",
        "Honey never spoils — archaeologists have found pots of it still edible after thousands of years.",
    ],
    "quote": [
        "“Success is the sum of small efforts, repeated day in and day out.” — Robert Collier",
        "“The future depends on what you do today.” — Mahatma Gandhi",
        "“It always seems impossible until it’s done.” — Nelson Mandela",
    ],
    "motivation": [
        "You’ve got this! One small step today can lead to a big win tomorrow.",
        "Great things take time, but your effort matters more than your speed.",
        "Keep going — consistency beats perfection.",
    ],
    "weather": [
        "I can’t see the live weather, but I can help you plan for it — do you want a quick outfit idea or a weather-check routine?",
        "I don’t have live weather data here, but I can help you decide what to wear or do based on the forecast you share.",
    ],
}

# ---------- Helper functions ----------
def get_time():
    now = datetime.now()
    return now.strftime("%I:%M %p")


def normalize_message(message):
    return message.lower().strip()


def generate_reply(user_message):
    message = normalize_message(user_message)

    if not message:
        return "Please type a message so I can respond."

    if message in {"clear", "clear chat", "reset", "new chat"}:
        st.session_state.chat_history = []
        return "Chat cleared! Let’s start fresh."

    if message in {"help", "what can you do", "what can you do?", "commands"}:
        return random.choice(responses["help"])

    if "time" in message:
        return random.choice(responses["time"]).format(time=get_time())

    if any(word in message for word in ["hello", "hi", "hey", "namaste", "good morning", "good evening"]):
        return random.choice(responses["hello"])

    if any(word in message for word in ["how are you", "how r u", "how do you feel"]):
        return random.choice(responses["how_are_you"])

    if any(word in message for word in ["your name", "who are you", "what is your name", "what's your name"]):
        return random.choice(responses["name"])

    if any(word in message for word in ["who made you", "who created you", "your creator", "who built you"]):
        return random.choice(responses["creator"])

    if any(word in message for word in ["bye", "goodbye", "see you later", "talk later"]):
        return random.choice(responses["bye"])

    if any(word in message for word in ["thank you", "thanks", "thx"]):
        return random.choice(responses["thanks"])

    if any(word in message for word in ["joke", "funny", "make me laugh", "tell me a joke"]):
        return random.choice(responses["joke"])

    if any(word in message for word in ["fact", "interesting fact", "tell me a fact", "fun fact"]):
        return random.choice(responses["fact"])

    if any(word in message for word in ["quote", "inspiration", "motivational quote", "wise words"]):
        return random.choice(responses["quote"])

    if any(word in message for word in ["motivate me", "inspire me", "encourage me", "confidence"]):
        return random.choice(responses["motivation"])

    if any(word in message for word in ["weather", "temperature", "forecast"]):
        return random.choice(responses["weather"])

    for key, replies in responses.items():
        if key in message:
            return random.choice(replies)

    return (
        "I’m here to chat! Try asking me for a joke, a fact, a quote, the time, or simply say hello."
    )


# ---------- Session state ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------- Sidebar quick actions ----------
with st.sidebar:
    st.subheader("Quick actions")
    quick_actions = [
        "Say hello",
        "Tell me a joke",
        "Give me a fact",
        "Share a quote",
        "What can you do?",
        "What time is it?",
        "Clear chat",
    ]

    for action in quick_actions:
        if st.button(action, key=f"action_{action}"):
            if action == "Clear chat":
                st.session_state.chat_history = []
                st.session_state.last_prompt = "Chat cleared!"
            else:
                st.session_state.last_prompt = action

# ---------- Conversation display ----------
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- User input ----------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    reply = generate_reply(user_input)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
    st.rerun()

# ---------- Quick action trigger ----------
if "last_prompt" in st.session_state and st.session_state.last_prompt:
    prompt = st.session_state.last_prompt
    if prompt == "Chat cleared!":
        st.success(prompt)
    else:
        assistant_reply = generate_reply(prompt)
        if not any(msg["content"] == assistant_reply for msg in st.session_state.chat_history):
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_reply})
            st.session_state.last_prompt = None
            st.rerun()

# ---------- Welcome message ----------
if not st.session_state.chat_history:
    with st.chat_message("assistant"):
        st.markdown(random.choice(welcome_messages))
