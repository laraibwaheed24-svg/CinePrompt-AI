import streamlit as st
from modules.poster_generator import generate_movie_poster


def display_movie_header(movie):

    poster_key = "movie_poster"

    if poster_key not in st.session_state:
        st.session_state[poster_key] = None


    st.title(f"🎬 {movie['movie_title']}")

    if st.button("🎨 Generate Movie Poster"):

        with st.spinner("Creating movie poster..."):

            st.session_state[poster_key] = generate_movie_poster(movie)

    if st.session_state[poster_key]:

        st.image(
            st.session_state[poster_key],
            caption="AI Movie Poster",
            use_container_width=True,
        )
    

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
