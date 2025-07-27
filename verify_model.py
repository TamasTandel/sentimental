#!/usr/bin/env python3
"""
Automated model verification using test sentences
"""

import pickle
import string
import pandas as pd
from nltk.corpus import stopwords
import nltk
from test_sentences import TEST_SENTENCES, MIXED_SENTENCES, NEUTRAL_SENTENCES

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
    text = text.lower()
    text = remove_punc(text)
    text = remove_numbers(text)
    text = remove_emojis(text)
    text = remove_stopwords(text)
    return text

def predict_emotion(text, model, vectorizer, emotion_mapping):
    """Predict emotion for given text"""
    processed_text = preprocess_text(text)
    text_vectorized = vectorizer.transform([processed_text])
    prediction = model.predict(text_vectorized)[0]
    prediction_proba = model.predict_proba(text_vectorized)[0]
    emotion = emotion_mapping[prediction]
    confidence = prediction_proba[prediction] * 100
    return emotion, confidence, prediction_proba

def test_emotion_category(emotion_name, sentences, model, vectorizer, emotion_mapping):
    """Test all sentences for a specific emotion category"""
    print(f"\n🎯 TESTING {emotion_name.upper()} SENTENCES:")
    print("─" * 80)
    
    correct_predictions = 0
    total_sentences = len(sentences)
    results = []
    
    for i, sentence in enumerate(sentences, 1):
        predicted_emotion, confidence, probs = predict_emotion(sentence, model, vectorizer, emotion_mapping)
        is_correct = predicted_emotion.lower() == emotion_name.lower()
        
        if is_correct:
            correct_predictions += 1
            status = "✅"
        else:
            status = "❌"
        
        print(f"{i:2d}. {status} Predicted: {predicted_emotion.upper()} ({confidence:.1f}%)")
        print(f"     Text: {sentence}")
        
        # Show top 2 predictions for incorrect ones
        if not is_correct:
            sorted_probs = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
            top_2 = [(emotion_mapping[idx], prob*100) for idx, prob in sorted_probs[:2]]
            print(f"     Top predictions: {top_2[0][0]} ({top_2[0][1]:.1f}%), {top_2[1][0]} ({top_2[1][1]:.1f}%)")
        print()
        
        results.append({
            'sentence': sentence,
            'expected': emotion_name,
            'predicted': predicted_emotion,
            'confidence': confidence,
            'correct': is_correct
        })
    
    accuracy = (correct_predictions / total_sentences) * 100
    print(f"📊 {emotion_name.upper()} ACCURACY: {correct_predictions}/{total_sentences} = {accuracy:.1f}%")
    
    return results, accuracy

def test_mixed_sentences(sentences, model, vectorizer, emotion_mapping):
    """Test mixed emotion sentences"""
    print(f"\n🤔 TESTING MIXED EMOTION SENTENCES:")
    print("─" * 80)
    
    for i, sentence in enumerate(sentences, 1):
        predicted_emotion, confidence, probs = predict_emotion(sentence, model, vectorizer, emotion_mapping)
        
        # Show top 3 predictions for mixed sentences
        sorted_probs = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
        top_3 = [(emotion_mapping[idx], prob*100) for idx, prob in sorted_probs[:3]]
        
        print(f"{i:2d}. Primary: {predicted_emotion.upper()} ({confidence:.1f}%)")
        print(f"     Text: {sentence}")
        print(f"     Top 3: {top_3[0][0]} ({top_3[0][1]:.1f}%), {top_3[1][0]} ({top_3[1][1]:.1f}%), {top_3[2][0]} ({top_3[2][1]:.1f}%)")
        print()

def test_neutral_sentences(sentences, model, vectorizer, emotion_mapping):
    """Test neutral sentences"""
    print(f"\n😐 TESTING NEUTRAL SENTENCES:")
    print("─" * 80)
    
    emotion_counts = {emotion: 0 for emotion in emotion_mapping.values()}
    
    for i, sentence in enumerate(sentences, 1):
        predicted_emotion, confidence, probs = predict_emotion(sentence, model, vectorizer, emotion_mapping)
        emotion_counts[predicted_emotion] += 1
        
        print(f"{i:2d}. Predicted: {predicted_emotion.upper()} ({confidence:.1f}%)")
        print(f"     Text: {sentence}")
        print()
    
    print("📊 NEUTRAL SENTENCE EMOTION DISTRIBUTION:")
    for emotion, count in emotion_counts.items():
        percentage = (count / len(sentences)) * 100
        print(f"   {emotion.title()}: {count} sentences ({percentage:.1f}%)")

def main():
    print("🎭 COMPREHENSIVE MODEL VERIFICATION")
    print("=" * 80)
    
    # Load model
    try:
        model, vectorizer, emotion_mapping = load_model_components()
        print("✅ Model loaded successfully!")
        print(f"📊 Available emotions: {list(emotion_mapping.values())}")
    except FileNotFoundError as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Test each emotion category
    all_results = []
    total_accuracy = []
    
    for emotion_name, sentences in TEST_SENTENCES.items():
        results, accuracy = test_emotion_category(emotion_name, sentences, model, vectorizer, emotion_mapping)
        all_results.extend(results)
        total_accuracy.append(accuracy)
    
    # Calculate overall accuracy
    overall_accuracy = sum(total_accuracy) / len(total_accuracy)
    correct_total = sum(1 for result in all_results if result['correct'])
    total_sentences = len(all_results)
    
    print(f"\n🎯 OVERALL PERFORMANCE:")
    print("─" * 80)
    print(f"Total correct predictions: {correct_total}/{total_sentences}")
    print(f"Overall accuracy: {(correct_total/total_sentences)*100:.1f}%")
    print(f"Average category accuracy: {overall_accuracy:.1f}%")
    
    # Test mixed emotion sentences
    test_mixed_sentences(MIXED_SENTENCES, model, vectorizer, emotion_mapping)
    
    # Test neutral sentences
    test_neutral_sentences(NEUTRAL_SENTENCES, model, vectorizer, emotion_mapping)
    
    # Summary by emotion
    print(f"\n📈 DETAILED ACCURACY BY EMOTION:")
    print("─" * 80)
    for emotion_name in TEST_SENTENCES.keys():
        emotion_results = [r for r in all_results if r['expected'] == emotion_name]
        correct = sum(1 for r in emotion_results if r['correct'])
        total = len(emotion_results)
        accuracy = (correct/total)*100 if total > 0 else 0
        print(f"   {emotion_name.title():10}: {correct:2d}/{total:2d} = {accuracy:5.1f}%")

if __name__ == "__main__":
    main()
