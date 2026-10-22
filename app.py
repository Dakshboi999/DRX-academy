import streamlit as st

from openai import OpenAI


# Page setup and configuration
st.set_page_config(
    page_title="DRX Academy",
    page_icon="✨",
    layout="centered"
)


# Initialize session state variables
if 'step' not in st.session_state:
    st.session_state.step = 'splash'

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_email' not in st.session_state:
    st.session_state.user_email = ""


# Custom CSS styling and bloom animation (Rendered properly with HTML)
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
    .stApp {
        background: linear-gradient(135deg, #0a192f 0%, #020c1b 50%, #000000 100%);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }
    
    @keyframes bloom {
        0% { transform: scale(0.1) rotate(0deg); opacity: 0; filter: drop-shadow(0 0 2px #00d2ff); }
        50% { opacity: 0.6; }
        100% { transform: scale(1) rotate(360deg); opacity: 0.4; filter: drop-shadow(0 0 20px #00d2ff); }
    }
    
    .flower-bg {
        position: fixed;
        right: -30px;
        top: 15%;
        width: 380px;
        height: 380px;
        border: 3px solid #00d2ff;
        border-radius: 50% 30% 50% 30%;
        animation: bloom 2.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
        z-index: 999;
        pointer-events: none;
        box-shadow: 0 0 30px rgba(0,210,255,0.3);
    }
    
    .main-title {
        font-family: 'Cinzel', serif !important;
        font-size: 42px !important;
        font-weight: bold !important;
        color: #00d2ff !important;
        text-align: center !important;
        text-shadow: 0 0 20px rgba(0,210,255,0.8), 0 0 40px rgba(0,210,255,0.4);
    }
    
    .sub-title {
        color: #64ffda;
        text-align: center;
        margin-bottom: 30px;
        font-size: 15px;
        font-weight: 600;
        letter-spacing: 1px;
    }
    
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #0077ff);
        color: white;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 0 15px rgba(0,210,255,0.5);
    }
    </style>
    <div class="flower-bg"></div>
""", unsafe_allow_html=True)


# Step 1: Splash screen view
if st.session_state.step == 'splash':
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown('<p class="main-title">DRX ACADEMY</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="sub-title">OpenRouter Meta Llama Study Assistant</p>', unsafe_allow_html=True)
    
    st.write("### Welcome to smart learning.")
    
    st.write("Break down complex chapters into simple summaries and analogies.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("GET STARTED", key="btn_get_started"):
        st.session_state.step = 'login'
        st.rerun()


# Step 2: Login and Register interface view
elif st.session_state.step == 'login':
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<p class="main-title">DRX ACADEMY</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="sub-title">Secure Student Login</p>', unsafe_allow_html=True)
    
    email = st.text_input("Username / Email", key="login_email")
    
    password = st.text_input("Password", type="password", key="login_password")
    
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


# Step 3: AI Dashboard view with global languages and OpenRouter Llama
elif st.session_state.step == 'dashboard':
    st.markdown('<p class="main-title">DRX DASHBOARD</p>', unsafe_allow_html=True)
    
    st.markdown(f'<p class="sub-title">Logged in as: {st.session_state.user_email} | Powered by OpenRouter Llama</p>', unsafe_allow_html=True)
    
    api_key = st.text_input("Enter OpenRouter API Key", type="password", key="dash_api_key")
    
    global_languages = [
        "English",
        "Mandarin Chinese / 中文",
        "Spanish / Español",
        "French / Français",
        "Arabic / العربية",
        "Russian / Русский",
        "Hindi / हिंदी",
        "Portuguese / Português",
        "Bengali / বাংলা",
        "German / Deutsch",
        "Japanese / 日本語",
        "Korean / 한국어",
        "Turkish / Türkçe",
        "Italian / Italiano",
        "Vietnamese / Tiếng Việt",
        "Urdu / اردو",
        "Persian / فارسی",
        "Javanese / Basa Jawa",
        "Marathi / मराठी",
        "Telugu / తెలుగు",
        "Tamil / தமிழ்",
        "Gujarati / ગુજરાતી",
        "Polish / Polski",
        "Ukrainian / Українська",
        "Dutch / Nederlands",
        "Greek / Ελληνικά",
        "Swahili / Kiswahili",
        "Thai / ไทย",
        "Malay / Bahasa Melayu"
    ]
    
    language = st.selectbox("Select Global Language", global_languages, key="dash_language")
    
    topic = st.text_input("Enter your complex topic or chapter name (e.g., Photosynthesis):", key="dash_topic")

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