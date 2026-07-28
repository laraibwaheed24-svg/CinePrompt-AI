import streamlit as st

st.set_page_config(
    page_title="Storyboard Studio",
    page_icon="📚",
    layout="wide"
)


st.title("📚 Storyboard Studio")


if "movie" not in st.session_state or st.session_state.movie is None:

    st.warning(
        "No movie found. Please generate a story first."
    )

else:

    movie = st.session_state.movie

    st.success(
        f"Storyboard: {movie['movie_title']}"
    )

    st.markdown("---")


    for scene in movie["scenes"]:

        st.subheader(
            f"🎬 Scene {scene['scene_number']}: {scene['title']}"
        )

        st.write(
            scene["description"]
        )

        st.info(
            scene["image_prompt"]
        )

        st.markdown("---")
