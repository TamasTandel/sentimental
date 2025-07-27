import streamlit as st
import sys
import os

# Debug information
st.title("🎭 Emotion Classification App")
st.write("Debug Information:")
st.write(f"Python version: {sys.version}")
st.write(f"Current directory: {os.getcwd()}")
st.write(f"Files in directory: {os.listdir('.')}")

# Test basic functionality
st.header("App Status Check")

try:
    import pickle
    st.success("✅ Pickle import successful")
except ImportError as e:
    st.error(f"❌ Pickle import failed: {e}")

try:
    import pandas as pd
    st.success("✅ Pandas import successful")
except ImportError as e:
    st.error(f"❌ Pandas import failed: {e}")

try:
    import sklearn
    st.success("✅ Scikit-learn import successful")
except ImportError as e:
    st.error(f"❌ Scikit-learn import failed: {e}")

try:
    import nltk
    st.success("✅ NLTK import successful")
except ImportError as e:
    st.error(f"❌ NLTK import failed: {e}")

# Check if model files exist
model_files = ['logistic_model_bow.pkl', 'bow_vectorizer.pkl', 'emotion_mapping.pkl']
for file in model_files:
    if os.path.exists(file):
        st.success(f"✅ {file} found")
    else:
        st.error(f"❌ {file} not found")

st.header("Simple Text Input Test")
user_input = st.text_input("Enter some text:", "This is a test")
if user_input:
    st.write(f"You entered: {user_input}")
    st.write(f"Text length: {len(user_input)}")
