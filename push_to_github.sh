#!/bin/bash
# Run this after creating your GitHub repository

echo "🚀 Pushing to GitHub..."
echo "Repository: https://github.com/TamasTandel/emotion-classification-app"

# Add remote origin
git remote add origin https://github.com/TamasTandel/emotion-classification-app.git

# Push to GitHub
git push -u origin main

echo "✅ Code pushed successfully!"
echo ""
echo "🌐 Your repository: https://github.com/TamasTandel/emotion-classification-app"
echo ""
echo "🚀 Next: Deploy to Streamlit Cloud"
echo "1. Go to: https://share.streamlit.io"
echo "2. Sign in with GitHub"
echo "3. Click 'New app'"
echo "4. Select: TamasTandel/emotion-classification-app"
echo "5. Main file: streamlit_app.py"
echo "6. Click Deploy!"
echo ""
echo "📱 Your app will be live at:"
echo "https://tamastandel-emotion-classification-app.streamlit.app"
