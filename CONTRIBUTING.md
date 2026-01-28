# Contributing to Face Recognition Attendance System

First off, thank you for considering contributing to this project! 🎉

## Code of Conduct

This project and everyone participating in it is governed by respect and professionalism. Be kind and constructive.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed and what you expected**
- **Include screenshots if relevant**
- **Include your environment details:**
  - OS: [e.g., Windows 10, Ubuntu 20.04]
  - Python version: [e.g., 3.8.5]
  - Library versions: [run `pip list`]

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**
- **Explain why this enhancement would be useful**

### Pull Requests

1. **Fork the repo** and create your branch from `main`
   ```bash
   git checkout -b feature/YourFeatureName
   ```

2. **Make your changes**
   - Write clear, commented code
   - Follow the existing code style
   - Add tests if applicable

3. **Test your changes**
   ```bash
   python attendance_system.py
   ```

4. **Commit your changes**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```
   
   Commit message prefixes:
   - `Add:` New feature
   - `Fix:` Bug fix
   - `Update:` Update existing feature
   - `Refactor:` Code refactoring
   - `Docs:` Documentation changes
   - `Test:` Adding tests

5. **Push to your fork**
   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a Pull Request**

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git
   cd face-recognition-attendance
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create test dataset:
   ```bash
   mkdir -p test_dataset/TestPerson
   # Add test images
   ```

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Maximum line length: 100 characters

Example:
```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

## Testing

Before submitting a PR, ensure:

- [ ] Code runs without errors
- [ ] No regression in existing functionality
- [ ] New features work as expected
- [ ] Documentation is updated
- [ ] No sensitive data in commits

## Documentation

- Update README.md if you change functionality
- Add docstrings to new functions
- Update comments if you change logic
- Add examples for new features

## Project Structure

```
face-recognition-attendance/
├── attendance_system.py      # Main script
├── requirements.txt           # Dependencies
├── README.md                  # Main documentation
├── CONTRIBUTING.md           # This file
├── LICENSE                    # MIT License
└── .gitignore                # Git ignore rules
```

## Need Help?

- Check existing issues and discussions
- Create a new issue with your question
- Tag it as `question`

## Recognition

Contributors will be acknowledged in the README.md file.

Thank you for contributing! 🚀
