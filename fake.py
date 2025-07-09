import streamlit as st
import joblib

# Load model and vectorizer
vectorizer = joblib.load('vectorizer.jb')
model = joblib.load('model.jb')

# Streamlit app UI
st.title('📰 Fake News Detector')
st.write("Enter a news article below to check whether it is **fake** or **real**.")

# Input from user
news_input = st.text_input("📝 News Article:")

# Predict button
if st.button("Predict"):
    if news_input.strip():
        # Transform input (must be in a list)
        transform_input = vectorizer.transform([news_input])
        prediction = model.predict(transform_input)

        # Show result
        if prediction[0] == 1:
            st.error("🚨 This News Article is **FAKE**.")
        else:
            st.success("✅ This News Article is **REAL**.")
    else:
        st.warning("⚠️ Please enter a news article.")
