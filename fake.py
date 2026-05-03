import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Inject CSS
st.markdown("""
<style>
/* Background */
.stApp {
    background: url("https://cdn.dribbble.com/users/2170220/screenshots/5978177/news_reading.gif");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

/* Center container */
.main-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* White card */
.card {
    background: rgba(255,255,255,0.95);
    padding: 2.5rem;
    border-radius: 20px;
    width: 100%;
    max-width: 600px;
    text-align: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* Title */
.title {
    font-size: 34px;
    font-weight: bold;
    color: #222;
    margin-bottom: 10px;
}

/* Description */
.desc {
    font-size: 17px;
    color: #555;
    margin-bottom: 25px;
}

/* Input */
.stTextInput > div > input {
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
}

/* Button */
.stButton>button {
    background-color: #2b71ec;
    color: white;
    border-radius: 10px;
    padding: 0.7em;
    font-size: 16px;
    width: 100%;
}

.stButton>button:hover {
    background-color: #164ebc;
}
</style>
""", unsafe_allow_html=True)

# Center layout wrapper
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# Title & description (now perfectly inside box)
st.markdown('<div class="title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Enter a news article to check if it is <b>Fake</b> or <b>Real</b>.</div>', unsafe_allow_html=True)

# Input
news_input = st.text_input("Enter News Article")

# Button
if st.button("Predict"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.error("🚨 This News Article is FAKE")
        else:
            st.success("✅ This News Article is REAL")
    else:
        st.warning("⚠️ Please enter a news article")

# Close divs
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
