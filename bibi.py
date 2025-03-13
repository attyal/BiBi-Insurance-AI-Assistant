import streamlit as st
from gemini import ask_gemini

st.title("BiBi Insurance Assistant")
st.write("Ask about an insurance policy:")

user_input = st.text_input("Enter your message:", "")

if user_input:
    response = ask_gemini(user_input) 
    st.write(response)
