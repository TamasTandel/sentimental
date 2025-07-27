import streamlit as st
import pickle
import os

# Basic health check
st.title("🎭 Emotion Classification App")
st.write("App is starting up...")

# Check if model files exist
model_files = ['logistic_model_bow.pkl', 'bow_vectorizer.pkl', 'emotion_mapping.pkl']
all_files_exist = True

st.write("Checking model files:")
for file in model_files:
    if os.path.exists(file):
        st.success(f"✅ {file} found")
    else:
        st.error(f"❌ {file} not found")
        all_files_exist = False

if all_files_exist:
    st.success("All model files are available!")
    
    # Simple text input for testing
    text = st.text_input("Test the app:", "I am happy today")
    if st.button("Test"):
        st.write(f"Input received: {text}")
        st.write("Ready for full deployment!")
else:
    st.error("Some model files are missing. Please check the repository.")
