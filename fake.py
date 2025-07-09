import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        color: #4a4a4a;
    }
    .desc {
        text-align: center;
        color: #6e6e6e;
        margin-bottom: 30px;
    }
    .stTextInput > div > input {
        border: 2px solid #ddd;
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

# Streamlit UI
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
