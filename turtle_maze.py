import turtle as t
import time

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("lightblue")
screen.title("Turtle Maze Challenge")

print("this is a game where you have to get the turtle to the end of the maze.") #print an introduction
print("use the arrow keys to move the turtle.") #print instructions
print("you can only move up, down, left, and right.") #print instructions
print("you can only move in straight lines.") #print instructions

# Game state
game_won = False
start_time = None   

def draw_maze():
    t.penup()
    t.goto(-200, 200)  # Start from top-left corner
    t.pendown()
    t.speed(0)
    
    # Draw the maze pattern
    t.width(2)  # Make walls more visible
    
    # Starting point
    t.penup()
    t.goto(-180, 160)
    t.setheading(0)
    t.pendown()
    
    # Main corridors (following the pattern from the image)
    t.forward(320)  # Top horizontal line
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(280)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(280)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(280)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(280)
    
    # Add inner walls
    t.penup()
    t.goto(-100, 160)
    t.pendown()
    t.setheading(270)
    t.forward(60)
    
    t.penup()
    t.goto(20, 160)
    t.pendown()
    t.forward(60)
    
    t.penup()
    t.goto(-100, 20)
    t.pendown()
    t.forward(60)
    
    t.penup()
    t.goto(20, 20)
    t.pendown()
    t.forward(60)
    
    # Reset position for player start
    t.penup()
    t.goto(-160, 140)
    t.setheading(0)
    t.pendown()

# Create player turtle
def create_player():
    player = t.Turtle()
    player.shape("turtle")
    player.color("blue")
    player.penup()
    player.speed(0)
    player.goto(-160, 140)  # Start position
    return player

# Create finish marker
def create_finish():
    finish = t.Turtle()
    finish.shape("circle")
    finish.color("red")
    finish.penup()
    finish.goto(120, -120)  # End position
    finish.shapesize(2, 2)  # Make it bigger
    finish.hideturtle()
    finish.stamp()
    return finish

def check_win():
    """Check if player reached the finish."""
    global game_won, start_time
    if player.distance(120, -120) < 30 and not game_won:
        game_won = True
        elapsed_time = time.time() - start_time

        # Display victory message
        victory = t.Turtle()
        victory.hideturtle()
        victory.penup()
        victory.goto(0, 0)
        victory.color("green")
        victory.write(f"CONGRATULATIONS!\nYou completed the maze!\nTime: {elapsed_time:.1f} seconds",
                     align="center", font=("Arial", 20, "bold"))

# Movement functions
def move_up():
    if not game_won:
        player.setheading(90)
        player.forward(20)
        check_win()

def move_down():
    if not game_won:
        player.setheading(270)
        player.forward(20)
        check_win()

def move_left():
    if not game_won:
        player.setheading(180)
        player.forward(20)
        check_win()

def move_right():
    if not game_won:
        player.setheading(0)
        player.forward(20)
        check_win()

# Call the function to draw the maze
draw_maze()

# Create game elements
player = create_player()
finish = create_finish()

# Add title and instructions
title = t.Turtle()
title.hideturtle()
title.penup()
title.goto(0, 250)
title.color("darkblue")
title.write("Navigate to the RED circle!", align="center", font=("Arial", 16, "bold"))

# Set up controls
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Start timer
start_time = time.time()

screen.exitonclick()