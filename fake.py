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
        background: url("https://cdn.dribbble.com/users/177029/screenshots/3321306/news.gif");
        background-size: cover;
        background-attachment: fixed;
        background-position: center bottom;
        background-repeat: no-repeat;
    }

    /* Make content fixed at top center */
    .fixed-content {
        position: fixed;
        top: 50px;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.85);
        padding: 30px;
        border-radius: 15px;
        max-width: 800px;
        width: 90%;
        z-index: 100;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }

    .main-title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #222;
    }

    .desc {
        text-align: center;
        color: #444;
        margin-bottom: 20px;
        font-size: 18px;
    }

    .stTextInput > div > input {
        border: 2px solid #bbb;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }

    .stButton>button {
        background-color: #008CBA;
        color: white;
        padding: 0.6em 2em;
        border: none;
        border-radius: 10px;
        font-size: 16px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #005f75;
    }
    </style>
""", unsafe_allow_html=True)

# Fixed content wrapper
st.markdown('<div class="fixed-content">', unsafe_allow_html=True)

st.markdown('<div class="main-title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Enter a news article to check if it is <strong>Fake</strong> or <strong>Real</strong>.</div>', unsafe_allow_html=True)

# Input field
news_input = st.text_input("📝 News Article:")

# Predict button
if st.button("🔍 Predict"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.error("🚨 This News Article is **FAKE**.")
        else:
            st.success("✅ This News Article is **REAL**.")
    else:
        st.warning("⚠️ Please enter a news article.")

# Close fixed content wrapper
st.markdown('</div>', unsafe_allow_html=True)
