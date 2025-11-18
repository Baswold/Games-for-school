"""
Game Utilities Module
Common functions and classes used across multiple games
"""
import turtle as t
import random
import time
import math
from typing import Tuple, List, Optional, Callable

# ==================== TURTLE GRAPHICS UTILITIES ====================

class TurtleHelper:
    """Helper class for common turtle graphics operations."""

    @staticmethod
    def setup_screen(width: int = 800, height: int = 600,
                     title: str = "Game", bgcolor: str = "white") -> t.Screen:
        """
        Set up a turtle screen with common settings.

        Args:
            width: Screen width in pixels
            height: Screen height in pixels
            title: Window title
            bgcolor: Background color

        Returns:
            Configured screen object
        """
        screen = t.Screen()
        screen.setup(width=width, height=height)
        screen.title(title)
        screen.bgcolor(bgcolor)
        screen.tracer(0)  # Disable auto-update for better performance
        return screen

    @staticmethod
    def create_turtle(shape: str = "turtle", color: str = "black",
                     speed: int = 0, visible: bool = True) -> t.Turtle:
        """
        Create a turtle with common settings.

        Args:
            shape: Turtle shape
            color: Turtle color
            speed: Animation speed (0 = instant)
            visible: Whether turtle is visible

        Returns:
            Configured turtle object
        """
        turtle = t.Turtle()
        turtle.shape(shape)
        turtle.color(color)
        turtle.speed(speed)
        turtle.penup()

        if not visible:
            turtle.hideturtle()

        return turtle

    @staticmethod
    def create_text_turtle(x: int = 0, y: int = 0, color: str = "black") -> t.Turtle:
        """
        Create a turtle for displaying text.

        Args:
            x: X coordinate
            y: Y coordinate
            color: Text color

        Returns:
            Text turtle object
        """
        text_turtle = t.Turtle()
        text_turtle.hideturtle()
        text_turtle.penup()
        text_turtle.goto(x, y)
        text_turtle.color(color)
        return text_turtle

    @staticmethod
    def write_text(turtle: t.Turtle, text: str, align: str = "center",
                   font: Tuple[str, int, str] = ("Arial", 16, "normal")):
        """
        Write text using a turtle.

        Args:
            turtle: Turtle to write with
            text: Text to write
            align: Text alignment
            font: Font tuple (family, size, style)
        """
        turtle.clear()
        turtle.write(text, align=align, font=font)

    @staticmethod
    def draw_rectangle(turtle: t.Turtle, x: int, y: int,
                      width: int, height: int, fill_color: str = None):
        """
        Draw a filled rectangle.

        Args:
            turtle: Turtle to draw with
            x: Top-left x coordinate
            y: Top-left y coordinate
            width: Rectangle width
            height: Rectangle height
            fill_color: Fill color (None for no fill)
        """
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()

        if fill_color:
            turtle.fillcolor(fill_color)
            turtle.begin_fill()

        for _ in range(2):
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)

        if fill_color:
            turtle.end_fill()

        turtle.penup()

    @staticmethod
    def draw_circle(turtle: t.Turtle, x: int, y: int,
                   radius: int, fill_color: str = None):
        """
        Draw a filled circle.

        Args:
            turtle: Turtle to draw with
            x: Center x coordinate
            y: Center y coordinate
            radius: Circle radius
            fill_color: Fill color (None for no fill)
        """
        turtle.penup()
        turtle.goto(x, y - radius)
        turtle.pendown()

        if fill_color:
            turtle.fillcolor(fill_color)
            turtle.begin_fill()

        turtle.circle(radius)

        if fill_color:
            turtle.end_fill()

        turtle.penup()


# ==================== COLLISION DETECTION ====================

class CollisionDetector:
    """Collision detection utilities for games."""

    @staticmethod
    def distance(x1: float, y1: float, x2: float, y2: float) -> float:
        """
        Calculate distance between two points.

        Args:
            x1, y1: First point coordinates
            x2, y2: Second point coordinates

        Returns:
            Distance between points
        """
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    @staticmethod
    def circle_collision(x1: float, y1: float, r1: float,
                        x2: float, y2: float, r2: float) -> bool:
        """
        Check if two circles collide.

        Args:
            x1, y1: First circle center
            r1: First circle radius
            x2, y2: Second circle center
            r2: Second circle radius

        Returns:
            True if circles collide
        """
        dist = CollisionDetector.distance(x1, y1, x2, y2)
        return dist < (r1 + r2)

    @staticmethod
    def point_in_rectangle(px: float, py: float,
                          rx: float, ry: float,
                          rw: float, rh: float) -> bool:
        """
        Check if a point is inside a rectangle.

        Args:
            px, py: Point coordinates
            rx, ry: Rectangle top-left corner
            rw, rh: Rectangle width and height

        Returns:
            True if point is inside rectangle
        """
        return (rx <= px <= rx + rw) and (ry <= py <= ry + rh)

    @staticmethod
    def point_to_line_distance(px: float, py: float,
                               x1: float, y1: float,
                               x2: float, y2: float) -> float:
        """
        Calculate distance from a point to a line segment.

        Args:
            px, py: Point coordinates
            x1, y1: Line segment start
            x2, y2: Line segment end

        Returns:
            Distance from point to line segment
        """
        # Vector from line start to end
        dx = x2 - x1
        dy = y2 - y1

        # Vector from line start to point
        px_dx = px - x1
        py_dy = py - y1

        # Calculate parameter t
        line_length_sq = dx * dx + dy * dy

        if line_length_sq == 0:
            # Line is a point
            return math.sqrt((px - x1) ** 2 + (py - y1) ** 2)

        t = max(0, min(1, (px_dx * dx + py_dy * dy) / line_length_sq))

        # Closest point on line segment
        closest_x = x1 + t * dx
        closest_y = y1 + t * dy

        # Distance from point to closest point
        return math.sqrt((px - closest_x) ** 2 + (py - closest_y) ** 2)


# ==================== GAME TIMER ====================

class GameTimer:
    """Simple game timer for tracking elapsed time."""

    def __init__(self):
        """Initialize the timer."""
        self.start_time = None
        self.pause_time = None
        self.total_paused = 0
        self.is_paused = False

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        self.pause_time = None
        self.total_paused = 0
        self.is_paused = False

    def pause(self):
        """Pause the timer."""
        if not self.is_paused and self.start_time:
            self.pause_time = time.time()
            self.is_paused = True

    def resume(self):
        """Resume the timer."""
        if self.is_paused and self.pause_time:
            self.total_paused += time.time() - self.pause_time
            self.is_paused = False
            self.pause_time = None

    def get_elapsed(self) -> float:
        """
        Get elapsed time in seconds.

        Returns:
            Elapsed time (excluding paused time)
        """
        if not self.start_time:
            return 0

        if self.is_paused:
            return self.pause_time - self.start_time - self.total_paused
        else:
            return time.time() - self.start_time - self.total_paused

    def format_time(self, elapsed: float = None) -> str:
        """
        Format time as MM:SS.

        Args:
            elapsed: Time to format (uses current elapsed if None)

        Returns:
            Formatted time string
        """
        if elapsed is None:
            elapsed = self.get_elapsed()

        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        return f"{minutes:02d}:{seconds:02d}"


# ==================== SCORE TRACKER ====================

class ScoreTracker:
    """Track and display score during gameplay."""

    def __init__(self, initial_score: int = 0):
        """
        Initialize score tracker.

        Args:
            initial_score: Starting score
        """
        self.score = initial_score
        self.high_score = 0
        self.multiplier = 1
        self.combo = 0

    def add_points(self, points: int, apply_multiplier: bool = True) -> int:
        """
        Add points to score.

        Args:
            points: Points to add
            apply_multiplier: Whether to apply score multiplier

        Returns:
            Points actually added
        """
        if apply_multiplier:
            points *= self.multiplier

        self.score += points
        return points

    def subtract_points(self, points: int):
        """
        Subtract points from score.

        Args:
            points: Points to subtract
        """
        self.score = max(0, self.score - points)

    def reset(self):
        """Reset score to zero."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.multiplier = 1
        self.combo = 0

    def increase_multiplier(self, amount: float = 0.5):
        """
        Increase score multiplier.

        Args:
            amount: Amount to increase by
        """
        self.multiplier += amount

    def reset_multiplier(self):
        """Reset multiplier to 1."""
        self.multiplier = 1

    def increase_combo(self):
        """Increase combo counter."""
        self.combo += 1

    def reset_combo(self):
        """Reset combo counter."""
        self.combo = 0

    def get_score(self) -> int:
        """Get current score."""
        return self.score

    def get_high_score(self) -> int:
        """Get high score."""
        return self.high_score


# ==================== INPUT VALIDATION ====================

class InputValidator:
    """Utilities for validating user input."""

    @staticmethod
    def get_int_input(prompt: str, min_val: int = None,
                     max_val: int = None, default: int = None) -> Optional[int]:
        """
        Get validated integer input from user.

        Args:
            prompt: Input prompt
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            default: Default value if input is empty

        Returns:
            Validated integer or None if cancelled
        """
        while True:
            try:
                user_input = input(prompt).strip()

                if not user_input and default is not None:
                    return default

                value = int(user_input)

                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}")
                    continue

                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}")
                    continue

                return value

            except ValueError:
                print("Please enter a valid number")
            except KeyboardInterrupt:
                return None

    @staticmethod
    def get_choice(prompt: str, choices: List[str],
                  case_sensitive: bool = False) -> Optional[str]:
        """
        Get validated choice from list.

        Args:
            prompt: Input prompt
            choices: Valid choices
            case_sensitive: Whether choices are case-sensitive

        Returns:
            Validated choice or None if cancelled
        """
        while True:
            try:
                user_input = input(prompt).strip()

                if not case_sensitive:
                    user_input = user_input.lower()
                    choices = [c.lower() for c in choices]

                if user_input in choices:
                    return user_input

                print(f"Please choose from: {', '.join(choices)}")

            except KeyboardInterrupt:
                return None

    @staticmethod
    def get_yes_no(prompt: str, default: bool = None) -> bool:
        """
        Get yes/no response from user.

        Args:
            prompt: Input prompt
            default: Default value (True/False/None)

        Returns:
            True for yes, False for no
        """
        yes_choices = ['y', 'yes']
        no_choices = ['n', 'no']

        if default is True:
            prompt += " [Y/n]: "
        elif default is False:
            prompt += " [y/N]: "
        else:
            prompt += " [y/n]: "

        while True:
            try:
                response = input(prompt).strip().lower()

                if not response and default is not None:
                    return default

                if response in yes_choices:
                    return True
                if response in no_choices:
                    return False

                print("Please enter 'yes' or 'no'")

            except KeyboardInterrupt:
                return False if default is None else default


# ==================== RANDOM UTILITIES ====================

class RandomHelper:
    """Helper functions for random number generation."""

    @staticmethod
    def weighted_choice(choices: List[Tuple[any, float]]) -> any:
        """
        Make a weighted random choice.

        Args:
            choices: List of (item, weight) tuples

        Returns:
            Randomly selected item
        """
        total = sum(weight for item, weight in choices)
        r = random.uniform(0, total)
        upto = 0

        for item, weight in choices:
            if upto + weight >= r:
                return item
            upto += weight

        return choices[-1][0]

    @staticmethod
    def shuffle_with_seed(items: List, seed: int = None) -> List:
        """
        Shuffle list with optional seed for reproducibility.

        Args:
            items: List to shuffle
            seed: Random seed

        Returns:
            Shuffled list
        """
        if seed is not None:
            random.seed(seed)

        shuffled = items.copy()
        random.shuffle(shuffled)
        return shuffled


# ==================== EXAMPLE USAGE ====================

if __name__ == "__main__":
    print("Game Utilities Module")
    print("=" * 50)
    print("\nThis module provides common utilities for games:")
    print("- TurtleHelper: Turtle graphics utilities")
    print("- CollisionDetector: Collision detection")
    print("- GameTimer: Time tracking")
    print("- ScoreTracker: Score management")
    print("- InputValidator: Input validation")
    print("- RandomHelper: Random number utilities")
    print("\nImport this module in your games to use these utilities!")
