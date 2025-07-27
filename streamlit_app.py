import streamlit as st
import pickle
import pandas as pd
import string

# Set page config
st.set_page_config(
    page_title="Emotion Classification App",
    page_icon="🎭",
    layout="wide"
)

# Simple stopwords list (no NLTK dependency issues)
STOPWORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours',
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does',
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until',
    'while', 'of', 'at', 'by', 'for', 'with', 'through', 'during', 'before', 'after',
    'above', 'below', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again',
    'further', 'then', 'once'
}

# Load model components
@st.cache_resource
def load_model_components():
    try:
        with open("logistic_model_bow.pkl", "rb") as f:
            model = pickle.load(f)
        
        with open("bow_vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        
        with open("emotion_mapping.pkl", "rb") as f:
            emotion_mapping = pickle.load(f)
        
        return model, vectorizer, emotion_mapping
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None, None

# Text preprocessing function
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in STOPWORDS]
    
    return ' '.join(words)

# Main app
def main():
    st.title("🎭 Emotion Classification App")
    
    # Sidebar with model information
    with st.sidebar:
        st.header("📊 Model Information")
        st.markdown("""
        **Model Details:**
        - Algorithm: Logistic Regression
        - Vectorizer: Bag of Words (CountVectorizer)
        - Accuracy: 88.9%
        - Emotions: sadness, anger, love, surprise, fear, joy
        """)
    
    # Load model components
    model, vectorizer, emotion_mapping = load_model_components()
    
    if model is None:
        st.error("Failed to load model components. Please check if all .pkl files are available.")
        return
    
    # Create main content area
    st.header("📝 Enter Text for Emotion Classification")
    
    # Text input
    st.write("Type your text here:")
    user_text = st.text_area(
        "",
        placeholder="Example: I feel so happy today because the weather is beautiful!",
        height=100,
        key="user_input"
    )
    
    # Classify button
    if st.button("🔍 Classify Emotion", type="primary"):
        if user_text.strip():
            try:
                # Preprocess the text
                processed_text = preprocess_text(user_text)
                
                # Vectorize the text
                text_vector = vectorizer.transform([processed_text])
                
                # Get prediction and probabilities
                prediction = model.predict(text_vector)[0]
                probabilities = model.predict_proba(text_vector)[0]
                
                # Get emotion name
                emotion = emotion_mapping[prediction]
                confidence = max(probabilities) * 100
                
                # Display results
                st.success(f"**Predicted Emotion: {emotion.title()} ({confidence:.1f}% confidence)**")
                
                # Show probability distribution
                st.subheader("📊 Probability Distribution")
                prob_df = pd.DataFrame({
                    'Emotion': [emotion_mapping[i].title() for i in range(len(probabilities))],
                    'Probability': probabilities
                }).sort_values('Probability', ascending=False)
                
                st.bar_chart(prob_df.set_index('Emotion'))
                
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.warning("Please enter some text to classify!")
    
    # Footer
    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit | Model Accuracy: 88.9%")

if __name__ == "__main__":
    main()
