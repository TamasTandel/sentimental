@echo off
REM GitHub Setup Script for Emotion Classification App

echo 🚀 GITHUB SETUP SCRIPT
echo ======================
echo.

REM Check if git is initialized
if not exist ".git" (
    echo ❌ Git not initialized. Please run 'git init' first.
    pause
    exit /b 1
)

echo ✅ Git repository is ready!
echo.

REM Get GitHub username
set /p GITHUB_USERNAME="📝 Please enter your GitHub username: "

if "%GITHUB_USERNAME%"=="" (
    echo ❌ Username cannot be empty!
    pause
    exit /b 1
)

echo.
echo 🔗 Setting up remote repository...

REM Add remote origin
git remote add origin https://github.com/%GITHUB_USERNAME%/emotion-classification-app.git

echo ✅ Remote origin added!
echo.

echo 📤 Pushing to GitHub...
echo    Repository: https://github.com/%GITHUB_USERNAME%/emotion-classification-app
echo.

REM Push to GitHub
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo 🎉 SUCCESS! Your code is now on GitHub!
    echo 🌐 Repository URL: https://github.com/%GITHUB_USERNAME%/emotion-classification-app
    echo.
    echo 🚀 NEXT STEP: Deploy to Streamlit Cloud
    echo 1. Go to: https://share.streamlit.io
    echo 2. Sign in with GitHub
    echo 3. Click 'New app'
    echo 4. Select your repository: %GITHUB_USERNAME%/emotion-classification-app
    echo 5. Set Main file path: streamlit_app.py
    echo 6. Click Deploy!
    echo.
    echo 📱 Your app will be available at:
    echo    https://%GITHUB_USERNAME%-emotion-classification-app.streamlit.app
) else (
    echo.
    echo ❌ Push failed! Please check:
    echo 1. Make sure you created the repository on GitHub
    echo 2. Check your GitHub credentials
    echo 3. Ensure repository name is: emotion-classification-app
)

echo.
pause
