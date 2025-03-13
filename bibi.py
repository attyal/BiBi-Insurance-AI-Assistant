import streamlit as st
from gemini import ask_gemini  

st.markdown("""
    <style>
        body, .stApp {
            background: linear-gradient(135deg, #19447B, #228B22);
            background-attachment: fixed;
            color: white;
        }
        
        h1, h2, h3 {
            text-align: center;
            color: white;
        }

        div[data-testid="stTextInput"] > div {
            border-radius: 25px !important;
            padding: 8px;
            border: 2px solid #ddd;
            width: 100%;
        }
        input {
            border-radius: 25px !important;
            padding: 10px;
            border: none;
            width: 100%;
            outline: none;
        }

        div[data-testid="stTextInput"] {
            display: flex;
            justify-content: center;
        }

        div.stButton button {
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            display: block;
            margin: auto;
        }

        p {
            text-align: center;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.title("🌿 BiBi Insurance Assistant")
st.markdown("Ask me anything about insurance policies!")

# Rounded Search Bar
user_input = st.text_input("Enter your message:", "")

# Process user input
if user_input:
    response = ask_gemini(user_input)  # Get AI response
    st.markdown("Response:")
    st.write(response)

# Footer
st.markdown("<br><br><p style='text-align: center; color: white;'>BiBi is an AI chatbot built with Python and deployed using Streamlit and Github. Meant to be a more visiually pleasing alternative to a traditional chatbot"
".</p>", unsafe_allow_html=True)
