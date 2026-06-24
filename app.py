import streamlit as st
from google import genai

client = genai.Client(
    api_key="AQ.Ab8RN6LFdvYRUGeyao3NhwF5w_Y2csBSmSRnD_sXB6_6wDjQvQ"
)

st.title("🤖 Gemini Research Chatbot")

question = st.text_input("Ask me something:")

if st.button("Submit"):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question
    )

    st.write("Answer:")
    st.write(response.text)

if st.button("Clear"):
    st.rerun()
