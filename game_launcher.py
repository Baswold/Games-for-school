"""
Game Launcher - Central hub for all school games
Launch any game from a beautiful menu interface!
"""
import os
import sys
import subprocess
import time
from datetime import datetime

# ANSI color codes for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Game database
GAMES = {
    '1': {
        'name': 'Turtle Tag',
        'file': 'Turtle tag.py',
        'description': 'A thrilling chase game! Avoid the red turtle for as long as possible.',
        'category': 'Action',
        'difficulty': 'Easy-Hard'
    },
    '2': {
        'name': 'Quiz Game',
        'file': 'Quiz_game.py',
        'description': 'Test your Python knowledge with 15 challenging questions!',
        'category': 'Educational',
        'difficulty': 'Medium'
    },
    '3': {
        'name': 'Maze Runner (Advanced)',
        'file': 'maze_turtle2.py',
        'description': 'Navigate through a complex maze with wall collision detection.',
        'category': 'Puzzle',
        'difficulty': 'Hard'
    },
    '4': {
        'name': 'Maze Challenge',
        'file': 'turtle_maze.py',
        'description': 'A simpler maze for beginners. Find your way to the finish!',
        'category': 'Puzzle',
        'difficulty': 'Easy'
    },
    '5': {
        'name': 'Number Guessing Game',
        'file': 'number_game.py',
        'description': 'Guess the secret number between 1 and 100. You have 10 attempts!',
        'category': 'Logic',
        'difficulty': 'Easy'
    },
    '6': {
        'name': 'Mini Arcade',
        'file': 'mini_arcade.py',
        'description': 'Three games in one! Coin flip, number guess, and etch-a-sketch.',
        'category': 'Variety',
        'difficulty': 'Easy'
    },
    '7': {
        'name': 'Simple Games',
        'file': 'simple_game.py',
        'description': 'Rock-Paper-Scissors and dice rolling games!',
        'category': 'Casual',
        'difficulty': 'Easy'
    },
    '8': {
        'name': 'ASCII Webcam',
        'file': 'picture_ASKII.py',
        'description': 'Turn your webcam into ASCII art! (requires OpenCV)',
        'category': 'Creative',
        'difficulty': 'N/A'
    },
    '9': {
        'name': 'Background Maze',
        'file': 'background_maze.py',
        'description': 'Navigate a turtle with a custom background image.',
        'category': 'Casual',
        'difficulty': 'Easy'
    }
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name != 'nt' else 'cls')

def print_banner():
    """Print a fancy banner."""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║              🎮  SCHOOL GAMES COLLECTION LAUNCHER  🎮                ║
║                                                                      ║
║                    Your Ultimate Gaming Hub!                         ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""
    print(banner)

def print_welcome():
    """Print welcome message."""
    print(f"\n{Colors.YELLOW}Welcome to the Game Launcher!{Colors.ENDC}")
    print(f"{Colors.CYAN}Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.ENDC}")
    print(f"\n{Colors.GREEN}Choose from {len(GAMES)} amazing games below:{Colors.ENDC}\n")

def print_game_list():
    """Print the list of available games with details."""
    print(f"{Colors.BOLD}{'='*76}{Colors.ENDC}")

    for key, game in sorted(GAMES.items()):
        # Color code by category
        if game['category'] == 'Action':
            color = Colors.RED
        elif game['category'] == 'Educational':
            color = Colors.BLUE
        elif game['category'] == 'Puzzle':
            color = Colors.CYAN
        elif game['category'] == 'Logic':
            color = Colors.YELLOW
        else:
            color = Colors.GREEN

        print(f"{Colors.BOLD}[{key}]{Colors.ENDC} {color}{game['name']}{Colors.ENDC}")
        print(f"    {game['description']}")
        print(f"    {Colors.CYAN}Category:{Colors.ENDC} {game['category']}  |  "
              f"{Colors.YELLOW}Difficulty:{Colors.ENDC} {game['difficulty']}")
        print()

    print(f"{Colors.BOLD}{'='*76}{Colors.ENDC}")

def print_menu_options():
    """Print menu options."""
    print(f"\n{Colors.BOLD}Other Options:{Colors.ENDC}")
    print(f"  {Colors.GREEN}[L]{Colors.ENDC} List all games again")
    print(f"  {Colors.GREEN}[S]{Colors.ENDC} Show statistics")
    print(f"  {Colors.GREEN}[H]{Colors.ENDC} Help & Instructions")
    print(f"  {Colors.RED}[Q]{Colors.ENDC} Quit launcher\n")

def show_statistics():
    """Show game statistics."""
    clear_screen()
    print_banner()
    print(f"\n{Colors.BOLD}{Colors.CYAN}📊 Game Statistics{Colors.ENDC}\n")

    # Count by category
    categories = {}
    difficulties = {}

    for game in GAMES.values():
        cat = game['category']
        diff = game['difficulty']

        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1

    print(f"{Colors.BOLD}Games by Category:{Colors.ENDC}")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count} game(s)")

    print(f"\n{Colors.BOLD}Games by Difficulty:{Colors.ENDC}")
    for diff, count in sorted(difficulties.items()):
        print(f"  {diff}: {count} game(s)")

    print(f"\n{Colors.BOLD}Total Games:{Colors.ENDC} {len(GAMES)}")
    print(f"\n{Colors.CYAN}{'='*76}{Colors.ENDC}\n")

    input(f"{Colors.YELLOW}Press Enter to return to menu...{Colors.ENDC}")

def show_help():
    """Show help information."""
    clear_screen()
    print_banner()
    print(f"\n{Colors.BOLD}{Colors.CYAN}❓ Help & Instructions{Colors.ENDC}\n")

    help_text = """
    🎮 How to Use This Launcher:
    ═══════════════════════════════════════════════════════════════════

    1. Browse the game list and choose a game by entering its number (1-9)
    2. The game will launch in a new window or in the terminal
    3. When you exit the game, you'll return to this launcher
    4. Use the menu options to explore different features

    🎯 Game Categories:
    ═══════════════════════════════════════════════════════════════════

    • Action: Fast-paced games that test your reflexes
    • Educational: Learn while you play!
    • Puzzle: Brain-teasing maze and logic challenges
    • Logic: Number and pattern games
    • Casual: Relax and have fun
    • Creative: Unique and artistic experiences

    💡 Tips:
    ═══════════════════════════════════════════════════════════════════

    • Start with Easy difficulty games if you're new
    • Try all categories to find your favorite!
    • Some games require specific libraries (like OpenCV)
    • Arrow keys are commonly used for movement in turtle games
    • Press 'Q' to quit most turtle graphics games

    🛠️ Troubleshooting:
    ═══════════════════════════════════════════════════════════════════

    • If a game doesn't start, check if all dependencies are installed
    • For ASCII Webcam, make sure you have cv2 (OpenCV) installed
    • If a turtle game window doesn't respond, click on it to focus

    """
    print(help_text)
    print(f"{Colors.CYAN}{'='*76}{Colors.ENDC}\n")

    input(f"{Colors.YELLOW}Press Enter to return to menu...{Colors.ENDC}")

def launch_game(game_key):
    """Launch the selected game."""
    if game_key not in GAMES:
        print(f"{Colors.RED}Invalid game selection!{Colors.ENDC}")
        time.sleep(1)
        return

    game = GAMES[game_key]
    game_file = game['file']

    # Check if file exists
    if not os.path.exists(game_file):
        print(f"{Colors.RED}Error: Game file '{game_file}' not found!{Colors.ENDC}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.ENDC}")
        return

    print(f"\n{Colors.GREEN}{Colors.BOLD}🚀 Launching {game['name']}...{Colors.ENDC}")
    print(f"{Colors.CYAN}File: {game_file}{Colors.ENDC}")
    time.sleep(1)

    try:
        # Launch the game using subprocess
        subprocess.run([sys.executable, game_file])
    except Exception as e:
        print(f"{Colors.RED}Error launching game: {e}{Colors.ENDC}")
        input(f"{Colors.YELLOW}Press Enter to continue...{Colors.ENDC}")
        return

    # Game finished
    print(f"\n{Colors.GREEN}Thanks for playing {game['name']}!{Colors.ENDC}")
    time.sleep(2)

def main():
    """Main launcher loop."""
    while True:
        clear_screen()
        print_banner()
        print_welcome()
        print_game_list()
        print_menu_options()

        choice = input(f"{Colors.BOLD}Enter your choice: {Colors.ENDC}").strip().upper()

        if choice in GAMES:
            launch_game(choice)
        elif choice == 'L':
            continue  # Redraw menu
        elif choice == 'S':
            show_statistics()
        elif choice == 'H':
            show_help()
        elif choice == 'Q':
            clear_screen()
            print(f"\n{Colors.CYAN}{Colors.BOLD}Thanks for using the Game Launcher!{Colors.ENDC}")
            print(f"{Colors.YELLOW}Keep gaming and keep learning! 🎮{Colors.ENDC}\n")
            break
        else:
            print(f"{Colors.RED}Invalid choice! Please try again.{Colors.ENDC}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{Colors.CYAN}Launcher interrupted. Goodbye!{Colors.ENDC}\n")
        sys.exit(0)
