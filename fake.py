import streamlit as st
import joblib
import base64

# ---------------------------
# 🔹 Function: Convert image to base64
# ---------------------------
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 🔹 Load background image (make sure bg.png exists)
bg_image = get_base64("bg.png")

# ---------------------------
# 🔹 Load model
# ---------------------------
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# ---------------------------
# 🔹 CSS Styling
# ---------------------------
st.markdown(f"""
<style>

/* 🔹 Background Image */
.stApp {{
    background: url("data:image/png;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}}

/* 🔹 Blur overlay for readability */
.stApp::before {{
    content: "";
    position: fixed;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(3px);
}}

/* 🔹 Center Container */
.main-container {{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}}

/* 🔹 White Card */
.card {{
    background-color: rgba(255,255,255,0.95);
    padding: 2rem;
    border-radius: 20px;
    max-width: 600px;
    width: 90%;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}}

/* 🔹 Title */
.title {{
    font-size: 34px;
    font-weight: bold;
    color: #222;
    margin-bottom: 10px;
}}

/* 🔹 Description */
.desc {{
    font-size: 17px;
    color: #555;
    margin-bottom: 25px;
}}

/* 🔹 Input */
.stTextInput > div > input {{
    border: 2px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    font-size: 16px;
}}

/* 🔹 Button */
.stButton>button {{
    background-color: #2b71ec;
    color: white;
    padding: 0.6em;
    border-radius: 10px;
    font-size: 16px;
    width: 100%;
}}

.stButton>button:hover {{
    background-color: #164ebc;
}}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# 🔹 UI Layout
# ---------------------------
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)

# Title
st.markdown('<div class="title">📰 Fake News Detector</div>', unsafe_allow_html=True)

# Description
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
