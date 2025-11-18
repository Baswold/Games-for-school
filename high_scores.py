"""
High Score Tracking System
Persistent storage and management of game high scores
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class HighScoreManager:
    """Manages high scores for multiple games with persistent storage."""

    def __init__(self, scores_file: str = "high_scores.json"):
        """
        Initialize the high score manager.

        Args:
            scores_file: Path to the JSON file storing scores
        """
        self.scores_file = scores_file
        self.scores = self._load_scores()

    def _load_scores(self) -> Dict:
        """Load scores from JSON file or create new structure."""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                print("Warning: Could not load scores file, creating new one.")
                return self._create_empty_structure()
        else:
            return self._create_empty_structure()

    def _create_empty_structure(self) -> Dict:
        """Create empty score structure for all games."""
        return {
            "turtle_tag": {
                "game_name": "Turtle Tag",
                "score_type": "time_survived",
                "unit": "seconds",
                "higher_is_better": True,
                "scores": []
            },
            "quiz_game": {
                "game_name": "Quiz Game",
                "score_type": "points",
                "unit": "points",
                "higher_is_better": True,
                "scores": []
            },
            "maze_runner": {
                "game_name": "Maze Runner (Advanced)",
                "score_type": "completion_time",
                "unit": "seconds",
                "higher_is_better": False,
                "scores": []
            },
            "maze_challenge": {
                "game_name": "Maze Challenge",
                "score_type": "completion_time",
                "unit": "seconds",
                "higher_is_better": False,
                "scores": []
            },
            "number_guess": {
                "game_name": "Number Guessing Game",
                "score_type": "attempts",
                "unit": "attempts",
                "higher_is_better": False,
                "scores": []
            }
        }

    def _save_scores(self):
        """Save scores to JSON file."""
        try:
            with open(self.scores_file, 'w') as f:
                json.dump(self.scores, f, indent=2)
        except IOError as e:
            print(f"Error saving scores: {e}")

    def add_score(self, game_id: str, score: float, player_name: str = "Player"):
        """
        Add a new score entry.

        Args:
            game_id: Identifier for the game
            score: The score value
            player_name: Name of the player
        """
        if game_id not in self.scores:
            print(f"Warning: Unknown game ID '{game_id}'")
            return

        score_entry = {
            "player": player_name,
            "score": score,
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        }

        self.scores[game_id]["scores"].append(score_entry)

        # Sort scores (best first)
        higher_is_better = self.scores[game_id]["higher_is_better"]
        self.scores[game_id]["scores"].sort(
            key=lambda x: x["score"],
            reverse=higher_is_better
        )

        # Keep only top 10
        self.scores[game_id]["scores"] = self.scores[game_id]["scores"][:10]

        self._save_scores()

    def get_top_scores(self, game_id: str, limit: int = 10) -> List[Dict]:
        """
        Get top scores for a game.

        Args:
            game_id: Identifier for the game
            limit: Maximum number of scores to return

        Returns:
            List of score entries
        """
        if game_id not in self.scores:
            return []

        return self.scores[game_id]["scores"][:limit]

    def get_best_score(self, game_id: str) -> Optional[float]:
        """
        Get the best score for a game.

        Args:
            game_id: Identifier for the game

        Returns:
            Best score value or None if no scores exist
        """
        scores = self.get_top_scores(game_id, limit=1)
        return scores[0]["score"] if scores else None

    def is_high_score(self, game_id: str, score: float) -> bool:
        """
        Check if a score qualifies as a top 10 high score.

        Args:
            game_id: Identifier for the game
            score: The score to check

        Returns:
            True if it's a high score
        """
        if game_id not in self.scores:
            return False

        current_scores = self.scores[game_id]["scores"]

        # If less than 10 scores, it's always a high score
        if len(current_scores) < 10:
            return True

        higher_is_better = self.scores[game_id]["higher_is_better"]
        worst_score = current_scores[-1]["score"]

        if higher_is_better:
            return score > worst_score
        else:
            return score < worst_score

    def get_rank(self, game_id: str, score: float) -> int:
        """
        Get the rank a score would have.

        Args:
            game_id: Identifier for the game
            score: The score to rank

        Returns:
            Rank (1-based) or -1 if not in top 10
        """
        if game_id not in self.scores:
            return -1

        higher_is_better = self.scores[game_id]["higher_is_better"]
        all_scores = [s["score"] for s in self.scores[game_id]["scores"]] + [score]

        all_scores.sort(reverse=higher_is_better)
        rank = all_scores.index(score) + 1

        return rank if rank <= 10 else -1

    def display_high_scores(self, game_id: str):
        """
        Display high scores for a game in a formatted way.

        Args:
            game_id: Identifier for the game
        """
        if game_id not in self.scores:
            print(f"No scores available for game: {game_id}")
            return

        game_data = self.scores[game_id]
        scores = game_data["scores"]

        print("\n" + "=" * 70)
        print(f"🏆  HIGH SCORES - {game_data['game_name']}  🏆".center(70))
        print("=" * 70)

        if not scores:
            print("\nNo high scores yet! Be the first to set a record!\n")
        else:
            print(f"\n{'Rank':<6} {'Player':<20} {'Score':<15} {'Date':<20}")
            print("-" * 70)

            for i, entry in enumerate(scores, 1):
                rank_symbol = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                score_str = f"{entry['score']:.2f} {game_data['unit']}"
                print(f"{rank_symbol:<6} {entry['player']:<20} {score_str:<15} {entry['date']:<20}")

        print("=" * 70 + "\n")

    def display_all_high_scores(self):
        """Display high scores for all games."""
        print("\n" + "=" * 80)
        print("🏆  ALL HIGH SCORES  🏆".center(80))
        print("=" * 80 + "\n")

        for game_id in self.scores:
            game_data = self.scores[game_id]
            scores = game_data["scores"][:3]  # Show top 3 for overview

            print(f"{game_data['game_name']}:")

            if not scores:
                print("  No scores yet")
            else:
                for i, entry in enumerate(scores, 1):
                    rank_symbol = "🥇" if i == 1 else "🥈" if i == 2 else "🥉"
                    score_str = f"{entry['score']:.2f} {game_data['unit']}"
                    print(f"  {rank_symbol} {entry['player']}: {score_str}")

            print()

        print("=" * 80 + "\n")

    def clear_scores(self, game_id: Optional[str] = None):
        """
        Clear scores for a game or all games.

        Args:
            game_id: Game to clear, or None to clear all
        """
        if game_id:
            if game_id in self.scores:
                self.scores[game_id]["scores"] = []
                self._save_scores()
                print(f"Cleared scores for {self.scores[game_id]['game_name']}")
        else:
            for gid in self.scores:
                self.scores[gid]["scores"] = []
            self._save_scores()
            print("Cleared all scores")

    def export_to_text(self, output_file: str = "high_scores.txt"):
        """
        Export all high scores to a readable text file.

        Args:
            output_file: Path to output text file
        """
        try:
            with open(output_file, 'w') as f:
                f.write("=" * 80 + "\n")
                f.write("HIGH SCORES - SCHOOL GAMES COLLECTION\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 80 + "\n\n")

                for game_id, game_data in self.scores.items():
                    f.write(f"\n{game_data['game_name']}\n")
                    f.write("-" * 80 + "\n")

                    if not game_data["scores"]:
                        f.write("No scores recorded\n")
                    else:
                        for i, entry in enumerate(game_data["scores"], 1):
                            score_str = f"{entry['score']:.2f} {game_data['unit']}"
                            f.write(f"{i}. {entry['player']}: {score_str} ({entry['date']})\n")

                    f.write("\n")

            print(f"Scores exported to {output_file}")
        except IOError as e:
            print(f"Error exporting scores: {e}")


# Example usage and testing
if __name__ == "__main__":
    # Create manager
    manager = HighScoreManager()

    # Add some test scores
    print("Adding test scores...")
    manager.add_score("turtle_tag", 45.2, "Alice")
    manager.add_score("turtle_tag", 62.8, "Bob")
    manager.add_score("turtle_tag", 38.1, "Charlie")

    manager.add_score("quiz_game", 85, "Alice")
    manager.add_score("quiz_game", 95, "Bob")
    manager.add_score("quiz_game", 70, "Charlie")

    manager.add_score("maze_runner", 24.5, "Alice")
    manager.add_score("maze_runner", 19.2, "Bob")
    manager.add_score("maze_runner", 31.7, "Charlie")

    # Display scores
    print("\nDisplaying individual game scores:")
    manager.display_high_scores("turtle_tag")
    manager.display_high_scores("quiz_game")
    manager.display_high_scores("maze_runner")

    # Display all scores
    manager.display_all_high_scores()

    # Export to text
    manager.export_to_text()

    print("\nHigh score system ready!")
