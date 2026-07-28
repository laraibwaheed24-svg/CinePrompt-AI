from groq import Groq
import streamlit as st
import json

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

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by AI.",
            "raw_response": content
        }
