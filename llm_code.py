from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
llm = ChatGroq(st.secrets["GROQ_API_KEY"], model_name="llama-3.2-90b-text-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)