import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="DRX Academy",
    page_icon="✨",
    layout="centered"
)

# Initialize session states
if 'step' not in st.session_state:
    st.session_state.step = 'splash'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""

# Clean & Bright Professional Styling (No broken HTML/CSS)
st.markdown("""
    <style>
    .main-header {
        font-size: 38px !important;
        font-weight: 800 !important;
        color: #00d2ff !important;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 16px !important;
        color: #a0aec0 !important;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #0077ff);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        padding: 12px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Step 1: Splash Screen
if st.session_state.step == 'splash':
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<p class="main-header">DRX ACADEMY</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Meta Llama-Powered AI Study Assistant</p>', unsafe_allow_html=True)
    
    st.markdown("### Welcome to smart learning.")
    st.write("Break down complex chapters into simple summaries and everyday analogies instantly.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("GET STARTED", key="btn_get_started"):
        st.session_state.step = 'login'
        st.rerun()

# Step 2: Login Interface
elif st.session_state.step == 'login':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="main-header">DRX ACADEMY</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Secure Student Login</p>', unsafe_allow_html=True)
    
    email = st.text_input("Username / Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("LOGIN", key="btn_login"):
            if email and password:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.step = 'dashboard'
                st.success("Login Successful!")
                st.rerun()
            else:
                st.warning("Please enter credentials.")
    with col2:
        if st.button("REGISTER", key="btn_register"):
            st.info("Registration portal is ready.")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Forgot Password?", key="btn_forgot"):
        st.success("Password reset link sent.")

# Step 3: AI Dashboard
elif st.session_state.step == 'dashboard':
    st.markdown('<p class="main-header">DRX DASHBOARD</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">Logged in as: {st.session_state.user_email} | Powered by Meta Llama</p>', unsafe_allow_html=True)
    
    api_key = st.text_input("Enter OpenRouter API Key", type="password", key="dash_api_key")
    
    global_languages = [
        "English", "Mandarin Chinese / 中文", "Spanish / Español", "French / Français", 
        "Arabic / العربية", "Russian / Русский", "Hindi / हिंदी", "Portuguese / Português", 
        "Bengali / বাংলা", "German / Deutsch", "Japanese / 日本語", "Korean / 한국어", 
        "Turkish / Türkçe", "Italian / Italiano", "Vietnamese / Tiếng Việt", "Urdu / اردو"
    ]
    
    language = st.selectbox("Select Global Language", global_languages, key="dash_language")
    topic = st.text_input("Enter your complex topic or chapter name (e.g., Photosynthesis):", key="dash_topic")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("GENERATE STUDY MATERIAL", key="btn_generate"):
        if not api_key:
            st.warning("Please enter your OpenRouter API key first.")
        elif not topic:
            st.warning("Please enter a topic.")
        else:
            with st.spinner("OpenRouter Llama AI is simplifying your topic..."):
                try:
                    client = OpenAI(
                        base_url="https://openrouter.ai/api/v1",
                        api_key=api_key,
                    )
                    
                    completion = client.chat.completions.create(
                        model="meta-llama/llama-3-8b-instruct",
                        messages=[
                            {
                                "role": "user", 
                                "content": f"Explain the topic '{topic}' in {language} with a simple summary and an everyday analogy."
                            }
                        ]
                    )
                    
                    response = completion.choices[0].message.content
                    st.success("Here is your breakdown!")
                    st.write(response)
                    
                except Exception as e:
                    st.error(f"Error: {e}")
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Logout", key="btn_logout"):
        st.session_state.step = 'splash'
        st.session_state.logged_in = False
        st.rerun()