# 🎮 School Games Collection

A comprehensive collection of fun, educational Python games perfect for learning programming concepts while having a great time!

## 📋 Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Game Descriptions](#game-descriptions)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Contributing](#contributing)

---

## 🌟 Overview

This collection features **9 unique games** ranging from action-packed chase games to brain-teasing puzzles. Each game is designed to be both entertaining and educational, teaching programming concepts like loops, conditionals, functions, and event handling.

### Game Count by Category

- **Action Games**: 1
- **Puzzle Games**: 2
- **Educational Games**: 1
- **Casual Games**: 3
- **Mini-Games Collection**: 1 (with 7 sub-games)
- **Creative Tools**: 1

---

## 🚀 Quick Start

### Using the Game Launcher (Recommended)

```bash
python3 game_launcher.py
```

The launcher provides a beautiful menu interface to browse and launch all games!

### Running Individual Games

```bash
python3 "Turtle tag.py"
python3 Quiz_game.py
python3 maze_turtle2.py
# ... etc
```

---

## 🎯 Game Descriptions

### 1. Turtle Tag (Enhanced Edition) 🏃

**File**: `Turtle tag.py`
**Category**: Action
**Difficulty**: Easy - Hard

An exciting chase game where you control a blue turtle trying to escape from a red chaser!

**Features**:
- 🎚️ Three difficulty levels (Easy, Medium, Hard)
- ⭐ Four types of power-ups:
  - 🟡 **Invincible**: Become temporarily invincible
  - 🔵 **Speed Boost**: Move faster to escape
  - ❄️ **Freeze**: Stop the chaser temporarily
  - 🌀 **Teleport**: Jump to a random location
- 📊 Real-time score tracking
- 🏆 High score integration
- 🎮 Turbo mode (W/S keys for extra speed)

**Controls**:
- **Arrow Keys**: Normal movement
- **W/S**: Turbo forward/backward
- **Collect colored circles**: Power-ups

---

### 2. Python Quiz Game 📚

**File**: `Quiz_game.py`
**Category**: Educational
**Difficulty**: Medium

Test your Python programming knowledge with this comprehensive quiz!

**Features**:
- 15 carefully crafted questions about Python
- Multiple choice format (A/B/C/D)
- Detailed explanations for each answer
- Speed bonus for quick answers
- Letter grade system (A-F)
- Randomized question order
- Time tracking per question

**Topics Covered**:
- Python syntax and keywords
- Data types and operators
- Functions and modules
- Control flow
- Built-in functions

---

### 3. Maze Runner (Advanced) 🧩

**File**: `maze_turtle2.py`
**Category**: Puzzle
**Difficulty**: Hard

Navigate through a complex maze with realistic wall collision detection!

**Features**:
- ✅ Advanced point-to-line segment collision detection
- ⏱️ Completion time tracking
- 🎯 Clear start (green) and finish (red) markers
- 🏁 Victory screen with time display
- 📏 Precise 25-pixel grid movement

**Controls**:
- **Arrow Keys**: Move up, down, left, right

**Objective**: Navigate from the green start circle to the red finish circle without hitting walls!

---

### 4. Maze Challenge 🗺️

**File**: `turtle_maze.py`
**Category**: Puzzle
**Difficulty**: Easy

A simpler maze perfect for beginners!

**Features**:
- Beautiful light blue background
- Clear visual design
- Completion time tracking
- Simple maze layout

**Controls**:
- **Arrow Keys**: Navigate the maze

---

### 5. Number Guessing Game 🔢

**File**: `number_game.py`
**Category**: Logic
**Difficulty**: Easy

Guess the secret number between 1 and 100!

**Features**:
- 10 attempts to guess correctly
- "Too high" / "Too low" hints
- "Getting close!" proximity hints
- Replay option
- Invalid input handling

---

### 6. Mega Mini Arcade 🎰

**File**: `mini_arcade.py`
**Category**: Variety
**Difficulty**: Easy - Medium

**A collection of 7 mini-games in one program!**

#### Sub-Games:

1. **🪙 Coin Flip**
   - Flip a virtual coin
   - Track heads/tails statistics
   - Perfect for learning probability

2. **🔢 Number Guess**
   - Guess numbers 1-10
   - Attempt tracking
   - High/low hints

3. **🎨 Etch-a-Sketch**
   - Draw with turtle graphics
   - Change colors (Space bar)
   - Clear canvas (C key)
   - Pen up/down (U/D keys)

4. **🎯 Hangman**
   - Classic word guessing game
   - Programming-themed words
   - 6 wrong guesses allowed
   - Visual word progress

5. **🧠 Memory Match**
   - Match pairs of fruit emojis
   - 12 cards (6 pairs)
   - Attempt counting
   - Memory training

6. **⚡ Reaction Time Test**
   - Test your reflexes
   - Results in milliseconds
   - Performance ratings
   - Multiple attempts

7. **🔢 Math Challenge**
   - 10 rapid-fire math problems
   - Addition, subtraction, multiplication
   - Time tracking
   - Accuracy scoring

---

### 7. Simple Games 🎲

**File**: `simple_game.py`
**Category**: Casual
**Difficulty**: Easy

Two classic games for quick fun:

1. **Rock Paper Scissors**
   - 3 rounds against computer
   - Automatic play demonstration

2. **Dice Roll Adventure**
   - Roll two dice 5 times
   - Special bonuses:
     - Double sixes: +10 bonus points
     - Snake eyes (double ones): Unlucky!
   - Score ratings

---

### 8. ASCII Webcam 📹

**File**: `picture_ASKII.py`
**Category**: Creative
**Difficulty**: N/A

Turn your webcam into ASCII art in real-time!

**Features**:
- Live webcam to ASCII conversion
- Adjustable frame size
- ~10 FPS display
- Artistic character mapping

**Requirements**: OpenCV (`cv2`), numpy

---

### 9. Background Maze 🖼️

**File**: `background_maze.py`
**Category**: Casual
**Difficulty**: Easy

Navigate a turtle on a custom background image!

**Features**:
- Image scaling and resizing
- Custom background support
- Smooth turtle controls

**Requirements**: Pillow (PIL)

---

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- tkinter (usually comes with Python)

### Required Libraries

Install using pip:

```bash
# Core requirements (for most games)
pip install pillow

# Optional (for ASCII Webcam)
pip install opencv-python numpy
```

### Clone or Download

```bash
git clone <repository-url>
cd Games-for-school
```

---

## 📖 Usage

### Method 1: Game Launcher (Recommended)

```bash
python3 game_launcher.py
```

Navigate the menu with number keys and enjoy features like:
- Game browsing by category
- Statistics view
- Help system
- Clean interface

### Method 2: Direct Execution

```bash
python3 "name-of-game.py"
```

### High Score Tracking

Some games integrate with the high score system:

```bash
python3 high_scores.py
```

View, manage, and export high scores!

---

## ✨ Features

### 🎯 Game Features

- **Multiple Difficulty Levels**: Choose your challenge
- **High Score Tracking**: Compete against yourself
- **Power-ups and Bonuses**: Special abilities in select games
- **Real-time Feedback**: Instant scoring and hints
- **Educational Value**: Learn while playing

### 🔧 Technical Features

- **Clean Code**: Well-documented and organized
- **Error Handling**: Graceful failure management
- **Cross-platform**: Works on Windows, macOS, Linux
- **No External Game Libraries**: Uses Python standard library
- **Persistent Storage**: JSON-based high scores

---

## 📦 Requirements

### Required

- **Python**: 3.6+
- **tkinter**: For turtle graphics (usually pre-installed)

### Optional

- **Pillow**: For background image games
  ```bash
  pip install pillow
  ```

- **OpenCV + NumPy**: For ASCII webcam
  ```bash
  pip install opencv-python numpy
  ```

---

## 📁 File Structure

```
Games-for-school/
│
├── game_launcher.py         # Central game launcher
├── high_scores.py           # High score management system
├── high_scores.json         # High score data (auto-generated)
│
├── Turtle tag.py            # Enhanced chase game
├── Quiz_game.py             # Python quiz game
├── maze_turtle2.py          # Advanced maze with collision
├── turtle_maze.py           # Simple maze game
├── number_game.py           # Number guessing game
├── mini_arcade.py           # 7-in-1 game collection
├── simple_game.py           # Rock-paper-scissors & dice
├── picture_ASKII.py         # ASCII webcam
├── background_maze.py       # Maze with custom background
│
├── background.gif           # Background image
├── background_scaled.gif    # Scaled background (auto-generated)
│
└── README.md               # This file
```

---

## 🎮 Gameplay Tips

### Turtle Tag
- Collect power-ups strategically
- Use walls to your advantage
- Save turbo mode for emergencies
- Gold circles (invincibility) are most valuable

### Maze Games
- Plan your route before moving
- In Maze Runner, the collision detection is precise
- Take your time - there's no time penalty

### Quiz Game
- Read questions carefully
- Speed bonus rewards quick thinking
- Learn from explanations

### Mini Arcade
- **Hangman**: Common letters first (E, T, A, O)
- **Memory Match**: Remember positions, not just matches
- **Reaction Time**: Don't anticipate - wait for GO!
- **Math Challenge**: Mental math practice helps

---

## 🐛 Known Issues

- **Turtle Graphics**: May be slow on some systems
- **ASCII Webcam**: Requires webcam permission
- **Background Games**: Need correct GIF file path

---

## 🤝 Contributing

This is a school project, but suggestions are welcome!

### Ideas for Future Enhancements

- [ ] Sound effects
- [ ] More maze levels
- [ ] Multiplayer modes
- [ ] Leaderboards with names
- [ ] More quiz categories
- [ ] Mobile version

---

## 📝 License

This project is for educational purposes.

---

## 🎓 Learning Objectives

By exploring these games, you'll learn:

- **Event-driven programming**: Keyboard input handling
- **Game loops**: While loops and timing
- **Collision detection**: Distance calculations and boundaries
- **Data structures**: Lists, dictionaries, classes
- **File I/O**: JSON for persistent storage
- **Turtle graphics**: Visual programming
- **Random number generation**: Game mechanics
- **User input validation**: Error handling
- **Time management**: Performance tracking
- **Code organization**: Functions and modules

---

## 🎉 Have Fun!

Enjoy playing these games and learning Python! Each game teaches different programming concepts while being genuinely fun to play.

**Questions or suggestions?** Feel free to explore the code and learn how each game works!

---

**Made with ❤️ using Python**

*Happy Gaming! 🎮*
