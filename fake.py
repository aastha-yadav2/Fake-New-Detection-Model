import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Inject CSS for background and layout styling
st.markdown("""
    <style>
    .stApp {
        background: url("https://cdn.dribbble.com/users/2170220/screenshots/5978177/news_reading.gif"); /* Replace with hosted GIF URL */
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center bottom;
        background-attachment: fixed;
    }
    .main-container {
        padding-top: 30px;
        padding-bottom: 300px; /* Allow visibility of GIF */
        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
        border-radius: 15px;
        margin: 50px auto;
        width: 90%;
        max-width: 700px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        color: #333;
        margin-bottom: 10px;
    }
    .desc {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
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

# Start main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Title and description
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

# Close main container
st.markdown('</div>', unsafe_allow_html=True)
