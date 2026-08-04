import streamlit as st
from modules.image_generator import generate_image
from modules.narration_generator import generate_narration


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

    edited_prompt = st.text_area(
        "Edit image prompt",
        value=scene["image_prompt"],
        height=120,
        key=f"prompt_{scene['scene_number']}",
        label_visibility="collapsed"
    )

    st.markdown("### 🎥 Camera Shot")
    st.success(scene["camera_shot"])

    st.markdown("### 🎙 Narration")
    st.write(scene["narration"])

    st.markdown("### 🎵 Background Music")
    st.write(scene["background_music"])

    st.markdown("### 🔊 Sound Effects")

    for effect in scene["sound_effects"]:
        st.write(f"• {effect}")

 
    st.markdown("### 🎬 Director Controls")

    col1, col2 = st.columns(2)

    with col1:
        camera = st.selectbox(
            "Camera",
            [
                "Wide Shot",
                "Close-Up",
                "Medium Shot",
                "Tracking Shot",
                "Aerial Shot",
            ],
            key=f"camera_{scene['scene_number']}",
        )

        lighting = st.selectbox(
            "Lighting",
            [
                "Golden Hour",
                "Studio",
                "Moonlight",
                "Soft Light",
                "Dramatic",
            ],
            key=f"light_{scene['scene_number']}",
        )

    with col2:
        style = st.selectbox(
            "Art Style",
            [
                "Cinematic",
                "Realistic",
                "Anime",
                "Pixar",
                "Ghibli",
            ],
            key=f"style_{scene['scene_number']}",
        )

        weather = st.selectbox(
            "Weather",
            [
                "Clear",
                "Rain",
                "Snow",
                "Fog",
                "Storm",
            ],
            key=f"weather_{scene['scene_number']}",
        )

    

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
                enhanced_prompt = (
                    f"{edited_prompt}\n\n"
                    f"Style: {style}\n"
                    f"Camera: {camera}\n"
                    f"Lighting: {lighting}\n"
                    f"Weather: {weather}\n\n"
                    "Ultra realistic, masterpiece, cinematic lighting, "
                    "high detail, movie still, 8K quality."
                ).strip()

                result = generate_image(enhanced_prompt)
                st.write(result)
                st.write(result["image_url"])
                

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
            st.code(edited_prompt)

    
# ==========================
# AI Narration
# ==========================

    st.divider()

    audio_key = f"scene_audio_{scene['scene_number']}"

    if audio_key not in st.session_state:
        st.session_state[audio_key] = None

    if st.button(
        "🎙 Generate Narration",
        key=f"voice_{scene['scene_number']}"
    ):

        with st.spinner("Generating AI narration..."):

            audio_file = generate_narration(
                scene["narration"]
            )

            st.session_state[audio_key] = audio_file


    if st.session_state[audio_key]:

        st.audio(st.session_state[audio_key])
