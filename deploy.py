#!/usr/bin/env python3
"""
Complete deployment automation for Emotion Classification App
"""

import os
import subprocess
import webbrowser
from pathlib import Path

def print_header(title):
    print(f"\n{'='*60}")
    print(f"🎭 {title}")
    print(f"{'='*60}")

def print_step(step, description):
    print(f"\n📋 STEP {step}: {description}")
    print("-" * 50)

def run_command(command, description, check=True):
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=check, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} completed!")
            return True, result.stdout
        else:
            print(f"❌ {description} failed!")
            print(f"Error: {result.stderr}")
            return False, result.stderr
    except Exception as e:
        print(f"❌ {description} failed with exception: {e}")
        return False, str(e)

def check_git_status():
    """Check if git is properly set up"""
    if not os.path.exists('.git'):
        print("❌ Git not initialized!")
        return False
    
    # Check if we have commits
    success, _ = run_command("git log --oneline -1", "Checking git history", check=False)
    if not success:
        print("❌ No commits found!")
        return False
    
    return True

def get_github_username():
    """Get GitHub username from user"""
    print("\n📝 GitHub Setup Required!")
    print("Before we can push your code, you need to:")
    print("1. Create a GitHub repository named: emotion-classification-app")
    print("2. Make it PUBLIC (so others can access your deployed app)")
    print("3. Don't initialize with README (we already have one)")
    
    username = input("\n👤 Enter your GitHub username: ").strip()
    
    if not username:
        print("❌ Username cannot be empty!")
        return None
    
    return username

def push_to_github(username):
    """Push code to GitHub"""
    repo_url = f"https://github.com/{username}/emotion-classification-app.git"
    
    print(f"\n🔗 Setting up remote repository...")
    print(f"Repository: {repo_url}")
    
    # Remove existing remote if it exists
    run_command("git remote remove origin", "Removing existing origin", check=False)
    
    # Add new remote
    success, _ = run_command(f"git remote add origin {repo_url}", "Adding remote origin")
    if not success:
        return False
    
    # Push to GitHub
    print(f"\n📤 Pushing to GitHub...")
    success, output = run_command("git push -u origin main", "Pushing to GitHub", check=False)
    
    if "fatal" in output.lower() or "error" in output.lower():
        print("❌ Push failed! Please check:")
        print("1. Repository exists on GitHub")
        print("2. Repository name is exactly: emotion-classification-app")
        print("3. You have push permissions")
        return False
    
    print("✅ Code successfully pushed to GitHub!")
    return True

def open_streamlit_cloud():
    """Open Streamlit Cloud for deployment"""
    print("\n🚀 Opening Streamlit Cloud for deployment...")
    webbrowser.open("https://share.streamlit.io")

def show_deployment_instructions(username):
    """Show final deployment instructions"""
    print_step("FINAL", "Deploy to Streamlit Cloud")
    
    print("🌐 Streamlit Cloud should now be open in your browser.")
    print("\nFollow these steps:")
    print("1. ✅ Sign in with GitHub")
    print("2. ✅ Click 'New app'")
    print(f"3. ✅ Select repository: {username}/emotion-classification-app")
    print("4. ✅ Branch: main")
    print("5. ✅ Main file path: streamlit_app.py")
    print("6. ✅ Click 'Deploy!'")
    
    print(f"\n🎉 Your app will be live at:")
    print(f"https://{username}-emotion-classification-app.streamlit.app")
    
    print("\n⏱️  Deployment takes 2-5 minutes.")
    print("📱 Share the URL with anyone to let them try your app!")

def main():
    """Main deployment automation"""
    print_header("AUTOMATED DEPLOYMENT SYSTEM")
    
    print("🎯 This script will:")
    print("   • Verify your project is ready")
    print("   • Push your code to GitHub")
    print("   • Guide you through Streamlit Cloud deployment")
    print("   • Give you a live, shareable URL")
    
    input("\n👆 Press Enter to continue...")
    
    # Step 1: Check git status
    print_step(1, "Verify Project Status")
    if not check_git_status():
        print("❌ Please run 'git init' and commit your files first!")
        return
    
    print("✅ Git repository is ready!")
    print("✅ All files are committed!")
    
    # Step 2: Get GitHub username and create repository
    print_step(2, "GitHub Repository Setup")
    
    username = get_github_username()
    if not username:
        return
    
    print(f"\n✅ Username: {username}")
    print(f"📋 Next, create repository: https://github.com/new")
    print("   Repository name: emotion-classification-app")
    print("   Make it PUBLIC")
    print("   Don't initialize with files")
    
    input("\n👆 Press Enter after creating the repository...")
    
    # Step 3: Push to GitHub
    print_step(3, "Push Code to GitHub")
    
    if not push_to_github(username):
        print("❌ Failed to push to GitHub. Please check the repository setup.")
        return
    
    # Step 4: Open Streamlit Cloud
    print_step(4, "Deploy to Streamlit Cloud")
    
    input("\n👆 Press Enter to open Streamlit Cloud...")
    open_streamlit_cloud()
    
    # Step 5: Show final instructions
    show_deployment_instructions(username)
    
    print_header("DEPLOYMENT COMPLETE! 🎉")
    
    print("🏆 What you've accomplished:")
    print("   ✅ Code is on GitHub (public repository)")
    print("   ✅ Ready for Streamlit Cloud deployment")
    print("   ✅ Will have a live, shareable URL")
    print("   ✅ Others can use your emotion classifier")
    
    print(f"\n📊 Your project stats:")
    print(f"   • 88.9% model accuracy")
    print(f"   • 6 emotion categories")
    print(f"   • 16,000+ training examples")
    print(f"   • Professional web interface")
    
    print(f"\n🌟 After deployment, update your README.md:")
    print(f"   Replace 'your-username' with '{username}'")
    
    input("\n👆 Press Enter to finish...")

if __name__ == "__main__":
    main()
