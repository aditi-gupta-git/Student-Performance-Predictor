#!/usr/bin/env python3
"""
Setup script for the Student Performance Predictor project.
This script helps set up the project environment and install dependencies.
"""

import subprocess
import sys
import os
import platform

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("❌ Python 3.9 or higher is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def setup_virtual_environment():
    """Create and activate virtual environment."""
    if os.path.exists("venv"):
        print("✅ Virtual environment already exists")
        return True
    
    return run_command("python -m venv venv", "Creating virtual environment")

def install_dependencies():
    """Install project dependencies."""
    # Determine the correct pip command based on OS
    if platform.system() == "Windows":
        pip_cmd = "venv\\Scripts\\pip"
    else:
        pip_cmd = "venv/bin/pip"
    
    return run_command(f"{pip_cmd} install -r requirements.txt", "Installing dependencies")

def create_artifacts_directory():
    """Create artifacts directory if it doesn't exist."""
    if not os.path.exists("artifacts"):
        os.makedirs("artifacts")
        print("✅ Created artifacts directory")
    else:
        print("✅ Artifacts directory already exists")
    return True

def main():
    """Main setup function."""
    print("🚀 Setting up Student Performance Predictor...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Setup virtual environment
    if not setup_virtual_environment():
        print("❌ Failed to create virtual environment")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Failed to install dependencies")
        sys.exit(1)
    
    # Create artifacts directory
    create_artifacts_directory()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed successfully!")
    print("\nTo activate the virtual environment:")
    if platform.system() == "Windows":
        print("  venv\\Scripts\\activate")
    else:
        print("  source venv/bin/activate")
    print("\nTo run the application:")
    print("  python app.py")
    print("\nTo run tests:")
    print("  python run_tests.py")

if __name__ == "__main__":
    main()