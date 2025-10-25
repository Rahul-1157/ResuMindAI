# src/resumind/config.py
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

def configure_gemini_api():
    """
    Loads the environment variables and configures the Gemini API.
    Returns True if successful, False otherwise.
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return False
    
    try:
        genai.configure(api_key=api_key)
        return True
    except Exception as e:
        # Using st.error to display the error message in the Streamlit app
        st.error(f"Error configuring the Gemini API: {e}")
        return False