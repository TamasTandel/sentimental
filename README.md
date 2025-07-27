# 🎭 Emotion Classification Project

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning project that classifies text emotions using Natural Language Processing (NLP) techniques and provides an interactive Streamlit web interface.

## 🌟 Live Demo
[**Try the app live here!**](https://your-app-url.streamlit.app) _(Update this URL after deployment)_

## 📊 Project Overview

This project implements a text emotion classification system that can identify 6 different emotions from text:
- 😢 **Sadness**
- 😠 **Anger**  
- ❤️ **Love**
- 😮 **Surprise**
- 😨 **Fear**
- 😄 **Joy**

## 🧠 Model Details

- **Algorithm**: Logistic Regression
- **Vectorization**: Bag of Words (CountVectorizer)
- **Accuracy**: 88.9%
- **Dataset**: Custom emotion-labeled text dataset
- **Preprocessing**: Text cleaning, punctuation removal, stopword removal, emoji removal

## 📁 Project Structure

```
emotion-classification-app/
├── 📊 Data & Training
│   ├── train.txt                           # Training dataset (16,000+ labeled emotions)
│   └── emotion_classification_training.ipynb  # Complete model training notebook
├── 🚀 Main Application
│   ├── streamlit_app.py                    # Main Streamlit web application
│   └── requirements.txt                    # Python dependencies
├── 🧪 Testing & Verification
│   ├── test_model.py                       # Interactive command-line testing
│   ├── test_sentences.py                   # Comprehensive test sentences
│   └── verify_model.py                     # Automated model performance analysis
├── ⚙️ Setup & Deployment
│   ├── setup.py                           # Automated setup script
│   ├── Procfile                           # Heroku deployment configuration
│   ├── run_app.bat                        # Windows quick-start script
│   └── run_app.sh                         # Linux/Mac quick-start script
├── 📋 Documentation
│   ├── README.md                          # Complete project documentation
│   └── .gitignore                         # Git ignore rules
└── 🤖 Generated Model Files
    ├── logistic_model_bow.pkl             # Trained Logistic Regression model
    ├── bow_vectorizer.pkl                 # Fitted CountVectorizer
    └── emotion_mapping.pkl                # Emotion label mapping
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/emotion-classification-app.git
   cd emotion-classification-app
   ```

2. **Quick Setup (Recommended)**:
   ```bash
   python setup.py
   ```
   
   **OR Manual Setup**:
   ```bash
   pip install -r requirements.txt
   # Then run the training notebook if model files don't exist
   ```

3. **Generate model files** (if not already present):
   - Open `emotion_classification_training.ipynb` in Jupyter Notebook or VS Code
   - Run all cells to train the model and generate the required `.pkl` files

### Running the Application

#### Option 1: Streamlit Web Interface (Recommended)

**Windows:**
```bash
run_app.bat
```

**Linux/Mac:**
```bash
chmod +x run_app.sh
./run_app.sh
```

**Manual:**
```bash
streamlit run streamlit_app.py
```

The app will start at `http://localhost:8501`

#### Option 2: Command Line Testing

```bash
python test_model.py
```

## 🖥️ Web Interface Features

### Main Features:
- **Real-time Text Classification**: Enter any text and get instant emotion prediction
- **Confidence Scores**: See prediction confidence percentages
- **Probability Distribution**: View probabilities for all emotions
- **Interactive Examples**: Quick-test buttons with sample texts
- **Preprocessing Visualization**: View how text is processed before classification

### Interface Sections:
1. **Text Input Area**: Large text box for entering text to classify
2. **Prediction Results**: Shows predicted emotion with confidence
3. **Probability Chart**: Bar chart showing all emotion probabilities
4. **Example Buttons**: Quick test buttons for different emotions
5. **Model Information**: Sidebar with model details and accuracy

## 🔧 Technical Implementation

### Data Preprocessing Pipeline:
1. **Lowercase conversion**: Convert all text to lowercase
2. **Punctuation removal**: Remove all punctuation marks
3. **Number removal**: Remove all numeric characters
4. **Emoji removal**: Remove non-ASCII characters
5. **Stopword removal**: Remove common English stopwords

### Model Training Process:
1. **Data Loading**: Load text data with emotion labels
2. **Label Encoding**: Convert emotion names to numeric labels
3. **Text Preprocessing**: Apply cleaning pipeline
4. **Vectorization**: Convert text to numerical features using CountVectorizer
5. **Model Training**: Train Logistic Regression classifier
6. **Model Evaluation**: Achieve 88.9% accuracy on test set

### Files Generated:
- `logistic_model_bow.pkl`: Trained Logistic Regression model
- `bow_vectorizer.pkl`: Fitted CountVectorizer for text transformation
- `emotion_mapping.pkl`: Dictionary mapping numeric labels to emotion names

## 📊 Model Performance

- **Training Accuracy**: ~89%
- **Test Accuracy**: 88.9%
- **Model Type**: Logistic Regression with Bag of Words
- **Cross-validation**: Performed with train-test split (80-20)

## 🎯 Usage Examples

### Web Interface:
1. Open the Streamlit app
2. Enter text like: *"I feel so happy and excited today!"*
3. Click "Classify Emotion"
4. View results: **JOY (85.2% confidence)**

### Command Line:
```python
from test_model import predict_emotion, load_model_components

# Load model
model, vectorizer, emotion_mapping = load_model_components()

# Predict emotion
emotion, confidence, probs = predict_emotion(
    "I love spending time with my family", 
    model, vectorizer, emotion_mapping
)

print(f"Emotion: {emotion} ({confidence:.1f}% confidence)")
# Output: Emotion: love (92.3% confidence)
```

## 🛠️ Customization

### Adding New Emotions:
1. Update training data with new emotion labels
2. Retrain the model in the Jupyter notebook
3. Update emotion mapping in the code
4. Regenerate model files

### Improving Accuracy:
- **More Training Data**: Add more diverse examples
- **Feature Engineering**: Try TF-IDF, n-grams, or word embeddings
- **Model Tuning**: Experiment with different algorithms (SVM, Random Forest)
- **Preprocessing**: Fine-tune text cleaning pipeline

## 📦 Dependencies

```
streamlit>=1.28.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
nltk>=3.8
matplotlib>=3.7.0
seaborn>=0.12.0
pickle-mixin>=1.0.2
```

## 🐛 Troubleshooting

### Common Issues:

1. **Model files not found**:
   - Run the Jupyter notebook to generate `.pkl` files
   - Ensure all cells execute successfully

2. **NLTK data not found**:
   - The app automatically downloads required NLTK data
   - Manual download: `nltk.download('punkt')` and `nltk.download('stopwords')`

3. **Import errors**:
   - Install all requirements: `pip install -r requirements.txt`
   - Use a virtual environment if needed

4. **Streamlit not found**:
   - Install Streamlit: `pip install streamlit`
   - Check Python PATH configuration

## 🔮 Future Enhancements

- [ ] **Model Improvements**: Implement BERT or other transformer models
- [ ] **Real-time Analysis**: Add batch processing capabilities
- [ ] **Visualization**: Enhanced charts and emotion trends
- [ ] **API Integration**: REST API for external applications
- [ ] **Multi-language Support**: Support for languages other than English
- [ ] **Deployment**: Docker containerization and cloud deployment

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. **Push to GitHub**: Make sure your code is pushed to a GitHub repository
2. **Visit**: [share.streamlit.io](https://share.streamlit.io)
3. **Connect**: Link your GitHub account
4. **Deploy**: Select your repository and `streamlit_app.py` as the main file
5. **Requirements**: Streamlit Cloud will automatically install from `requirements.txt`

### Heroku Deployment

1. **Create Heroku account** and install Heroku CLI
2. **Create Procfile**:
   ```
   web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0
   ```
3. **Deploy**:
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Local Docker Deployment

1. **Create Dockerfile**:
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   EXPOSE 8501
   CMD ["streamlit", "run", "streamlit_app.py"]
   ```
2. **Build and run**:
   ```bash
   docker build -t emotion-app .
   docker run -p 8501:8501 emotion-app
   ```

### GitHub Pages (Static Documentation)

- The README.md and documentation can be deployed to GitHub Pages for project showcase

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, fork the repository, and create pull requests.

## 📧 Contact

For questions or suggestions, please open an issue in the repository.

---

**Built with ❤️ using Python, Scikit-learn, and Streamlit**
