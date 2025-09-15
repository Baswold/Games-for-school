import random

def play_number_guessing_game():
    """A simple number guessing game"""
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            # Give hints when close
            if abs(guess - secret_number) <= 5:
                print("You're getting close!")
                
        except ValueError:
            print("Please enter a valid number!")
            attempts -= 1  # Don't count invalid inputs
    
    else:
        print(f"\n😔 Game over! The number was {secret_number}. Better luck next time!")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y' or play_again == 'yes':
        play_number_guessing_game()

if __name__ == "__main__":
    play_number_guessing_game()