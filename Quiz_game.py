"""
Python Quiz Game - Test your Python knowledge!
"""
import random
import time

# Quiz questions with multiple choice answers
QUIZ_QUESTIONS = [
    {
        "question": "What does 'def' do in Python?",
        "options": {
            "A": "It starts a function definition",
            "B": "It tells the computer to sing",
            "C": "It deletes a file",
            "D": "It defines a variable"
        },
        "correct": "A",
        "explanation": "'def' is used to define functions in Python."
    },
    {
        "question": "Which of these is NOT a valid Python data type?",
        "options": {
            "A": "int",
            "B": "string",
            "C": "float",
            "D": "bool"
        },
        "correct": "B",
        "explanation": "The correct data type is 'str', not 'string'."
    },
    {
        "question": "What does the 'print()' function do?",
        "options": {
            "A": "Prints to a printer",
            "B": "Displays output to the console",
            "C": "Creates a copy of a variable",
            "D": "Saves a file"
        },
        "correct": "B",
        "explanation": "print() displays output to the console/terminal."
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": {
            "A": "//",
            "B": "/* */",
            "C": "#",
            "D": "--"
        },
        "correct": "C",
        "explanation": "# is used for single-line comments in Python."
    },
    {
        "question": "What will 'print(5 == 5)' output?",
        "options": {
            "A": "5",
            "B": "True",
            "C": "False",
            "D": "Error"
        },
        "correct": "B",
        "explanation": "== is the equality operator, and 5 equals 5, so it returns True."
    },
    {
        "question": "Which of these is used to create a loop in Python?",
        "options": {
            "A": "loop",
            "B": "repeat",
            "C": "for",
            "D": "cycle"
        },
        "correct": "C",
        "explanation": "'for' and 'while' are used to create loops in Python."
    },
    {
        "question": "What does 'len()' function return?",
        "options": {
            "A": "The length of an object",
            "B": "A random number",
            "C": "The type of an object",
            "D": "Nothing"
        },
        "correct": "A",
        "explanation": "len() returns the number of items in an object like a string or list."
    },
    {
        "question": "Which operator is used for exponentiation in Python?",
        "options": {
            "A": "^",
            "B": "**",
            "C": "exp()",
            "D": "pow"
        },
        "correct": "B",
        "explanation": "** is the exponentiation operator (e.g., 2**3 = 8)."
    },
    {
        "question": "What is the correct way to import a module?",
        "options": {
            "A": "include math",
            "B": "using math",
            "C": "import math",
            "D": "require math"
        },
        "correct": "C",
        "explanation": "'import' is the keyword used to import modules in Python."
    },
    {
        "question": "Which of these is a mutable data type?",
        "options": {
            "A": "tuple",
            "B": "string",
            "C": "list",
            "D": "int"
        },
        "correct": "C",
        "explanation": "Lists are mutable (can be changed), while tuples and strings are immutable."
    },
    {
        "question": "What does 'range(5)' generate?",
        "options": {
            "A": "Numbers from 1 to 5",
            "B": "Numbers from 0 to 5",
            "C": "Numbers from 0 to 4",
            "D": "Numbers from 1 to 4"
        },
        "correct": "C",
        "explanation": "range(5) generates numbers from 0 to 4 (5 is not included)."
    },
    {
        "question": "Which keyword is used to handle exceptions?",
        "options": {
            "A": "catch",
            "B": "try",
            "C": "handle",
            "D": "except"
        },
        "correct": "B",
        "explanation": "'try' and 'except' are used together for exception handling."
    },
    {
        "question": "What will 'print(type([]))' output?",
        "options": {
            "A": "<class 'array'>",
            "B": "<class 'list'>",
            "C": "<class 'tuple'>",
            "D": "<class 'dict'>"
        },
        "correct": "B",
        "explanation": "[] creates an empty list, so type() returns <class 'list'>."
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": {
            "A": "add()",
            "B": "insert()",
            "C": "append()",
            "D": "push()"
        },
        "correct": "C",
        "explanation": "append() adds an item to the end of a list."
    },
    {
        "question": "What is the output of 'print(bool(\"\"))'?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "None",
            "D": "Error"
        },
        "correct": "B",
        "explanation": "An empty string is considered False in boolean context."
    }
]

def display_question(q_num, question_data):
    """Display a single question with its options."""
    print(f"\n{'='*60}")
    print(f"Question {q_num + 1} of {len(QUIZ_QUESTIONS)}")
    print(f"{'='*60}")
    print(f"\n{question_data['question']}\n")

    for key, value in sorted(question_data['options'].items()):
        print(f"  {key}) {value}")
    print()

def get_user_answer():
    """Get and validate user's answer."""
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer in ['A', 'B', 'C', 'D']:
            return answer
        print("Invalid input! Please enter A, B, C, or D.")

def play_quiz(num_questions=10, random_order=True):
    """Main quiz game function."""
    print("\n" + "="*60)
    print("Welcome to the Python Quiz Game!")
    print("="*60)
    print(f"\nYou will be asked {num_questions} questions about Python.")
    print("Each correct answer is worth 10 points.")
    print("Good luck!\n")

    input("Press Enter to start...")

    # Select questions
    questions = QUIZ_QUESTIONS.copy()
    if random_order:
        random.shuffle(questions)
    questions = questions[:num_questions]

    score = 0
    total_time = 0

    for i, question in enumerate(questions):
        start_time = time.time()

        display_question(i, question)
        answer = get_user_answer()

        elapsed = time.time() - start_time
        total_time += elapsed

        # Check answer
        if answer == question['correct']:
            points = 10
            if elapsed < 5:  # Bonus for quick answers
                points += 5
                print(f"\n🎉 Correct! (+{points} points - Speed bonus!)")
            else:
                print(f"\n✓ Correct! (+{points} points)")
            score += points
        else:
            print(f"\n✗ Incorrect! The correct answer was {question['correct']}.")
            print(f"   {question['explanation']}")

        print(f"\nCurrent Score: {score}")

        if i < len(questions) - 1:
            time.sleep(1.5)  # Brief pause before next question

    # Final results
    print("\n" + "="*60)
    print("QUIZ COMPLETE!")
    print("="*60)
    print(f"\nFinal Score: {score} out of {num_questions * 10}")
    print(f"Percentage: {(score / (num_questions * 10)) * 100:.1f}%")
    print(f"Total Time: {total_time:.1f} seconds")
    print(f"Average Time per Question: {total_time/num_questions:.1f} seconds")

    # Grade
    percentage = (score / (num_questions * 10)) * 100
    if percentage >= 90:
        grade = "A - Excellent! You're a Python master!"
    elif percentage >= 80:
        grade = "B - Great job! You know your Python well!"
    elif percentage >= 70:
        grade = "C - Good! Keep practicing!"
    elif percentage >= 60:
        grade = "D - Not bad, but there's room for improvement!"
    else:
        grade = "F - Keep learning! Practice makes perfect!"

    print(f"\nGrade: {grade}\n")

    return score

def main():
    """Main entry point for the quiz game."""
    while True:
        score = play_quiz(num_questions=10, random_order=True)

        play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
        if play_again not in ['y', 'yes']:
            print("\nThanks for playing! Keep coding!")
            break

if __name__ == "__main__":
    main()
