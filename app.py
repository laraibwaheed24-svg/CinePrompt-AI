import streamlit as st
from modules.story_generator import generate_story
from utils.parser import parse_story

def set_page_config():
    """Set page configuration"""
    st.set_page_config(
        page_title="CinePrompt AI",
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def set_custom_css():
    """Set custom CSS styles"""
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

def set_sidebar():
    """Set sidebar configuration"""
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

def set_hero_section():
    """Set hero section"""
    st.markdown(
        "<div class='main-title'>🎬 CinePrompt AI</div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div class='subtitle'>Transform Your Imagination into Cinematic AI Videos</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")

def set_prompt_box():
    """Set prompt box"""
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

def generate_story(prompt):
    # TO DO: implement story generation logic
    pass

def parse_story(story):
    # TO DO: implement story parsing logic
    pass

def set_feature_cards():
    """Set feature cards"""
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

def set_about_section():
    """Set about section"""
    st.header("🚀 About CinePrompt AI")
    st.write("""
    CinePrompt AI is an AI-powered platform that transforms text prompts
    into cinematic videos using story generation, AI images, narration,
    background music, subtitles, and video rendering.
    """)

def set_footer():
    """Set footer"""
    st.markdown(
        "<div class='footer'>Made with ❤️ using Python & Streamlit</div>",
        unsafe_allow_html=True
    )

def main():
    set_page_config()
    set_custom_css()
    set_sidebar()
    set_hero_section()
    prompt, generate = set_prompt_box()
    if generate:
        if prompt.strip() == "":
            st.warning("Please enter a prompt first.")
        else:
            with st.spinner("Creating cinematic story..."):
                story = generate_story(prompt)
            st.success("Story Generated!")
            movie = parse_story(story)
            st.success("Movie Created!")
            st.header(movie["title"])
            col1, col2, col3 = st.columns(3)
            col1.metric("🎭 Genre", movie["genre"])
            col2.metric("⏱ Duration", movie["duration"])
            col3.metric("🎬 Scenes", len(movie["scenes"]))
            st.markdown("---")
            for i, scene in enumerate(movie["scenes"], start=1):
                with st.expander(f"🎥 Scene {i}: {scene['title']}"):
                    st.write(scene["description"])
    set_feature_cards()
    set_about_section()
    set_footer()

if __name__ == "__main__":
    main()
