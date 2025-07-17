import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Inject CSS
st.markdown("""
    <style>
    /* Background GIF */
    .stApp {
        background: url("https://cdn.dribbble.com/users/2170220/screenshots/5978177/news_reading.gif");
        background-size: contain;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center bottom;
        background-color: #ff6f5e; /* fallback color */
    }

    /* Fixed white content card */
    .fixed-content {
        position: fixed;
        top: 60px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        max-width: 600px;
        width: 90%;
        z-index: 100;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }

    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #222;
        margin-bottom: 10px;
    }

    .desc {
        text-align: center;
        color: #444;
        font-size: 18px;
        margin-bottom: 30px;
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

# Content Block (fixed at top center)
st.markdown('<div class="fixed-content">', unsafe_allow_html=True)

# Title and description
st.markdown('<div class="main-title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Enter a news article to check if it is <strong>Fake</strong> or <strong>Real</strong>.</div>', unsafe_allow_html=True)

# Input field
news_input = st.text_input("News Article")

# Predict button
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

# Close content block
st.markdown('</div>', unsafe_allow_html=True)
