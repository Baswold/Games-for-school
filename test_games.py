"""
Game Testing and Demo Script
Automated tests and demonstrations for all games
"""
import os
import sys
import importlib
import time
from typing import List, Dict, Tuple

class GameTester:
    """Test framework for validating game functionality."""

    def __init__(self):
        """Initialize the tester."""
        self.tests_run = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.test_results = []

    def test_file_exists(self, filename: str) -> bool:
        """
        Test if a game file exists.

        Args:
            filename: File to check

        Returns:
            True if file exists
        """
        self.tests_run += 1
        exists = os.path.exists(filename)

        result = {
            'test': f'File exists: {filename}',
            'passed': exists,
            'message': 'Found' if exists else 'Missing'
        }

        self.test_results.append(result)

        if exists:
            self.tests_passed += 1
        else:
            self.tests_failed += 1

        return exists

    def test_import(self, module_name: str) -> bool:
        """
        Test if a module can be imported.

        Args:
            module_name: Module to import

        Returns:
            True if import succeeds
        """
        self.tests_run += 1

        try:
            importlib.import_module(module_name)
            self.tests_passed += 1

            result = {
                'test': f'Import: {module_name}',
                'passed': True,
                'message': 'Success'
            }

            self.test_results.append(result)
            return True

        except Exception as e:
            self.tests_failed += 1

            result = {
                'test': f'Import: {module_name}',
                'passed': False,
                'message': str(e)
            }

            self.test_results.append(result)
            return False

    def test_function_exists(self, module_name: str, function_name: str) -> bool:
        """
        Test if a function exists in a module.

        Args:
            module_name: Module containing function
            function_name: Function to check

        Returns:
            True if function exists
        """
        self.tests_run += 1

        try:
            module = importlib.import_module(module_name)
            has_function = hasattr(module, function_name)

            if has_function:
                self.tests_passed += 1
            else:
                self.tests_failed += 1

            result = {
                'test': f'Function exists: {module_name}.{function_name}',
                'passed': has_function,
                'message': 'Found' if has_function else 'Missing'
            }

            self.test_results.append(result)
            return has_function

        except Exception as e:
            self.tests_failed += 1

            result = {
                'test': f'Function exists: {module_name}.{function_name}',
                'passed': False,
                'message': str(e)
            }

            self.test_results.append(result)
            return False

    def print_results(self):
        """Print test results in a formatted way."""
        print("\n" + "="*80)
        print("GAME TEST RESULTS".center(80))
        print("="*80 + "\n")

        # Print individual results
        for result in self.test_results:
            status = "✓ PASS" if result['passed'] else "✗ FAIL"
            color_start = "\033[92m" if result['passed'] else "\033[91m"
            color_end = "\033[0m"

            print(f"{color_start}{status}{color_end} - {result['test']}")
            if not result['passed']:
                print(f"      Reason: {result['message']}")

        # Print summary
        print("\n" + "="*80)
        print(f"Total Tests: {self.tests_run}")
        print(f"✓ Passed: {self.tests_passed}")
        print(f"✗ Failed: {self.tests_failed}")

        if self.tests_failed == 0:
            print("\n🎉 All tests passed! 🎉")
        else:
            print(f"\n⚠️  {self.tests_failed} test(s) failed")

        print("="*80 + "\n")


def test_all_games():
    """Run tests on all game files."""
    tester = GameTester()

    print("Starting Game Tests...\n")

    # Test game files exist
    game_files = [
        "Turtle tag.py",
        "Quiz_game.py",
        "maze_turtle2.py",
        "turtle_maze.py",
        "number_game.py",
        "mini_arcade.py",
        "simple_game.py",
        "picture_ASKII.py",
        "background_maze.py",
        "game_launcher.py",
        "high_scores.py",
        "game_config.py",
        "game_utils.py"
    ]

    print("Testing file existence...")
    for game_file in game_files:
        tester.test_file_exists(game_file)

    # Test module imports
    print("\nTesting module imports...")
    importable_modules = [
        "high_scores",
        "game_config",
        "game_utils"
    ]

    for module in importable_modules:
        tester.test_import(module)

    # Test specific functions
    print("\nTesting function availability...")

    function_tests = [
        ("high_scores", "HighScoreManager"),
        ("game_config", "GameConfig"),
        ("game_utils", "TurtleHelper"),
        ("game_utils", "CollisionDetector"),
        ("game_utils", "GameTimer"),
    ]

    for module, function in function_tests:
        tester.test_function_exists(module, function)

    # Test configuration
    print("\nTesting configuration system...")
    try:
        from game_config import GameConfig
        config = GameConfig()
        assert config.get("global", "player_name") is not None
        tester.tests_run += 1
        tester.tests_passed += 1
        tester.test_results.append({
            'test': 'Configuration system',
            'passed': True,
            'message': 'Working'
        })
    except Exception as e:
        tester.tests_run += 1
        tester.tests_failed += 1
        tester.test_results.append({
            'test': 'Configuration system',
            'passed': False,
            'message': str(e)
        })

    # Test high scores
    print("\nTesting high score system...")
    try:
        from high_scores import HighScoreManager
        manager = HighScoreManager("test_scores.json")
        manager.add_score("turtle_tag", 50.5, "TestPlayer")
        assert manager.get_best_score("turtle_tag") is not None
        os.remove("test_scores.json")  # Cleanup
        tester.tests_run += 1
        tester.tests_passed += 1
        tester.test_results.append({
            'test': 'High score system',
            'passed': True,
            'message': 'Working'
        })
    except Exception as e:
        tester.tests_run += 1
        tester.tests_failed += 1
        tester.test_results.append({
            'test': 'High score system',
            'passed': False,
            'message': str(e)
        })

    # Print results
    tester.print_results()

    return tester.tests_failed == 0


def demo_utilities():
    """Demonstrate utility functions."""
    print("\n" + "="*80)
    print("UTILITY DEMONSTRATION".center(80))
    print("="*80 + "\n")

    # Demo GameTimer
    print("1. GameTimer Demo")
    print("-" * 40)

    from game_utils import GameTimer

    timer = GameTimer()
    timer.start()
    print("Timer started...")

    time.sleep(1)
    print(f"After 1 second: {timer.get_elapsed():.2f}s")

    timer.pause()
    print("Timer paused...")
    time.sleep(1)
    print(f"After pause (should be same): {timer.get_elapsed():.2f}s")

    timer.resume()
    time.sleep(1)
    print(f"After resume + 1s: {timer.get_elapsed():.2f}s")
    print(f"Formatted: {timer.format_time()}")

    # Demo ScoreTracker
    print("\n2. ScoreTracker Demo")
    print("-" * 40)

    from game_utils import ScoreTracker

    score = ScoreTracker()
    print(f"Initial score: {score.get_score()}")

    score.add_points(100)
    print(f"After adding 100: {score.get_score()}")

    score.increase_multiplier(0.5)
    score.add_points(100)
    print(f"After adding 100 with 1.5x multiplier: {score.get_score()}")

    score.reset()
    print(f"After reset: {score.get_score()}")
    print(f"High score: {score.get_high_score()}")

    # Demo CollisionDetector
    print("\n3. CollisionDetector Demo")
    print("-" * 40)

    from game_utils import CollisionDetector

    cd = CollisionDetector()

    dist = cd.distance(0, 0, 3, 4)
    print(f"Distance from (0,0) to (3,4): {dist}")

    collision = cd.circle_collision(0, 0, 5, 3, 4, 3)
    print(f"Circle (0,0,r=5) collides with (3,4,r=3): {collision}")

    inside = cd.point_in_rectangle(5, 5, 0, 0, 10, 10)
    print(f"Point (5,5) inside rect (0,0,10x10): {inside}")

    print("\n" + "="*80 + "\n")


def show_game_info():
    """Display information about each game."""
    print("\n" + "="*80)
    print("GAME INFORMATION".center(80))
    print("="*80 + "\n")

    games = [
        {
            'name': 'Turtle Tag (Enhanced)',
            'file': 'Turtle tag.py',
            'features': ['Power-ups', 'Difficulty levels', 'Score tracking', 'High scores'],
            'controls': 'Arrow keys to move, W/S for turbo'
        },
        {
            'name': 'Python Quiz Game',
            'file': 'Quiz_game.py',
            'features': ['15 questions', 'Speed bonuses', 'Explanations', 'Grading'],
            'controls': 'Text input'
        },
        {
            'name': 'Maze Runner (Advanced)',
            'file': 'maze_turtle2.py',
            'features': ['Collision detection', 'Timer', 'Win condition'],
            'controls': 'Arrow keys'
        },
        {
            'name': 'Mega Mini Arcade',
            'file': 'mini_arcade.py',
            'features': ['7 games in one', 'Hangman', 'Memory Match', 'Math Challenge'],
            'controls': 'Various'
        },
        {
            'name': 'Game Launcher',
            'file': 'game_launcher.py',
            'features': ['Menu system', 'Game browser', 'Statistics', 'Help'],
            'controls': 'Number selection'
        }
    ]

    for i, game in enumerate(games, 1):
        print(f"{i}. {game['name']}")
        print(f"   File: {game['file']}")
        print(f"   Features: {', '.join(game['features'])}")
        print(f"   Controls: {game['controls']}")
        print()

    print("="*80 + "\n")


def main():
    """Main test menu."""
    while True:
        print("\n" + "="*80)
        print("GAME TESTING & DEMO SUITE".center(80))
        print("="*80)
        print("\n[1] Run all tests")
        print("[2] Demo utility functions")
        print("[3] Show game information")
        print("[4] Check dependencies")
        print("[Q] Quit")
        print("\n" + "="*80)

        choice = input("\nSelect option: ").strip().lower()

        if choice == "1":
            test_all_games()
            input("\nPress Enter to continue...")

        elif choice == "2":
            demo_utilities()
            input("\nPress Enter to continue...")

        elif choice == "3":
            show_game_info()
            input("\nPress Enter to continue...")

        elif choice == "4":
            print("\nChecking dependencies...")
            print("-" * 40)

            deps = [
                ("turtle", "Turtle graphics (built-in)"),
                ("random", "Random numbers (built-in)"),
                ("time", "Time functions (built-in)"),
                ("json", "JSON support (built-in)"),
                ("PIL", "Pillow (for background images) - Optional"),
                ("cv2", "OpenCV (for ASCII webcam) - Optional")
            ]

            for module, description in deps:
                try:
                    __import__(module)
                    print(f"✓ {module:15} - {description}")
                except ImportError:
                    print(f"✗ {module:15} - {description} (NOT INSTALLED)")

            print("\n" + "-" * 40)
            input("\nPress Enter to continue...")

        elif choice == "q":
            print("\nGoodbye!")
            break

        else:
            print("\n❌ Invalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    main()
