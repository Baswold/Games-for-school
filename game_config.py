"""
Game Configuration System
Centralized configuration for all games with save/load functionality
"""
import json
import os
from typing import Any, Dict

class GameConfig:
    """
    Manages game configuration settings with persistent storage.
    Provides default values and allows customization per game.
    """

    DEFAULT_CONFIG = {
        # Global Settings
        "global": {
            "sound_enabled": False,
            "music_enabled": False,
            "show_fps": False,
            "debug_mode": False,
            "player_name": "Player",
            "color_scheme": "default"
        },

        # Turtle Tag Settings
        "turtle_tag": {
            "default_difficulty": "medium",
            "power_up_frequency": 7,  # seconds between power-ups
            "max_power_ups": 3,
            "power_up_duration": 5,  # seconds
            "enable_boundaries": True,
            "screen_width": 800,
            "screen_height": 600,
            "chase_speeds": {
                "easy": 8,
                "medium": 10,
                "hard": 12
            },
            "player_color": "blue",
            "chaser_color": "red"
        },

        # Quiz Game Settings
        "quiz_game": {
            "num_questions": 10,
            "random_order": True,
            "speed_bonus_enabled": True,
            "speed_bonus_threshold": 5,  # seconds
            "speed_bonus_points": 5,
            "show_explanations": True,
            "time_per_question": 0,  # 0 = unlimited
            "difficulty_filter": "all"  # all, easy, medium, hard
        },

        # Maze Game Settings
        "maze_runner": {
            "show_timer": True,
            "grid_size": 25,
            "collision_tolerance": 15,
            "player_color": "green",
            "wall_color": "black",
            "background_color": "white",
            "show_path": False,
            "enable_hints": False
        },

        # Number Guessing Settings
        "number_game": {
            "min_number": 1,
            "max_number": 100,
            "max_attempts": 10,
            "show_proximity_hints": True,
            "proximity_threshold": 5,
            "difficulty": "medium"
        },

        # Mini Arcade Settings
        "mini_arcade": {
            "show_statistics": True,
            "enable_all_games": True,
            "default_game": None,
            "color_mode": "full"  # full, basic, mono
        },

        # Display Settings
        "display": {
            "font_family": "Arial",
            "font_size_small": 10,
            "font_size_medium": 12,
            "font_size_large": 16,
            "font_size_title": 24,
            "show_instructions": True,
            "animation_speed": "normal"  # slow, normal, fast
        },

        # High Score Settings
        "high_scores": {
            "enabled": True,
            "auto_save": True,
            "max_entries_per_game": 10,
            "ask_for_name": True,
            "show_on_game_over": True
        },

        # Developer Settings
        "developer": {
            "enable_cheats": False,
            "log_level": "info",  # debug, info, warning, error
            "show_collision_boxes": False,
            "unlock_all_features": False
        }
    }

    def __init__(self, config_file: str = "game_settings.json"):
        """
        Initialize configuration manager.

        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load configuration from file or create default."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded_config = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    return self._merge_configs(self.DEFAULT_CONFIG, loaded_config)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load config file: {e}")
                print("Using default configuration.")
                return self.DEFAULT_CONFIG.copy()
        else:
            # Create default config file
            self._save_config(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()

    def _merge_configs(self, default: Dict, custom: Dict) -> Dict:
        """
        Recursively merge custom config with default config.

        Args:
            default: Default configuration
            custom: Custom configuration

        Returns:
            Merged configuration
        """
        result = default.copy()

        for key, value in custom.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._merge_configs(result[key], value)
            else:
                result[key] = value

        return result

    def _save_config(self, config: Dict = None):
        """
        Save configuration to file.

        Args:
            config: Configuration to save (uses self.config if None)
        """
        config_to_save = config if config is not None else self.config

        try:
            with open(self.config_file, 'w') as f:
                json.dump(config_to_save, f, indent=2)
        except IOError as e:
            print(f"Error saving configuration: {e}")

    def get(self, section: str, key: str = None, default: Any = None) -> Any:
        """
        Get a configuration value.

        Args:
            section: Configuration section (e.g., 'global', 'turtle_tag')
            key: Specific key within section (None to get entire section)
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        if section not in self.config:
            return default

        if key is None:
            return self.config[section]

        return self.config[section].get(key, default)

    def set(self, section: str, key: str, value: Any, save: bool = True):
        """
        Set a configuration value.

        Args:
            section: Configuration section
            key: Key to set
            value: Value to set
            save: Whether to save immediately
        """
        if section not in self.config:
            self.config[section] = {}

        self.config[section][key] = value

        if save:
            self._save_config()

    def reset_section(self, section: str):
        """
        Reset a section to default values.

        Args:
            section: Section to reset
        """
        if section in self.DEFAULT_CONFIG:
            self.config[section] = self.DEFAULT_CONFIG[section].copy()
            self._save_config()

    def reset_all(self):
        """Reset all configuration to defaults."""
        self.config = self.DEFAULT_CONFIG.copy()
        self._save_config()

    def export_config(self, filename: str):
        """
        Export current configuration to a file.

        Args:
            filename: File to export to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.config, f, indent=2)
            print(f"Configuration exported to {filename}")
        except IOError as e:
            print(f"Error exporting configuration: {e}")

    def import_config(self, filename: str):
        """
        Import configuration from a file.

        Args:
            filename: File to import from
        """
        try:
            with open(filename, 'r') as f:
                imported_config = json.load(f)
                self.config = self._merge_configs(self.DEFAULT_CONFIG, imported_config)
                self._save_config()
            print(f"Configuration imported from {filename}")
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error importing configuration: {e}")

    def display_config(self, section: str = None):
        """
        Display configuration in a readable format.

        Args:
            section: Specific section to display (None for all)
        """
        print("\n" + "="*70)
        print("GAME CONFIGURATION".center(70))
        print("="*70 + "\n")

        if section:
            sections = {section: self.config.get(section, {})}
        else:
            sections = self.config

        for sect_name, sect_data in sections.items():
            print(f"\n[{sect_name.upper()}]")
            print("-" * 70)

            if isinstance(sect_data, dict):
                for key, value in sect_data.items():
                    if isinstance(value, dict):
                        print(f"  {key}:")
                        for sub_key, sub_value in value.items():
                            print(f"    {sub_key}: {sub_value}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"  {sect_data}")

        print("\n" + "="*70 + "\n")

    def get_player_name(self) -> str:
        """Get the configured player name."""
        return self.get("global", "player_name", "Player")

    def set_player_name(self, name: str):
        """Set the player name."""
        self.set("global", "player_name", name)


# Convenience function for quick access
_global_config = None

def get_config() -> GameConfig:
    """Get the global configuration instance."""
    global _global_config
    if _global_config is None:
        _global_config = GameConfig()
    return _global_config


# Example usage and configuration editor
def main():
    """Interactive configuration editor."""
    config = GameConfig()

    while True:
        print("\n" + "="*70)
        print("GAME CONFIGURATION EDITOR".center(70))
        print("="*70)
        print("\n[1] View all settings")
        print("[2] View section settings")
        print("[3] Change player name")
        print("[4] Reset section to defaults")
        print("[5] Reset all to defaults")
        print("[6] Export configuration")
        print("[7] Import configuration")
        print("[Q] Quit")
        print("\n" + "="*70)

        choice = input("\nSelect option: ").strip().lower()

        if choice == "1":
            config.display_config()
            input("\nPress Enter to continue...")

        elif choice == "2":
            sections = list(config.DEFAULT_CONFIG.keys())
            print("\nAvailable sections:")
            for i, section in enumerate(sections, 1):
                print(f"[{i}] {section}")

            try:
                sect_num = int(input("\nSelect section number: ")) - 1
                if 0 <= sect_num < len(sections):
                    config.display_config(sections[sect_num])
                    input("\nPress Enter to continue...")
            except ValueError:
                print("Invalid input!")

        elif choice == "3":
            current = config.get_player_name()
            print(f"\nCurrent player name: {current}")
            new_name = input("Enter new player name (or press Enter to keep current): ").strip()
            if new_name:
                config.set_player_name(new_name)
                print(f"Player name updated to: {new_name}")

        elif choice == "4":
            sections = list(config.DEFAULT_CONFIG.keys())
            print("\nAvailable sections:")
            for i, section in enumerate(sections, 1):
                print(f"[{i}] {section}")

            try:
                sect_num = int(input("\nSelect section to reset: ")) - 1
                if 0 <= sect_num < len(sections):
                    config.reset_section(sections[sect_num])
                    print(f"Section '{sections[sect_num]}' reset to defaults!")
            except ValueError:
                print("Invalid input!")

        elif choice == "5":
            confirm = input("Are you sure you want to reset ALL settings? (yes/no): ")
            if confirm.lower() == "yes":
                config.reset_all()
                print("All settings reset to defaults!")

        elif choice == "6":
            filename = input("Enter filename to export to: ").strip()
            if filename:
                config.export_config(filename)

        elif choice == "7":
            filename = input("Enter filename to import from: ").strip()
            if filename:
                config.import_config(filename)

        elif choice == "q":
            print("\nConfiguration saved. Goodbye!")
            break

        else:
            print("\nInvalid choice!")


if __name__ == "__main__":
    main()
