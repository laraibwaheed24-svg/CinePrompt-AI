import streamlit as st
from modules.image_generator import generate_image


def display_scene(scene):
    """
    Display a single movie scene.
    """

    st.markdown("---")

    st.subheader(
        f"🎬 Scene {scene['scene_number']}: {scene['title']}"
    )

    st.markdown("### 📖 Description")
    st.write(scene["description"])

    st.markdown("### 🖼 Image Prompt")
    st.info(scene["image_prompt"])

    st.markdown("### 🎥 Camera Shot")
    st.success(scene["camera_shot"])

    st.markdown("### 🎙 Narration")
    st.write(scene["narration"])

    st.markdown("### 🎵 Background Music")
    st.write(scene["background_music"])

    st.markdown("### 🔊 Sound Effects")

    for effect in scene["sound_effects"]:
        st.write(f"• {effect}")

    st.divider()

    image_key = f"scene_image_{scene['scene_number']}"

    if image_key not in st.session_state:
        st.session_state[image_key] = None

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button(
            "🖼 Generate Image",
            key=f"generate_image_{scene['scene_number']}"
        ):
            with st.spinner("Generating cinematic image..."):
                result = generate_image(scene["image_prompt"])

                if result["status"] == "success":
                    st.session_state[image_key] = result["image_url"]

    with col2:
        if st.button(
            "🗑 Remove Image",
            key=f"remove_image_{scene['scene_number']}"
        ):
            st.session_state[image_key] = None

    if st.session_state[image_key]:

        st.image(
            st.session_state[image_key],
            caption=f"Scene {scene['scene_number']} Visualization",
            use_container_width=True
        )

        with st.expander("📝 Image Prompt Used"):
            st.code(scene["image_prompt"])
