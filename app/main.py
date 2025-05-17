import openai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("📚 AI Problem Generator")

notes = st.text_area("Paste your lecture notes here")
if st.button("Generate Questions:"):
    if notes.strip() == "":
        st.warning("Please enter some lecture notes first.")
    else:
        with st.spinner("Generating questions..."):
            prompt = f"""
            You are an AI that generates educational practice problem.
            Given the following lecture notes, generate three practice problem questions with solutions.

            Lecture Notes:
            \"\"\"
            {Notes}
            \"\"\"
            """

            response = openai.ChatCompletion.create(
                model = "gpt-3.5",
                messages=[{"role": "user", "content": "prompt"}],
                temperature = 0.7,
            )
            output = responce.choices[0].message.context.strip()
            st.markdown("Generated questions and answers: ")
            st.text_area("Output", output, height=400)
    