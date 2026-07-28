import streamlit as st

st.set_page_config(
    page_title="CinePrompt AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

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


st.markdown(
    "<div class='main-title'>🎬 CinePrompt AI</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Transform Your Imagination into Cinematic AI Videos</div>",
    unsafe_allow_html=True
)

st.markdown("---")


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

st.header("🚀 About CinePrompt AI")

st.write("""
CinePrompt AI is an AI-powered filmmaking platform that transforms
text prompts into cinematic experiences using AI story generation,
visuals, narration, music, and video rendering.
""")


st.markdown(
    "<div class='footer'>Made with ❤️ using Python & Streamlit</div>",
    unsafe_allow_html=True
)
