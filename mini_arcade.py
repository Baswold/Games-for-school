import random as r
import turtle as t
from time import sleep, time
import string

# Base variables
coin = 0
inputed = 0
maybe = 0
choice = " "
num = 0
guess = 0
again = " "

def welcome():
    '''Enhanced welcome message for the expanded arcade!'''
    print("\n" + "="*70)
    print("🎮 WELCOME TO THE MEGA MINI ARCADE! 🎮".center(70))
    print("="*70)
    print("\nNow featuring SEVEN awesome games!")
    for i in range(3):
        print("✨ Get ready to play! ✨".center(70))
        sleep(0.3)
    print()
    start()

def coin_flip():
    '''Coin flip game with statistics.'''
    print("\n" + "="*60)
    print("🪙 COIN FLIP GAME 🪙".center(60))
    print("="*60)

    heads_count = 0
    tails_count = 0
    flip_count = 0

    choice = ""
    while choice != "stop":
        coin = r.randint(1, 2)
        flip_count += 1

        if coin == 1:
            print(f"\nFlip #{flip_count}: 🟡 HEADS!")
            heads_count += 1
        else:
            print(f"\nFlip #{flip_count}: 🔵 TAILS!")
            tails_count += 1

        print(f"Statistics: Heads: {heads_count} | Tails: {tails_count}")

        choice = input("\nPress Enter to flip again! (type 'stop' to exit): ")

    print(f"\nFinal Stats: {flip_count} flips - {heads_count} heads, {tails_count} tails")
    start()

def number_guess():
    '''Enhanced number guessing game.'''
    print("\n" + "="*60)
    print("🔢 NUMBER GUESSING GAME 🔢".center(60))
    print("="*60)
    print("Guess a number between 1 and 10 to win!")

    input("\nPress enter to start!")
    choice = 0
    num = r.randint(1, 10)
    attempts = 0

    while choice != "stop":
        guess = int(input("\nInput your guess (1-10): "))
        attempts += 1

        if guess == num:
            print(f"\n🎉 You guessed it in {attempts} attempts! The number was {num}!")
            choice = "stop"
            break
        elif guess > num:
            print("Too high! Try again!")
        else:
            print("Too low! Try again!")

    again = input("\nPlay again? (y/n): ")
    if again.lower() == "y":
        number_guess()
    else:
        start()

def etch_sketch():
    '''Etch-a-sketch drawing game.'''
    screen = t.Screen()
    screen.setup(800, 600)
    screen.bgcolor("lightgray")
    screen.title("Etch-a-Sketch")

    pen = t.Turtle()
    pen.speed(0)
    pen.color("blue")
    pen.pensize(2)

    def exit_program():
        screen.bye()
        start()

    def clear_drawing():
        pen.clear()
        pen.penup()
        pen.home()
        pen.pendown()

    def change_color():
        colors = ["red", "blue", "green", "purple", "orange", "pink", "cyan"]
        pen.color(r.choice(colors))

    def pen_up():
        pen.penup()

    def pen_down():
        pen.pendown()

    screen.onkey(lambda: pen.forward(10), "Up")
    screen.onkey(lambda: pen.backward(10), "Down")
    screen.onkey(lambda: pen.left(90), "Left")
    screen.onkey(lambda: pen.right(90), "Right")
    screen.onkey(exit_program, "q")
    screen.onkey(clear_drawing, "c")
    screen.onkey(change_color, "space")
    screen.onkey(pen_up, "u")
    screen.onkey(pen_down, "d")

    pen.penup()
    pen.goto(-200, 250)
    pen.write("Arrow keys to draw | C=Clear | Space=Color | U/D=Pen Up/Down | Q=Quit",
              font=("Arial", 12, "normal"))
    sleep(2)
    pen.clear()
    pen.goto(0, 0)
    pen.pendown()

    screen.listen()
    screen.mainloop()

def hangman():
    '''Classic hangman word guessing game.'''
    print("\n" + "="*60)
    print("🎯 HANGMAN GAME 🎯".center(60))
    print("="*60)

    words = ["python", "turtle", "arcade", "game", "computer", "programming",
             "keyboard", "screen", "function", "variable", "random"]

    word = r.choice(words)
    guessed = ["_"] * len(word)
    wrong_guesses = []
    max_wrong = 6
    attempts = 0

    print("\nGuess the word! You have 6 wrong guesses allowed.")

    while attempts < max_wrong and "_" in guessed:
        print("\n" + " ".join(guessed))
        print(f"Wrong guesses ({len(wrong_guesses)}/{max_wrong}): {', '.join(wrong_guesses)}")

        letter = input("\nGuess a letter: ").lower()

        if len(letter) != 1 or letter not in string.ascii_lowercase:
            print("Please enter a single letter!")
            continue

        if letter in guessed or letter in wrong_guesses:
            print("You already guessed that letter!")
            continue

        if letter in word:
            print(f"✓ Correct! '{letter}' is in the word!")
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
        else:
            print(f"✗ Wrong! '{letter}' is not in the word.")
            wrong_guesses.append(letter)
            attempts += 1

    print("\n" + "="*60)
    if "_" not in guessed:
        print(f"🎉 YOU WIN! The word was: {word}")
    else:
        print(f"💀 GAME OVER! The word was: {word}")
    print("="*60)

    again = input("\nPlay again? (y/n): ")
    if again.lower() == "y":
        hangman()
    else:
        start()

def memory_match():
    '''Memory matching game.'''
    print("\n" + "="*60)
    print("🧠 MEMORY MATCH GAME 🧠".center(60))
    print("="*60)

    symbols = ["🍎", "🍌", "🍒", "🍇", "🍉", "🍓"]
    cards = symbols * 2
    r.shuffle(cards)

    revealed = [False] * len(cards)
    matches = 0
    attempts = 0

    print("\nFind all matching pairs!")
    print("Cards are numbered 1-12")

    while matches < len(symbols):
        # Display board
        print("\n" + "="*60)
        for i in range(12):
            if revealed[i]:
                print(f"[{cards[i]}]", end=" ")
            else:
                print(f"[{i+1:2d}]", end=" ")
            if (i + 1) % 4 == 0:
                print()

        # Get first card
        try:
            card1 = int(input("\nPick first card (1-12): ")) - 1
            if card1 < 0 or card1 >= 12 or revealed[card1]:
                print("Invalid choice!")
                continue

            # Get second card
            card2 = int(input("Pick second card (1-12): ")) - 1
            if card2 < 0 or card2 >= 12 or revealed[card2] or card1 == card2:
                print("Invalid choice!")
                continue

            attempts += 1

            print(f"\nCard {card1+1}: {cards[card1]}")
            print(f"Card {card2+1}: {cards[card2]}")

            if cards[card1] == cards[card2]:
                print("✓ MATCH!")
                revealed[card1] = True
                revealed[card2] = True
                matches += 1
            else:
                print("✗ No match!")
                sleep(1.5)

        except ValueError:
            print("Please enter valid numbers!")

    print(f"\n🎉 YOU WIN! Completed in {attempts} attempts!")

    again = input("\nPlay again? (y/n): ")
    if again.lower() == "y":
        memory_match()
    else:
        start()

def reaction_time():
    '''Test your reaction time!'''
    print("\n" + "="*60)
    print("⚡ REACTION TIME TEST ⚡".center(60))
    print("="*60)

    print("\nPress Enter as fast as you can when you see 'GO!'")
    input("\nPress Enter when ready...")

    wait_time = r.uniform(1, 4)
    print("\nWait for it...")
    sleep(wait_time)

    print("\n🟢 GO! 🟢")
    start_time = time()

    input()  # Wait for user to press Enter

    reaction = (time() - start_time) * 1000  # Convert to milliseconds

    print(f"\n⚡ Your reaction time: {reaction:.0f} ms")

    if reaction < 200:
        print("🏆 INCREDIBLE! Lightning fast!")
    elif reaction < 300:
        print("🥇 EXCELLENT! Very quick!")
    elif reaction < 400:
        print("🥈 GOOD! Above average!")
    elif reaction < 500:
        print("🥉 DECENT! Average reflexes!")
    else:
        print("🐌 Keep practicing!")

    again = input("\nTry again? (y/n): ")
    if again.lower() == "y":
        reaction_time()
    else:
        start()

def math_challenge():
    '''Quick math challenge game.'''
    print("\n" + "="*60)
    print("🔢 MATH CHALLENGE 🔢".center(60))
    print("="*60)

    print("\nSolve 10 math problems as fast as you can!")
    input("\nPress Enter to start...")

    correct = 0
    start_time = time()

    for i in range(10):
        num1 = r.randint(1, 20)
        num2 = r.randint(1, 20)
        operation = r.choice(["+", "-", "*"])

        if operation == "+":
            answer = num1 + num2
        elif operation == "-":
            answer = num1 - num2
        else:  # multiplication
            answer = num1 * num2

        try:
            user_answer = int(input(f"\nQuestion {i+1}: {num1} {operation} {num2} = "))
            if user_answer == answer:
                print("✓ Correct!")
                correct += 1
            else:
                print(f"✗ Wrong! Answer was {answer}")
        except ValueError:
            print(f"✗ Invalid input! Answer was {answer}")

    elapsed = time() - start_time

    print("\n" + "="*60)
    print(f"Score: {correct}/10 correct")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Average: {elapsed/10:.1f} seconds per problem")
    print("="*60)

    again = input("\nPlay again? (y/n): ")
    if again.lower() == "y":
        math_challenge()
    else:
        start()

def start():
    '''Main menu with all game options.'''
    print("\n" + "="*70)
    print("🎮 GAME MENU 🎮".center(70))
    print("="*70)
    print("\n[1] 🪙  Coin Flip")
    print("[2] 🔢  Number Guess")
    print("[3] 🎨  Etch-a-Sketch")
    print("[4] 🎯  Hangman")
    print("[5] 🧠  Memory Match")
    print("[6] ⚡  Reaction Time Test")
    print("[7] 🔢  Math Challenge")
    print("[Q] 🚪  Quit Arcade")
    print("\n" + "="*70)

    inputed = input("\nPick a game (1-7) or Q to quit: ").strip().lower()

    if inputed == "1":
        coin_flip()
    elif inputed == "2":
        number_guess()
    elif inputed == "3":
        etch_sketch()
    elif inputed == "4":
        hangman()
    elif inputed == "5":
        memory_match()
    elif inputed == "6":
        reaction_time()
    elif inputed == "7":
        math_challenge()
    elif inputed == "q":
        print("\n" + "="*70)
        print("Thanks for playing the Mega Mini Arcade!".center(70))
        print("Come back soon! 🎮".center(70))
        print("="*70 + "\n")
    else:
        print("\n❌ Invalid choice! Please pick 1-7 or Q.")
        sleep(1)
        start()

# Start the arcade!
if __name__ == "__main__":
    welcome()
