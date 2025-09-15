import random
import time

def rock_paper_scissors():
    """A simple rock-paper-scissors game against the computer"""
    choices = ['rock', 'paper', 'scissors']
    
    print("🎮 Rock Paper Scissors Game!")
    print("=" * 30)
    
    # Simulate multiple rounds
    for round_num in range(1, 4):
        print(f"\nRound {round_num}:")
        
        # Computer choice
        computer_choice = random.choice(choices)
        
        # Simulate player choice (random for demo)
        player_choice = random.choice(choices)
        
        print(f"Player chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            result = "Player wins!"
        else:
            result = "Computer wins!"
        
        print(f"Result: {result}")
        time.sleep(1)  # Pause for effect
    
    print("\n🎯 Game Over! Thanks for playing!")

def dice_roll_game():
    """A simple dice rolling game"""
    print("\n🎲 Dice Roll Adventure!")
    print("=" * 25)
    
    total_score = 0
    
    for roll in range(1, 6):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_total = dice1 + dice2
        total_score += roll_total
        
        print(f"Roll {roll}: {dice1} + {dice2} = {roll_total}")
        
        if roll_total == 12:
            print("🎉 Double sixes! Bonus points!")
            total_score += 10
        elif roll_total == 2:
            print("😅 Snake eyes! Unlucky!")
        
        time.sleep(0.5)
    
    print(f"\n🏆 Final Score: {total_score}")
    
    if total_score >= 40:
        print("🌟 Excellent! You're a dice master!")
    elif total_score >= 30:
        print("👍 Good job! Nice rolling!")
    else:
        print("🎲 Keep practicing!")

if __name__ == "__main__":
    print("🎮 Welcome to the Mini Game Collection!")
    print("=" * 40)
    
    rock_paper_scissors()
    dice_roll_game()
    
    print("\n✨ Thanks for playing! ✨")