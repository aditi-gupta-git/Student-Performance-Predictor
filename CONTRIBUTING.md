# Contributing to Student Performance Predictor

First off, thank you for considering contributing to Student Performance Predictor! It's people like you that make this project such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. By participating, you are expected to uphold this standard.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed and what behavior you expected**
* **Include screenshots if possible**
* **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a detailed description of the suggested enhancement**
* **Explain why this enhancement would be useful**
* **List some examples of how it would be used**

### Pull Requests

* Fill in the required template
* Follow the Python style guide (PEP 8)
* Include comments in your code where necessary
* Update the README.md with details of changes if applicable
* Ensure all tests pass
* Make sure your code lints without errors

## Development Setup

1. Fork the repo and clone your fork:
```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a new branch:
```bash
git checkout -b feature/your-feature-name
```

5. Make your changes and test them:
```bash
python app.py
```

6. Commit your changes:
```bash
git add .
git commit -m "Add: brief description of your changes"
```

7. Push to your fork:
```bash
git push origin feature/your-feature-name
```

8. Create a Pull Request

## Style Guidelines

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

Examples:
* `Fix: correct math score prediction bug`
* `Add: new model evaluation metrics`
* `Update: improve UI responsiveness`
* `Docs: update installation instructions`

### Python Style Guide

* Follow PEP 8
* Use meaningful variable names
* Add docstrings to functions and classes
* Keep functions focused and small
* Use type hints where appropriate

Example:
```python
def calculate_score(features: dict) -> float:
    """
    Calculate the predicted math score.
    
    Args:
        features (dict): Student features dictionary
        
    Returns:
        float: Predicted math score
    """
    # Implementation
    pass
```

## Project Structure

When adding new features, maintain the existing structure:

* `src/components/` - Data processing and model training components
* `src/pipeline/` - Training and prediction pipelines
* `templates/` - HTML templates
* `notebook/` - Jupyter notebooks for exploration
* `artifacts/` - Generated model files and data

## Testing

* Write tests for new features
* Ensure existing tests pass
* Test your changes locally before submitting

## Documentation

* Update README.md if you change functionality
* Add docstrings to new functions/classes
* Comment complex logic
* Update API documentation if you change endpoints

## Questions?

Feel free to open an issue with your question or reach out to the maintainer directly.

## Recognition

Contributors will be recognized in the project README and release notes.

Thank you for contributing! 🎉
