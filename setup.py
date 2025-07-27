#!/usr/bin/env python3
"""
Setup script for Emotion Classification App
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and print status"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python 3.7+ required. You have Python {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} is compatible")
    return True

def install_requirements():
    """Install required packages"""
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return False
    
    command = f"{sys.executable} -m pip install -r requirements.txt"
    return run_command(command, "Installing required packages")

def download_nltk_data():
    """Download required NLTK data"""
    try:
        import nltk
        print("🔄 Downloading NLTK data...")
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK data downloaded successfully!")
        return True
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")
        return False

def check_model_files():
    """Check if model files exist"""
    model_files = [
        "logistic_model_bow.pkl",
        "bow_vectorizer.pkl", 
        "emotion_mapping.pkl"
    ]
    
    missing_files = [f for f in model_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"⚠️  Missing model files: {', '.join(missing_files)}")
        print("📝 Please run the Jupyter notebook 'emotion_classification_training.ipynb' to generate model files")
        return False
    else:
        print("✅ All model files found!")
        return True

def main():
    """Main setup function"""
    print("🎭 EMOTION CLASSIFICATION APP SETUP")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        print("❌ Setup failed during package installation")
        sys.exit(1)
    
    # Download NLTK data
    if not download_nltk_data():
        print("⚠️  NLTK data download failed, but continuing...")
    
    # Check model files
    model_files_exist = check_model_files()
    
    print("\n🎉 SETUP COMPLETE!")
    print("-" * 50)
    
    if model_files_exist:
        print("✅ Your app is ready to run!")
        print("🚀 Start the app with: streamlit run streamlit_app.py")
        print("🌐 Or run: python streamlit_app.py")
    else:
        print("⚠️  Setup complete, but model files are missing")
        print("📝 Next steps:")
        print("   1. Open 'emotion_classification_training.ipynb'")
        print("   2. Run all cells to train the model")
        print("   3. Then run: streamlit run streamlit_app.py")
    
    print(f"\n📚 Additional commands:")
    print(f"   • Test model: python test_model.py")
    print(f"   • Verify model: python verify_model.py")
    print(f"   • View test sentences: python test_sentences.py")

if __name__ == "__main__":
    main()
