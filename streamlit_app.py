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
STOPWORDS = {'a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 'fifteen', 'fifty', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', 'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself', 'yourselves'
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
    
    # Create footer columns for better layout
    footer_col1, footer_col2, footer_col3 = st.columns([1, 2, 1])
    
    with footer_col2:
        st.markdown(
            """
            <div style='text-align: center; padding: 20px;'>
                <p style='margin: 5px 0; font-size: 16px;'>
                    Built with ❤️ using Streamlit | Model Accuracy: 88.9%
                </p>
                <p style='margin: 5px 0; font-size: 14px; color: #666;'>
                    🚀 Developed by <strong><a href="https://www.linkedin.com/in/tamas-tandel-80b857315" target="_blank" style="color: #0066cc; text-decoration: none;">Tamas Tandel</a></strong>
                </p>
                <p style='margin: 5px 0; font-size: 12px; color: #888;'>
                    Machine Learning • Natural Language Processing • Emotion Classification
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()
