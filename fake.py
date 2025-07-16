import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Inject CSS with glowing animation
st.markdown("""
    <style>
    /* Background GIF */
    .stApp {
        background: url("https://cdn.dribbble.com/users/2170220/screenshots/5978177/news_reading.gif");
        background-size: contain;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center bottom;
        background-color: #ff6f5e;
    }

    /* Title Strip */
    .title-strip {
        position: fixed;
        top: 40px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px 30px;
        border-radius: 15px;
        width: 90%;
        max-width: 700px;
        text-align: center;
        z-index: 100;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .main-title {
        font-size: 36px;
        font-weight: bold;
        color: #222;
        margin-bottom: 10px;
        animation: glow 1.5s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from {
            text-shadow: 0 0 10px #2b71ec, 0 0 20px #2b71ec, 0 0 30px #2b71ec;
        }
        to {
            text-shadow: 0 0 20px #174ac5, 0 0 30px #174ac5, 0 0 40px #174ac5;
        }
    }

    .desc {
        font-size: 18px;
        color: #444;
    }

    /* Input Section */
    .input-section {
        margin-top: 220px;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 15px;
        max-width: 700px;
        width: 90%;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }

    .stTextInput > div > input {
        border: 2px solid #ccc;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        width: 100%;
    }

    .stButton>button {
        background-color: #2b71ec;
        color: white;
        padding: 0.6em 2em;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        transition: 0.3s;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #164ebc;
    }
    </style>
""", unsafe_allow_html=True)

# Glowing Title Section
st.markdown('<div class="title-strip">', unsafe_allow_html=True)
st.markdown('<div class="main-title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Enter a news article to check if it is <strong>Fake</strong> or <strong>Real</strong>.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Input Section Below
st.markdown('<div class="input-section">', unsafe_allow_html=True)

news_input = st.text_input("News Article")

if st.button("Predict"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)
        if prediction[0] == 1:
            st.error("🚨 This News Article is **FAKE**.")
        else:
            st.success("✅ This News Article is **REAL**.")
    else:
        st.warning("⚠️ Please enter a news article.")

st.markdown('</div>', unsafe_allow_html=True)
