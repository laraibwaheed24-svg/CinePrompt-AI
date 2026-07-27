import streamlit as st
from modules.story_generator import generate_story
from utils.parser import parse_story

# Page Configuration
st.set_page_config(
    page_title="CinePrompt AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
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

# Sidebar
def render_sidebar():
    st.sidebar.title("🎬 CinePrompt AI")
    st.sidebar.success("Version 1.0")
    st.sidebar.markdown("---")
    st.sidebar.info(
        """
        **Development Progress**

        ✅ Project Setup

        ⏳ Story Generator

        ⏳ Storyboard

        ⏳ Image Generator

        ⏳ Narration

        ⏳ Video Rendering
        """
    )

render_sidebar()

# Hero Section
def render_hero_section():
    st.markdown(
        "<div class='main-title'>🎬 CinePrompt AI</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div class='subtitle'>Transform Your Imagination into Cinematic AI Videos</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")

render_hero_section()

# Prompt Box
def render_prompt_box():
    prompt = st.text_area(
        "✨ Enter Your Story Idea",
        height=150,
        placeholder="Example: A lone astronaut discovers an abandoned city on Mars..."
    )
    generate = st.button(
        "🎬 Generate Story",
        use_container_width=True
    )
    return prompt, generate

prompt, generate = render_prompt_box()

# Story Generation
def generate_and_display_story(prompt):
    if prompt.strip():
        with st.spinner("Creating cinematic story..."):
            try:
                story = generate_story(prompt)
                st.success("Story Generated!")
                st.text_area("Generated Story", story, height=500)
            except Exception as e:
                st.error(f"Error generating story: {e}")
    else:
        st.warning("Please enter a prompt first.")

if generate:
    generate_and_display_story(prompt)

# Feature Cards
def render_feature_cards():
    col1, col2, col3 = st.columns(3)
    features = [
        {"title": "📖 Story Generation", "description": "Generate engaging stories from a single prompt."},
        {"title": "🎨 AI Images", "description": "Create cinematic visuals for every scene."},
        {"title": "🎥 Video Creation", "description": "Turn scenes into a fully narrated movie."},
    ]
    for col, feature in zip([col1, col2, col3], features):
        with col:
            st.markdown(
                f"""
                <div class="feature-box">
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.markdown("---")

render_feature_cards()

# About
def render_about_section():
    st.header("🚀 About CinePrompt AI")
    st.write("""
    CinePrompt AI is an AI-powered platform that transforms text prompts
    into cinematic videos using story generation, AI images, narration,
    background music, subtitles, and video rendering.
    """)

render_about_section()

# Footer
def render_footer():
    st.markdown(
        "<div class='footer'>Made with ❤️ using Python & Streamlit</div>",
        unsafe_allow_html=True
    )

render_footer()
