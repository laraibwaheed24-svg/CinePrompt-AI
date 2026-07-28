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

    if st.button(
        "🖼 Generate Image",
        key=f"generate_image_{scene['scene_number']}"
    ):
        result = generate_image(scene["image_prompt"])

        if result["status"] == "success":
            st.image(
                result["image_url"],
                caption="AI Image Preview",
                use_container_width=True
            )

            with st.expander("📝 Prompt Used"):
                st.code(result["prompt"])
    
