import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="DRX Academy",
    page_icon="✨",
    layout="wide"
)

# Initialize session states
if 'step' not in st.session_state:
    st.session_state.step = 'landing'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Sleek Dark Theme + Mandala/Flower Corner Animation Styling
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background: linear-gradient(135deg, #040d1a 0%, #01060c 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Mandala / Flower Corner Graphic Effect */
    .mandala-flower {
        position: fixed;
        right: -40px;
        top: -40px;
        width: 380px;
        height: 380px;
        background: radial-gradient(circle, rgba(212,175,55,0.2) 0%, rgba(0,210,255,0.05) 50%, transparent 70%);
        border: 2px dashed rgba(212,175,55,0.4);
        border-radius: 50% 30% 50% 30%;
        animation: rotateFlower 20s linear infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes rotateFlower {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .hero-title {
        font-family: 'Cinzel', serif !important;
        font-size: 42px !important;
        font-weight: 700 !important;
        color: #ffffff;
        margin-bottom: 15px;
    }
    
    .hero-title span {
        color: #00d2ff;
    }

    .stButton>button {
        background: linear-gradient(90deg, #00d2ff, #0077ff);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 0 15px rgba(0,210,255,0.3);
        transition: 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(0,210,255,0.7);
    }
    </style>
    <div class="mandala-flower"></div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 1. LANDING PAGE
# ---------------------------------------------------------
if st.session_state.step == 'landing':
    col1, col2 = st.columns([1.2, 0.8])
    
    with col1:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown('<p class="hero-title">STUDY DEEPLY. <span>UNDERSTAND FULLY.</span></p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #8892b0; font-size: 15px; margin-bottom: 25px;">Turn complex chapters and debugging errors into clear lessons powered by Meta Llama.</p>', unsafe_allow_html=True)
        
        if st.button("Start learning →"):
            st.session_state.step = 'auth'
            st.rerun()
            
    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        st.markdown("""
            <div style="background: rgba(10,25,47,0.8); border: 1px solid rgba(0,210,255,0.2); padding: 20px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                <span style="font-size: 11px; color: #00d2ff; text-transform: uppercase; letter-spacing: 1px;">Live Preview</span>
                <h4 style="color: white; margin-top: 5px;">AI Study & Debug Assistant</h4>
                <p style="color: #8892b0; font-size: 13px;">Real-time concept breakdown with mandala aesthetic theme.</p>
                <div style="background: rgba(0,210,255,0.1); padding: 8px 12px; border-radius: 6px; font-size: 12px; color: #64ffda; margin-top: 10px;">
                    ✨ Google & Apple Sign-In Ready
                </div>
            </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. AUTHENTICATION PAGE (Google & Apple Options)
# ---------------------------------------------------------
elif st.session_state.step == 'auth':
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    
    with col2:
        st.markdown('<h2 style="text-align: center; font-family: \'Cinzel\'; color: #00d2ff;">DRX ACADEMY</h2>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; color: #8892b0; font-size: 14px; margin-bottom: 30px;">Choose your sign-in method to continue</p>', unsafe_allow_html=True)
        
        if st.button("🔵 Continue with Google"):
            st.session_state.logged_in = True
            st.session_state.step = 'dashboard'
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("🍎 Continue with Apple"):
            st.session_state.logged_in = True
            st.session_state.step = 'dashboard'
            st.rerun()
            
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("← Back to Home"):
            st.session_state.step = 'landing'
            st.rerun()

# ---------------------------------------------------------
# 3. DASHBOARD PAGE (AI Assistant & Debugging)
# ---------------------------------------------------------
elif st.session_state.step == 'dashboard':
    st.markdown('<p style="font-size: 26px; font-weight: 700;">AI STUDY & <span style="color: #00d2ff;">DEBUG ASSISTANT</span></p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #8892b0; font-size: 14px;">Generate structured notes or debug code instantly.</p>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    topic = st.text_input("Topic or Code to debug", placeholder="e.g. Photosynthesis / Python Bug")
    
    global_languages = [
        "English", "Hindi / हिंदी", "Spanish / Español", "French / Français", 
        "German / Deutsch", "Mandarin / 中文", "Japanese / 日本語", "Arabic / العربية"
    ]
    language = st.selectbox("Lesson language", global_languages)
    
    api_key = st.text_input("Enter OpenRouter API Key (Meta Llama)", type="password", placeholder="sk-or-v1-...")

    if st.button("Generate & Debug ⚡"):
        if not api_key:
            st.warning("Please enter your OpenRouter API key.")
        elif not topic:
            st.warning("Please enter a topic or code snippet.")
        else:
            with st.spinner("Analyzing via Meta Llama..."):
                try:
                    client = OpenAI(
                        base_url="https://openrouter.ai/api/v1",
                        api_key=api_key,
                    )
                    
                    completion = client.chat.completions.create(
                        model="meta-llama/llama-3-8b-instruct",
                        messages=[{
                            "role": "user", 
                            "content": f"Create a structured study guide and debugging breakdown for '{topic}' in {language}. Provide clear sections and simple explanations."
                        }]
                    )
                    
                    response = completion.choices[0].message.content
                    st.success("Generated successfully!")
                    st.markdown(response)
                except Exception as e:
                    st.error(f"Error: {e}")

    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.step = 'landing'
        st.rerun()