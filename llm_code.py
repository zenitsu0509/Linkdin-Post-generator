from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
llm = ChatGroq(api_key = st.secrets["GROQ_API_KEY"], model_name="llama-3.2-90b-text-preview")

