import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
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
