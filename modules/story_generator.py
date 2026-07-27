from groq import Groq
import streamlit as st

from config.prompts import SYSTEM_PROMPT


client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)


def generate_story(user_prompt):

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        temperature=0.8,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content
