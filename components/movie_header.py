import streamlit as st


def display_movie_header(movie):

    st.title(f"🎬 {movie['movie_title']}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🎭 Genre", movie["genre"])

    with col2:
        st.metric("⏱ Duration", movie["duration"])

    with col3:
        st.metric("🎬 Scenes", len(movie["scenes"]))

    st.markdown("### 🧑 Main Characters")

    for character in movie["characters"]:
        st.write(f"• {character}")

    st.markdown("### 📖 Story Summary")

    st.info(movie["summary"])

    st.divider()
