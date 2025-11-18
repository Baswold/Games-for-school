# Troubleshooting Guide

Common issues and their solutions for the School Games Collection.

## Table of Contents

- [Installation Issues](#installation-issues)
- [Game Launch Problems](#game-launch-problems)
- [Turtle Graphics Issues](#turtle-graphics-issues)
- [Performance Problems](#performance-problems)
- [Input/Control Issues](#inputcontrol-issues)
- [High Score Issues](#high-score-issues)
- [Platform-Specific Issues](#platform-specific-issues)
- [Error Messages](#error-messages)

---

## Installation Issues

### Python Not Found

**Problem**: `python: command not found` or `python3: command not found`

**Solution**:
```bash
# Check if Python is installed
which python3
python3 --version

# If not installed, install Python 3:
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3

# macOS (with Homebrew):
brew install python3

# Windows:
# Download from python.org
```

### Pip Not Working

**Problem**: `pip: command not found`

**Solution**:
```bash
# Try python3 -m pip instead
python3 -m pip install package_name

# Or install pip:
# Ubuntu/Debian:
sudo apt-get install python3-pip

# macOS:
# Comes with Python installation

# Windows:
# Use python -m ensurepip
```

### Tkinter Not Found

**Problem**: `ModuleNotFoundError: No module named '_tkinter'`

**Solution**:
```bash
# Ubuntu/Debian:
sudo apt-get install python3-tk

# macOS:
# Usually included with Python
# If not, reinstall Python from python.org

# Windows:
# Reinstall Python and ensure "tcl/tk" is selected
```

### Pillow Installation Fails

**Problem**: Error installing Pillow

**Solution**:
```bash
# Make sure you have build tools
# Ubuntu/Debian:
sudo apt-get install python3-dev python3-pil

# macOS:
# Install with pip should work
pip3 install Pillow

# Windows:
# Use pre-built wheels
pip install Pillow
```

### OpenCV Installation Issues

**Problem**: `cv2` import fails

**Solution**:
```bash
# Install opencv-python
pip3 install opencv-python

# If that fails, try:
pip3 install opencv-python-headless

# Note: ASCII webcam is optional
# Other games work without it
```

---

## Game Launch Problems

### Game Window Doesn't Open

**Problem**: Game starts but no window appears

**Solutions**:

1. **Check if window is behind other windows**
   - Look in taskbar/dock
   - Alt+Tab (Windows/Linux) or Cmd+Tab (macOS)

2. **Try running directly**:
   ```bash
   python3 "Turtle tag.py"
   ```

3. **Check display settings**:
   ```python
   # Add to game file temporarily:
   import turtle
   screen = turtle.Screen()
   screen.setup(width=800, height=600)
   print("Screen created!")
   input("Press Enter...")
   ```

### Game Launcher Won't Start

**Problem**: `game_launcher.py` fails to run

**Solutions**:

1. **Check for syntax errors**:
   ```bash
   python3 -m py_compile game_launcher.py
   ```

2. **Run with error details**:
   ```bash
   python3 game_launcher.py
   ```

3. **Try launching games directly**:
   ```bash
   python3 Quiz_game.py
   ```

### ImportError for Custom Modules

**Problem**: `ImportError: No module named 'high_scores'`

**Solution**:
```bash
# Make sure you're in the correct directory
cd /path/to/Games-for-school

# Run from that directory
python3 game_launcher.py

# Or add to Python path:
export PYTHONPATH="${PYTHONPATH}:/path/to/Games-for-school"
```

---

## Turtle Graphics Issues

### Turtle Window Freezes

**Problem**: Window becomes unresponsive

**Solutions**:

1. **Don't click rapidly on the window**
   - Turtle graphics can freeze if overloaded
   - Wait for operations to complete

2. **Close properly**:
   - Click the window (not just close button)
   - Let `exitonclick()` handle closing

3. **Force quit if needed**:
   - Press Ctrl+C in terminal
   - Or close terminal window

### Turtle Moves Too Fast/Slow

**Problem**: Animation speed is wrong

**Solution**:
```python
# In the game file, adjust speed:
turtle.speed(0)  # Fastest (instant)
turtle.speed(1)  # Slowest
turtle.speed(5)  # Medium (default)
turtle.speed(10) # Fast

# Or edit game_config.py:
"animation_speed": "slow"  # slow, normal, fast
```

### Graphics Are Choppy

**Problem**: Movements are jerky

**Solutions**:

1. **Disable animation**:
   ```python
   screen.tracer(0)  # Disable auto-update
   # ... draw everything ...
   screen.update()   # Manual update
   ```

2. **Reduce complexity**:
   - Fewer objects on screen
   - Simpler shapes
   - Lower frame rate

3. **Close other programs**:
   - Free up CPU/memory
   - Close browser tabs
   - Stop background processes

### Colors Don't Display

**Problem**: Colors appear as black/white

**Solution**:
```python
# Use valid color names:
turtle.color("red")      # ✓ Good
turtle.color("#FF0000")  # ✓ Good
turtle.color("redd")     # ✗ Invalid

# Check color depth:
screen.colormode(255)  # For RGB values 0-255
turtle.color(255, 0, 0)  # Red in RGB
```

---

## Performance Problems

### Game Runs Slowly

**Problem**: Low FPS, lag

**Solutions**:

1. **Reduce window size**:
   ```python
   screen.setup(width=600, height=400)  # Smaller
   ```

2. **Optimize drawing**:
   ```python
   turtle.speed(0)  # Fastest
   turtle.hideturtle()  # Hide when not needed
   screen.tracer(0)  # Manual updates
   ```

3. **Close other apps**:
   - Save memory and CPU
   - Close browser, IDE, etc.

4. **Check Python version**:
   ```bash
   python3 --version
   # Upgrade if very old
   ```

### High CPU Usage

**Problem**: Python using 100% CPU

**Solutions**:

1. **Add delays in loops**:
   ```python
   import time
   while True:
       # game logic
       time.sleep(0.01)  # Small delay
   ```

2. **Use ontimer instead of while**:
   ```python
   def update():
       # game logic
       screen.ontimer(update, 16)  # ~60 FPS
   ```

3. **Check for infinite loops**:
   - Add print statements
   - Use debugger

---

## Input/Control Issues

### Keyboard Controls Don't Work

**Problem**: Arrow keys/keys don't respond

**Solutions**:

1. **Click on the turtle window**:
   - Window must have focus
   - Click inside the graphics area

2. **Check key bindings**:
   ```python
   screen.listen()  # Enable keyboard input
   screen.onkey(function, "Up")  # Bind keys
   ```

3. **Verify function names**:
   ```python
   # Wrong:
   screen.onkey(move_up(), "Up")  # Calls immediately

   # Right:
   screen.onkey(move_up, "Up")    # Passes function
   ```

### Mouse Clicks Don't Register

**Problem**: `exitonclick()` doesn't work

**Solutions**:

1. **Wait for window to load**:
   - Let graphics render completely
   - Don't click too early

2. **Check for errors**:
   - Look in terminal for error messages
   - Fix any exceptions first

3. **Use alternative**:
   ```python
   # Instead of exitonclick:
   screen.mainloop()
   ```

### Input Box Doesn't Appear

**Problem**: `textinput()` or `numinput()` fails

**Solutions**:

1. **Check tkinter**:
   ```python
   import tkinter
   # If this errors, tkinter not installed
   ```

2. **Try alternative input**:
   ```python
   # Terminal input instead
   choice = input("Enter choice: ")
   ```

---

## High Score Issues

### Scores Not Saving

**Problem**: High scores disappear after closing

**Solutions**:

1. **Check file permissions**:
   ```bash
   ls -l high_scores.json
   # Should be writable
   chmod 644 high_scores.json
   ```

2. **Check for errors**:
   ```python
   # In game code, add:
   try:
       manager.add_score(...)
   except Exception as e:
       print(f"Error saving: {e}")
   ```

3. **Manually check JSON**:
   ```bash
   cat high_scores.json
   # Should be valid JSON
   ```

### JSON Decode Error

**Problem**: `JSONDecodeError` when loading scores

**Solutions**:

1. **Backup and reset**:
   ```bash
   mv high_scores.json high_scores.json.bak
   # Run game again (creates new file)
   ```

2. **Fix JSON manually**:
   - Open in text editor
   - Check for syntax errors
   - Ensure proper brackets/quotes

3. **Validate JSON**:
   ```python
   import json
   with open('high_scores.json') as f:
       data = json.load(f)  # Will show error
   ```

### Scores Show Wrong Order

**Problem**: Scores not sorted correctly

**Solution**:
```python
# Check higher_is_better setting
"higher_is_better": True   # For points/time survived
"higher_is_better": False  # For completion time
```

---

## Platform-Specific Issues

### macOS: Python 2 vs Python 3

**Problem**: Running `python` uses Python 2

**Solution**:
```bash
# Always use python3 explicitly
python3 game_launcher.py

# Or create alias:
echo 'alias python=python3' >> ~/.zshrc
source ~/.zshrc
```

### macOS: Turtle Window Behind Terminal

**Problem**: Graphics window hidden

**Solution**:
```python
# Add at start of game:
import os
os.system("osascript -e 'tell application \"Python\" to activate'")
```

### Windows: Wrong Python Version

**Problem**: `py` command uses wrong version

**Solution**:
```bash
# Use Python Launcher
py -3 game_launcher.py

# Or specify version
py -3.9 game_launcher.py

# Check available versions
py --list
```

### Windows: File Path Issues

**Problem**: File not found with spaces in path

**Solution**:
```bash
# Use quotes:
python "C:\Path With Spaces\Turtle tag.py"

# Or avoid spaces in paths
```

### Linux: Permission Denied

**Problem**: Can't execute file

**Solution**:
```bash
# Make executable:
chmod +x game_launcher.py

# Run with:
./game_launcher.py

# Or use python directly:
python3 game_launcher.py
```

---

## Error Messages

### ModuleNotFoundError

**Error**: `ModuleNotFoundError: No module named 'X'`

**Solutions**:
- Install missing module: `pip3 install X`
- Check spelling in import statement
- Ensure you're in correct directory

### AttributeError

**Error**: `AttributeError: 'X' object has no attribute 'Y'`

**Solutions**:
- Check object type (print(type(obj)))
- Verify method name spelling
- Check if object was initialized correctly

### SyntaxError

**Error**: `SyntaxError: invalid syntax`

**Solutions**:
- Check for missing colons `:` after if/for/def
- Check for matching brackets/parentheses
- Check indentation (use 4 spaces, not tabs)

### IndentationError

**Error**: `IndentationError: unexpected indent`

**Solutions**:
- Use consistent indentation (4 spaces)
- Don't mix tabs and spaces
- Check for extra spaces at start of lines

### ValueError

**Error**: `ValueError: invalid literal for int()`

**Solutions**:
- Validate input before converting
- Add error handling with try/except
- Check input format

### FileNotFoundError

**Error**: `FileNotFoundError: [Errno 2] No such file`

**Solutions**:
- Check file exists: `ls -l filename`
- Use absolute paths
- Check spelling of filename
- Ensure you're in correct directory

---

## Still Having Issues?

If your problem isn't listed here:

1. **Check the error message carefully**
   - Read the full traceback
   - Note the file and line number
   - Look for clues in the message

2. **Enable debug mode**:
   ```python
   # In game_config.py:
   "debug_mode": True
   ```

3. **Run tests**:
   ```bash
   python3 test_games.py
   ```

4. **Check Python version**:
   ```bash
   python3 --version
   # Should be 3.6 or higher
   ```

5. **Try a minimal example**:
   ```python
   import turtle
   screen = turtle.Screen()
   t = turtle.Turtle()
   t.forward(100)
   screen.exitonclick()
   ```

6. **Report the issue**:
   - Include error message
   - Include your OS and Python version
   - Describe steps to reproduce
   - Note what you've already tried

---

## Prevention Tips

**Avoid common issues**:

- ✓ Always run from project directory
- ✓ Use `python3` not `python`
- ✓ Keep Python updated
- ✓ Install dependencies properly
- ✓ Don't modify core files unless needed
- ✓ Make backups of high_scores.json
- ✓ Close games properly (don't force quit)
- ✓ Read error messages carefully

---

**Happy Gaming!** 🎮

Most issues have simple solutions. Don't hesitate to ask for help if stuck!
