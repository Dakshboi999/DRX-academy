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
    st.session_state.step = 'login'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_email' not in st.session_state:
    st.session_state.user_email = ""
if 'theme' not in st.session_state:
    st.session_state.theme = 'Dark Blue & Black'

# Theme Selector in Sidebar
st.sidebar.title("Appearance")
theme_choice = st.sidebar.selectbox("Choose Theme", ["Dark Blue & Black", "Evening Warmth (Light)"], key="theme_select")
st.session_state.theme = theme_choice

# Dynamic styling variables based on theme selection
if st.session_state.theme == 'Dark Blue & Black':
    bg_gradient = "linear-gradient(135deg, #020916 0%, #05162e 50%, #010409 100%)"
    text_color = "#ffffff"
    card_bg = "rgba(2, 12, 27, 0.8)"
    accent_color = "#00d2ff"
else:
    bg_gradient = "linear-gradient(135deg, #fdfbfb 0%, #ebedee 50%, #f4d03f 100%)"
    text_color = "#2c3e50"
    card_bg = "rgba(255, 255, 255, 0.9)"
    accent_color = "#d35400"

# Corrected f-string with properly escaped CSS brackets ({{ and }})
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg_gradient};
        color: {text_color};
        font-family: 'Poppins', sans-serif;
    }}
    
    .golden-floral-bg {{
        position: fixed;
        right: -50px;
        top: -50px;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, rgba(212,175,55,0.25) 0%, rgba(212,175,55,0.05) 50%, transparent 70%);
        border: 2px dashed rgba(212,175,55,0.4);
        border-radius: 40% 60% 50% 50%;
        pointer-events: none;
        z-index: 1;
    }}

    .main-header {{
        font-size: 38px !important;
        font-weight: 800 !important;
        color: {accent_color} !important;
        text-align: center;
        letter-spacing: 2px;
        margin-bottom: 5px;
        text-shadow: 0 0 20px rgba(0,210,255,0.4);
    }}
    
    .sub-header {{
        font-size: 14px !important;
        color: #d4af37 !important;
        text-align: center;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 30px;
    }}

    .stTextInput>div>div>input {{
        background-color: {card_bg};
        color: {text_color};
        border: 1px solid rgba(212, 175, 55, 0.5);
        border-radius: 8px;
    }}

    .stButton>button {{
        background: linear-gradient(90deg, {accent_color}, #d4af37);
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
        padding: 12px;
        border: 1px solid rgba(255,255,255,0.3);
        box-shadow: 0 0 15px rgba(212,175,55,0.3);
    }}
    
    .footer-text {{
        text-align: center;
        color: {text_color};
        opacity: 0.7;
        font-size: 12px;
        margin-top: 40px;
    }}
    </style>
    <div class="golden-floral-bg"></div>
""", unsafe_allow_html=True)

# Step 1: Main Login / Register Choice
if st.session_state.step == 'login':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="main-header">DRX</p>', unsafe_allow_html=True)
    st.markdown('<p class="main-header" style="margin-top:-20px;">ACADEMY</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Excellence in Learning</p>', unsafe_allow_html=True)
    
    if st.button("LOGIN", key="btn_main_login"):
        st.session_state.step = 'login_form'
        st.rerun()
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("REGISTER", key="btn_main_register"):
        st.session_state.step = 'register_form'
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown('<div class="footer-text">DRX Academy, All Rights Reserved</div>', unsafe_allow_html=True)

# Step 1.1: Login Form View
elif st.session_state.step == 'login_form':
    st.markdown('<p class="main-header" style="font-size:28px !important;">LOGIN</p>', unsafe_allow_html=True)
    
    email = st.text_input("Username/Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("SUBMIT LOGIN", key="btn_submit_login"):
        if email and password:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.step = 'dashboard'
            st.success("Login Successful!")
            st.rerun()
        else:
            st.warning("Please fill all details.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Forgot Password?", key="btn_forgot"):
        st.success("Password reset instructions sent!")
        
    if st.button("Back", key="btn_back_login"):
        st.session_state.step = 'login'
        st.rerun()

# Step 1.2: Register Form View
elif st.session_state.step == 'register_form':
    st.markdown('<p class="main-header" style="font-size:28px !important;">REGISTER</p>', unsafe_allow_html=True)
    
    reg_email = st.text_input("Username/Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("CREATE ACCOUNT", key="btn_submit_reg"):
        if reg_email and reg_password:
            st.success("Account created successfully! Please login.")
            st.session_state.step = 'login'
            st.rerun()
        else:
            st.warning("Please fill all fields.")
            
    if st.button("Back", key="btn_back_reg"):
        st.session_state.step = 'login'
        st.rerun()

# Step 2: AI Dashboard View
elif st.session_state.step == 'dashboard':
    st.markdown('<p class="main-header">DRX DASHBOARD</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">Welcome: {st.session_state.user_email}</p>', unsafe_allow_html=True)
    
    global_languages = [
        "English", "Hindi / हिंदी", "Spanish / Español", "French / Français", 
        "Arabic / العربية", "German / Deutsch", "Japanese / 日本語"
    ]
    
    language = st.selectbox("Select Language", global_languages, key="dash_lang")
    topic = st.text_input("Enter your topic or chapter name:", key="dash_topic")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("GENERATE STUDY MATERIAL", key="btn_gen"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating summary via Meta Llama..."):
                try:
                    api_key = st.secrets["OPENROUTER_API_KEY"]
                    client = OpenAI(
                        base_url="https://openrouter.ai/api/v1",
                        api_key=api_key,
                    )
                    
                    completion = client.chat.completions.create(
                        model="meta-llama/llama-3-8b-instruct",
                        messages=[{
                            "role": "user", 
                            "content": f"Explain '{topic}' in {language} with a simple summary and an everyday analogy."
                        }]
                    )
                    
                    response = completion.choices[0].message.content
                    st.success("Here is your breakdown!")
                    st.write(response)
                except Exception as e:
                    st.error("Connection error with AI secrets.")
            
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Logout", key="btn_logout"):
        st.session_state.step = 'login'
        st.rerun()