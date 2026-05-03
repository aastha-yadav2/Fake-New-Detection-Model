import streamlit as st
import joblib
import base64

# 🔹 Convert image to base64
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# 🔹 Load background image
bg_image = get_base64("bg.png")

# 🔹 Load model
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# 🔹 CSS (ALL INSIDE ONE BLOCK)
st.markdown(f"""
<style>

.stApp {{
    background: url("data:image/png;base64,{bg_image}") no-repeat center center fixed;
    background-size: cover;
}}

.fixed-content {{
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
}}

.main-title {{
    font-size: 36px;
    font-weight: bold;
    text-align: center;
}}

.desc {{
    text-align: center;
    margin-bottom: 20px;
}}

</style>
""", unsafe_allow_html=True)

# 🔹 UI
st.markdown('<div class="fixed-content">', unsafe_allow_html=True)

st.markdown('<div class="main-title">📰 Fake News Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="desc">Enter news to check if it is <b>Fake</b> or <b>Real</b>.</div>', unsafe_allow_html=True)

news_input = st.text_input("News Article")

if st.button("Predict"):
    if news_input.strip():
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.error("🚨 FAKE NEWS")
        else:
            st.success("✅ REAL NEWS")
    else:
        st.warning("⚠️ Enter some text")

st.markdown('</div>', unsafe_allow_html=True)
