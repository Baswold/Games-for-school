# Contributing to School Games Collection

Thank you for your interest in contributing to the School Games Collection! This document provides guidelines and instructions for contributing.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Submitting Changes](#submitting-changes)
- [Bug Reports](#bug-reports)
- [Feature Requests](#feature-requests)

---

## Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

---

## Getting Started

### Prerequisites

Before contributing, ensure you have:

1. **Python 3.6+** installed
2. **Git** for version control
3. **A text editor** or IDE (VS Code, PyCharm, etc.)
4. **Basic Python knowledge**

### First-Time Setup

1. **Fork the repository** (if applicable)
2. **Clone your fork**:
   ```bash
   git clone <your-fork-url>
   cd Games-for-school
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run tests**:
   ```bash
   python3 test_games.py
   ```

---

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

1. **Bug Fixes** - Fix issues in existing games
2. **New Features** - Add features to existing games
3. **New Games** - Create entirely new games
4. **Documentation** - Improve README, guides, comments
5. **Testing** - Write tests, find bugs
6. **Optimization** - Improve performance
7. **UI/UX** - Enhance user interface and experience

### Contribution Process

1. **Find or create an issue** to work on
2. **Discuss your approach** before starting large changes
3. **Create a branch** for your work
4. **Make your changes** following our standards
5. **Test thoroughly**
6. **Submit a pull request**
7. **Address review feedback**

---

## Development Setup

### Project Structure

```
Games-for-school/
├── game_launcher.py      # Main launcher
├── high_scores.py        # Score tracking
├── game_config.py        # Configuration
├── game_utils.py         # Utilities
├── test_games.py         # Test suite
├── [Individual games]    # Game files
├── README.md            # Documentation
└── CHANGELOG.md         # Version history
```

### Creating a New Game

When creating a new game, follow this template:

```python
"""
Game Name
Brief description of the game
"""
import turtle as t
from game_utils import TurtleHelper, GameTimer
from high_scores import HighScoreManager

def main():
    """Main game function."""
    # Set up screen
    screen = TurtleHelper.setup_screen(
        width=800,
        height=600,
        title="My Game",
        bgcolor="white"
    )

    # Game logic here

    # Clean up
    screen.exitonclick()

if __name__ == "__main__":
    main()
```

### Integrating with Launcher

To add your game to the launcher, edit `game_launcher.py`:

```python
GAMES = {
    'X': {
        'name': 'Your Game Name',
        'file': 'your_game.py',
        'description': 'Brief description',
        'category': 'Category',
        'difficulty': 'Easy/Medium/Hard'
    }
}
```

---

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

#### Naming Conventions

```python
# Variables and functions: snake_case
player_score = 100
def calculate_distance():
    pass

# Classes: PascalCase
class GameManager:
    pass

# Constants: UPPER_CASE
MAX_PLAYERS = 4
DEFAULT_COLOR = "blue"
```

#### Docstrings

Use Google-style docstrings:

```python
def function_name(param1: int, param2: str) -> bool:
    """
    Brief description of function.

    Longer description if needed.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When something goes wrong
    """
    pass
```

#### Type Hints

Use type hints where appropriate:

```python
from typing import List, Dict, Optional, Tuple

def process_scores(scores: List[int]) -> Optional[int]:
    """Process a list of scores."""
    if not scores:
        return None
    return max(scores)
```

#### Comments

```python
# Good: Explain WHY, not WHAT
# Use turtle graphics because it's beginner-friendly
screen = t.Screen()

# Bad: State the obvious
# Create a screen
screen = t.Screen()
```

### Code Organization

```python
# 1. Module docstring
"""Module description."""

# 2. Imports (standard library, then third-party, then local)
import os
import sys

import turtle as t

from game_utils import TurtleHelper

# 3. Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 4. Classes
class MyClass:
    pass

# 5. Functions
def my_function():
    pass

# 6. Main execution
if __name__ == "__main__":
    main()
```

### Error Handling

```python
# Always handle potential errors
try:
    score = int(input("Enter score: "))
except ValueError:
    print("Please enter a valid number")
    score = 0
```

---

## Testing Guidelines

### Writing Tests

Add tests to `test_games.py`:

```python
def test_my_feature(self):
    """Test description."""
    self.tests_run += 1

    try:
        # Test code here
        assert condition == expected

        self.tests_passed += 1
        self.test_results.append({
            'test': 'Feature name',
            'passed': True,
            'message': 'Success'
        })
    except Exception as e:
        self.tests_failed += 1
        self.test_results.append({
            'test': 'Feature name',
            'passed': False,
            'message': str(e)
        })
```

### Testing Checklist

Before submitting:

- [ ] All existing tests pass
- [ ] New tests added for new features
- [ ] Manual testing completed
- [ ] Edge cases considered
- [ ] Error handling tested
- [ ] Works on Python 3.6+

### Manual Testing

Test your game by:

1. Running it standalone
2. Launching via game launcher
3. Testing all controls
4. Testing edge cases
5. Testing on different screen sizes
6. Checking high score integration

---

## Submitting Changes

### Git Workflow

```bash
# 1. Create a branch
git checkout -b feature/my-feature

# 2. Make changes
# ... edit files ...

# 3. Commit changes
git add .
git commit -m "Add feature: description"

# 4. Push to remote
git push origin feature/my-feature

# 5. Create pull request
# (via GitHub/GitLab interface)
```

### Commit Messages

Follow conventional commits:

```
type(scope): brief description

Longer description if needed.

- Detail 1
- Detail 2
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

**Examples:**
```
feat(turtle-tag): add freeze power-up
fix(quiz): correct answer validation
docs(readme): update installation instructions
```

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation
- [ ] Other

## Testing
- [ ] Tests pass
- [ ] Manual testing completed
- [ ] Edge cases checked

## Screenshots
(if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] CHANGELOG.md updated
```

---

## Bug Reports

### Before Reporting

1. **Search existing issues** to avoid duplicates
2. **Test with latest version**
3. **Try to reproduce** the bug
4. **Gather information** about your environment

### Bug Report Template

```markdown
**Describe the bug**
Clear description of the bug

**To Reproduce**
1. Launch game
2. Click on ...
3. See error

**Expected behavior**
What should happen

**Screenshots**
If applicable

**Environment:**
- OS: [e.g. Windows 10, macOS 12, Ubuntu 20.04]
- Python version: [e.g. 3.9.7]
- Game version: [e.g. 2.0.0]

**Additional context**
Any other information
```

---

## Feature Requests

### Feature Request Template

```markdown
**Feature Description**
Clear description of the feature

**Problem it Solves**
What problem does this address?

**Proposed Solution**
How should it work?

**Alternatives Considered**
Other approaches you've thought about

**Additional Context**
Screenshots, mockups, examples
```

### Feature Ideas

Some areas we'd love contributions:

- **Sound Effects**: Add audio feedback
- **More Power-ups**: New abilities for Turtle Tag
- **New Games**: More mini-games
- **Achievements**: Achievement system
- **Themes**: Visual themes/skins
- **Levels**: More maze levels
- **Multiplayer**: Network play support

---

## Questions?

If you have questions:

1. Check the **README.md**
2. Review **existing code** for examples
3. Look at **similar features**
4. Ask in issues/discussions

---

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md (if we create one)
- Mentioned in release notes
- Appreciated greatly!

---

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to School Games Collection!** 🎮

Every contribution, no matter how small, is valued and appreciated!
