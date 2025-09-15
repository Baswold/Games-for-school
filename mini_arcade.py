import random as r #import stuff
import turtle as t
from time import sleep
coin = 0
inputed = 0 #base variables that i will use later. I tend to add to here as i need a new variable.
maybe = 0
choice = " "
num = 0
guess = 0
again = " "
def welcome(): 
    '''This is the simple WLECOME thing that leads the game.'''
    print("welcome to the mini arcade! where you can play not one, not two, but THREE games!!")
    for i in range(3):
        print("welcome!")
    start()

def coin_flip():
    '''this is the coin flip game. It uses random.'''
    maybe = input("you picked Coin Flip! Press enter to flip! (write 'stop' to exit)")
    choice = ""
    while choice != "stop":
        coin = r.randint(1, 3)
        if coin == 1:
            print("heads!")
        else:
            print("Tails!")
        choice = input("press enter to flip again! (write 'stop' to exit)")


def start():
    inputed = input("pick a game! 1 for Coin flip. 2 for Number guess. 3 for etch and sketch.")
    if int(inputed) == 1:
        coin_flip()
    elif int(inputed) == 2:
        number_guess()
    elif int(inputed) == 3:
        etch_scetch()

def number_guess():
    print("you picked Number Guess. Guess a number between 1 and 10 to win!")
    input("Press enter to start!")
    choice = 0
    num = r.randint(1, 10)
    
    while choice != "stop":
        print(num)
        guess = int(input("input guess: "))
        if guess == num:
            print("you guessed it! the number was", num)
            choice = "stop"
            break
        elif guess > num:
            print("to high! try again!")
        else:
            print("too low! Try again!")
    again = input("Play again? y/n")
    if again == "y":
        number_guess()
    else:
        start()


def etch_scetch():
    screen = t.Screen()
    pen = t.Turtle()
    pen.speed(0)

    def exit_program():
        screen.bye()
        start()
    
    screen.onkey(lambda: pen.forward(10), "Up")
    screen.onkey(lambda: pen.backward(10), "Down")
    screen.onkey(lambda: pen.left(90), "Left")
    screen.onkey(lambda: pen.right(90), "Right")
    screen.onkey(lambda: exit_program(), "q")
    pen.penup()
    pen.goto(-200, 200)
    pen.write("use arrow keys to direct Turtle, 'q' to exit.", font=("Arial", 16, "normal"))
    sleep(2)
    pen.clear()
    pen.goto(0, 0)
    pen.pendown()

    screen.listen()
    screen.mainloop()



welcome()