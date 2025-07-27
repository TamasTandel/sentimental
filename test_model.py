#!/usr/bin/env python3
"""
Simple script to test the emotion classification model
"""

import pickle
import string
from nltk.corpus import stopwords
import nltk

# Download required NLTK data if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Load model components
def load_model_components():
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

# Text preprocessing functions
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

def predict_emotion(text, model, vectorizer, emotion_mapping):
    """Predict emotion for given text"""
    # Preprocess the input text
    processed_text = preprocess_text(text)
    
    # Transform using the vectorizer
    text_vectorized = vectorizer.transform([processed_text])
    
    # Make prediction
    prediction = model.predict(text_vectorized)[0]
    prediction_proba = model.predict_proba(text_vectorized)[0]
    
    # Get emotion name
    emotion = emotion_mapping[prediction]
    confidence = prediction_proba[prediction] * 100
    
    return emotion, confidence, prediction_proba

def main():
    print("🎭 Emotion Classification Model Test")
    print("=" * 40)
    
    # Load model components
    try:
        model, vectorizer, emotion_mapping = load_model_components()
        print("✅ Model loaded successfully!")
        print(f"📊 Available emotions: {list(emotion_mapping.values())}")
        print()
    except FileNotFoundError as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Test with sample texts
    test_texts = [
        "I feel so happy and excited today!",
        "I am really angry about this situation",
        "I love spending time with my family",
        "This is a shocking and surprising news",
        "I am terrified of what might happen",
        "I feel so sad and lonely"
    ]
    
    print("🔍 Testing with sample texts:")
    print("-" * 40)
    
    for i, text in enumerate(test_texts, 1):
        emotion, confidence, probs = predict_emotion(text, model, vectorizer, emotion_mapping)
        print(f"{i}. Text: '{text}'")
        print(f"   Predicted Emotion: {emotion.upper()} ({confidence:.1f}% confidence)")
        print()
    
    # Interactive mode
    print("💬 Interactive Mode (type 'quit' to exit)")
    print("-" * 40)
    
    while True:
        user_input = input("\nEnter text to classify: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not user_input:
            print("⚠️  Please enter some text!")
            continue
        
        try:
            emotion, confidence, probs = predict_emotion(user_input, model, vectorizer, emotion_mapping)
            print(f"🎯 Predicted Emotion: {emotion.upper()} ({confidence:.1f}% confidence)")
            
            # Show all emotion probabilities
            print("📈 All emotion probabilities:")
            for i, prob in enumerate(probs):
                emo_name = emotion_mapping[i]
                print(f"   {emo_name.title()}: {prob*100:.1f}%")
                
        except Exception as e:
            print(f"❌ Error during prediction: {e}")

if __name__ == "__main__":
    main()
