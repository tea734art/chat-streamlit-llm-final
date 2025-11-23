import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai


def get_secret(key):
    """
    Retrieve secrets from Streamlit Cloud OR .env locally.
    """
    try:
        return st.secrets[key]
    except Exception:
        load_dotenv()
        return os.getenv(key)


def generate_ai_response(model, messages):
    """
    Send conversation history to Gemini 2.0 Flash.
    messages: [(role, content), ...]
    """

    formatted_history = []
    for role, content in messages:
        formatted_history.append({
            "role": "user" if role == "user" else "model",
            "parts": [content],
        })

    response = model.generate_content(formatted_history)
    return response.text
