import streamlit as st


def display_sidebar():

    st.sidebar.title("🎬 CinePrompt AI")

    st.sidebar.success("Version 1.0")

    st.sidebar.divider()

    st.sidebar.markdown("## 🚀 Development Progress")

    st.sidebar.checkbox("Project Setup", value=True, disabled=True)

    st.sidebar.checkbox("Story Generator", value=True, disabled=True)

    st.sidebar.checkbox("AI Director", value=True, disabled=True)

    st.sidebar.checkbox("Image Generation", value=False, disabled=True)

    st.sidebar.checkbox("Voice Narration", value=False, disabled=True)

    st.sidebar.checkbox("Video Rendering", value=False, disabled=True)
