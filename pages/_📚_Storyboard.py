import streamlit as st
from modules.pdf_generator import create_storyboard_pdf

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


        image_key = f"scene_image_{scene['scene_number']}"


        if image_key in st.session_state and st.session_state[image_key]:

            st.image(
                st.session_state[image_key],
                caption=f"Scene {scene['scene_number']} Image",
                use_container_width=True
            )

        else:

            st.warning(
                "🖼 Image not generated yet for this scene."
            )


        
        st.markdown("---")

        if st.button("📄 Generate Storyboard PDF"):

            pdf_file = create_storyboard_pdf(movie)

            with open(pdf_file, "rb") as file:

                st.download_button(
                    "⬇ Download PDF",
                    file,
                    file_name="CinePrompt_Storyboard.pdf",
                    mime="application/pdf"
                )
