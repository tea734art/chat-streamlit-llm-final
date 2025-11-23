import streamlit as st
import google.generativeai as genai
from functions import get_secret, generate_ai_response

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Manchester United ChatBot",
    page_icon="⚽",
    layout="centered",
)

# ---- API KEY ----
api_key = get_secret("API_KEY")
genai.configure(api_key=api_key)

# ---- MODEL ----
model = genai.GenerativeModel("gemini-2.0-flash")

# ---- MUFC THEME ----
st.markdown("""
<style>
body {
    background-color: #000;
}
.main {
    background-color: #111;
}
.user-msg {
    background-color: #DA291C;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
    color: white;
}
.ai-msg {
    background-color: #272727;
    padding: 12px;
    border-radius: 10px;
    margin: 8px 0;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---- LOGO ----
try:
    st.image("assets/manutd_logo.png", width=150)
except:
    st.write("🔴⚫ *Manchester United ChatBot*")

st.title("🔴⚫ Manchester United Fan ChatBot")

# ---- SESSION MEMORY ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.session_state.chat_history.append(
        ("assistant", "Hi ManUtd Fans! How can I help you today? 🔴⚫")
    )

# ---- RENDER HISTORY ----
for role, content in st.session_state.chat_history:
    css = "user-msg" if role == "user" else "ai-msg"
    st.markdown(f"<div class='{css}'>{content}</div>", unsafe_allow_html=True)

# ---- USER INPUT ----
user_message = st.chat_input("Type your message...")

if user_message:
    st.session_state.chat_history.append(("user", user_message))
    ai_reply = generate_ai_response(model, st.session_state.chat_history)
    st.session_state.chat_history.append(("assistant", ai_reply))
    st.rerun()

# ---- SIDEBAR ----
st.sidebar.header("⚙️ Settings")
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()
