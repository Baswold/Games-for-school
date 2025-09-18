import turtle as t
import time
'''This is a game of Turtle Tag!'''
pen = t.Turtle() #seting up stuff
screen = t.Screen()
difficulty = screen.textinput("Difficulty", "Choose a difficulty: easy, medium, hard") #use the turtle imput function
final = 0
time_of_play = 0
elapsed_time = 0
if difficulty == "hard":
    final = 60
elif difficulty == "medium":
    final = 150
elif difficulty == "easy":
    final = 300
else: 
    screen.textinput("Error", "thats not an option...")

screen.title("Turtle Tag")
pen.shape("turtle")
pen.color("blue")

clone = pen.clone() #making a clone of the turtle
clone.color("red")

def chase(): #make a functio for chasing
    
    clone.setheading(clone.towards(pen)) #make the clone go have its forward heading ponited at the pen
    clone.forward(10) #makes it MOVE!
   
    screen.ontimer(chase, final) #the timer thing. it makes it call the function lots


#user movment code:
def user():
    def forward():
        pen.forward(10)
    def left():
        pen.left(90)
        pen.forward(10)
    def right():
        pen.right(90)
        pen.forward(10)
    def back():
        pen.backward(10)
    screen.onkey(lambda: pen.forward(10), "Up")
    screen.onkey(lambda: pen.left(10), "Left")
    screen.onkey(lambda: pen.right(10), "Right")
    screen.onkey(lambda: pen.backward(10), "Down")
    screen.listen()

time_of_play =time.time()  
user() #call functions
chase()




while True:
    elapsed_time = time.time() - time_of_play
    if clone.distance(pen) < 15 and time_of_play - elapsed_time < 15: #if the distance between the two turtles is less than 15 (pixels)
         clone.goto(0, -0)


screen.exitonclick()