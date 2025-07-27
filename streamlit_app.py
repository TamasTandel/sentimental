import streamlit as st
import pickle
import pandas as pd
import string
import warnings
warnings.filterwarnings("ignore")

# Set page config first
st.set_page_config(
    page_title="Emotion Classification App",
    page_icon="🎭",
    layout="wide"
)

# Try to import nltk and handle the download
try:
    import nltk
    from nltk.corpus import stopwords
    
    # Download required NLTK data
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        with st.spinner("Downloading NLTK data..."):
            nltk.download('punkt', quiet=True)
    
    try:
        nltk.data.find('corpora/stopwords')
    except LookupError:
        with st.spinner("Downloading NLTK data..."):
            nltk.download('stopwords', quiet=True)
            
except ImportError:
    st.error("NLTK not available. Please install nltk package.")
    st.stop()

# Load the model, vectorizer, and emotion mapping
@st.cache_resource
def load_model_components():
    try:
        # Load the logistic regression model
        with open("logistic_model_bow.pkl", "rb") as f:
            model = pickle.load(f)
        
        # Load the vectorizer
        with open("bow_vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        
        # Load emotion mapping
        with open("emotion_mapping.pkl", "rb") as f:
            emotion_mapping = pickle.load(f)
        
        return model, vectorizer, emotion_mapping
    except FileNotFoundError as e:
        st.error(f"Model files not found: {e}")
        st.error("Please make sure all .pkl files are in the repository.")
        return None, None, None
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None

# Text preprocessing functions (same as in training)
def remove_punc(txt):
    return txt.translate(str.maketrans('', '', string.punctuation))

def remove_numbers(txt):
    new = ''
    for i in txt:
        if not i.isdigit():
            new = new + i
    return new

def remove_emojis(txt):
    new = ''
    for i in txt:
        if i.isascii():
            new = new + i
    return new

def remove_stopwords(txt):
    stop_words = set(stopwords.words('english'))
    words = txt.split()
    cleaned = []
    for word in words:
        if word not in stop_words:
            cleaned.append(word)
    return ' '.join(cleaned)

def preprocess_text(text):
    """Apply the same preprocessing steps as used in training"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = remove_punc(text)
    
    # Remove numbers
    text = remove_numbers(text)
    
    # Remove emojis
    text = remove_emojis(text)
    
    # Remove stopwords
    text = remove_stopwords(text)
    
    return text

# Streamlit UI
def main():
    st.set_page_config(
        page_title="Emotion Classification App",
        page_icon="😊",
        layout="wide"
    )
    
    st.title("🎭 Emotion Classification App")
    st.markdown("---")
    
    # Load model components
    model, vectorizer, emotion_mapping = load_model_components()
    
    if model is None:
        st.stop()
    
    # Sidebar with information
    st.sidebar.title("📊 Model Information")
    st.sidebar.info(
        """
        **Model Details:**
        - Algorithm: Logistic Regression
        - Vectorizer: Bag of Words (CountVectorizer)
        - Accuracy: 88.9%
        - Emotions: sadness, anger, love, surprise, fear, joy
        """
    )
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Enter Text for Emotion Classification")
        user_input = st.text_area(
            "Type your text here:",
            placeholder="Example: I feel so happy today because the weather is beautiful!",
            height=150
        )
        
        # Prediction button
        if st.button("🔍 Classify Emotion", type="primary"):
            if user_input.strip():
                with st.spinner("Analyzing emotion..."):
                    # Preprocess the input text
                    processed_text = preprocess_text(user_input)
                    
                    # Transform using the vectorizer
                    text_vectorized = vectorizer.transform([processed_text])
                    
                    # Make prediction
                    prediction = model.predict(text_vectorized)[0]
                    prediction_proba = model.predict_proba(text_vectorized)[0]
                    
                    # Get emotion name
                    emotion = emotion_mapping[prediction]
                    confidence = prediction_proba[prediction] * 100
                    
                    # Display results
                    st.success(f"**Predicted Emotion: {emotion.upper()}** 🎯")
                    st.info(f"**Confidence: {confidence:.2f}%**")
                    
                    # Show all probabilities
                    st.subheader("📈 Emotion Probabilities")
                    prob_data = []
                    for i, prob in enumerate(prediction_proba):
                        prob_data.append({
                            'Emotion': emotion_mapping[i].title(),
                            'Probability': f"{prob*100:.2f}%",
                            'Score': prob
                        })
                    
                    prob_df = pd.DataFrame(prob_data)
                    prob_df = prob_df.sort_values('Score', ascending=False)
                    
                    # Display as a bar chart
                    st.bar_chart(prob_df.set_index('Emotion')['Score'])
                    
                    # Display as a table
                    st.dataframe(prob_df[['Emotion', 'Probability']], hide_index=True)
                    
                    # Show processed text
                    with st.expander("🔧 View Preprocessed Text"):
                        st.text(f"Original: {user_input}")
                        st.text(f"Processed: {processed_text}")
            else:
                st.warning("Please enter some text to classify!")
    
    with col2:
        st.subheader("🎨 Emotion Examples")
        examples = {
            "😢 Sadness": "I feel so lonely and heartbroken today",
            "😠 Anger": "I am furious about this unfair treatment",
            "❤️ Love": "I love spending time with my family",
            "😮 Surprise": "I can't believe this amazing news!",
            "😨 Fear": "I am terrified of heights",
            "😄 Joy": "I feel incredible happiness and excitement"
        }
        
        for emotion, example in examples.items():
            if st.button(f"Try: {emotion}", key=emotion):
                st.query_params.text = example
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
            <p>Built with ❤️ using Streamlit | Model Accuracy: 88.9%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
