import streamlit as st
from modules.story_generator import generate_story
from utils.parser import parse_story
from components.scene_card import display_scene
from components.movie_header import display_movie_header
from components.sidebar import display_sidebar
from modules.image_generator import generate_image

if "movie" not in st.session_state:
    st.session_state.movie = None

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CinePrompt AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main-title{
    font-size:50px;
    font-weight:bold;
    color:#FFD700;
    text-align:center;
}

.subtitle{
    font-size:22px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.feature-box{
    background-color:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border:1px solid #333333;
    text-align:center;
    height:180px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

display_sidebar()


# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    "<div class='main-title'>🎬 CinePrompt AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Transform Your Imagination into Cinematic AI Videos</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# Prompt Box
# -----------------------------
prompt = st.text_area(
    "✨ Enter Your Story Idea",
    height=150,
    placeholder="Example: A lone astronaut discovers an abandoned city on Mars..."
)

generate = st.button(
    "🎬 Generate Story",
    use_container_width=True
)


if generate and prompt.strip():
    with st.spinner("Creating cinematic story..."):
        try:
            story = generate_story(prompt)
            st.json(story)

            st.success("Story Generated!")


            import json

            st.session_state.movie = story

            display_movie_header(movie)
            
            st.write(movie["summary"])

            st.markdown("---")

            for scene in movie["scenes"]:
                display_scene(scene)

        except Exception as e:
            st.error(f"Error generating story: {e}")

elif not prompt.strip():
    st.warning("Please enter a prompt first.")
# -----------------------------
# Feature Cards
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>📖 Story Generation</h3>
    <p>Generate engaging stories from a single prompt.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>🎨 AI Images</h3>
    <p>Create cinematic visuals for every scene.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>🎥 Video Creation</h3>
    <p>Turn scenes into a fully narrated movie.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# About
# -----------------------------
st.header("🚀 About CinePrompt AI")

st.write("""
CinePrompt AI is an AI-powered platform that transforms text prompts
into cinematic videos using story generation, AI images, narration,
background music, subtitles, and video rendering.
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    "<div class='footer'>Made with ❤️ using Python & Streamlit</div>",
    unsafe_allow_html=True
)
