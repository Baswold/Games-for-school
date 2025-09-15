import turtle as t

screen = t.Screen()
screen.bgcolor("white")
screen.title("Maze Game")
screen.setup(800, 600)

print("This is a maze game!")
print("Use the arrow keys to move the green turtle to the red finish.")
print("You can only move up, down, left, and right.")
print("Avoid hitting the black walls!")

def draw_maze():
    # Set up the drawing turtle
    maze_drawer = t.Turtle()
    maze_drawer.speed(0)
    maze_drawer.pensize(3)
    maze_drawer.color("black")
    
    # Draw outer walls
    maze_drawer.penup()
    maze_drawer.goto(-300, 250)
    maze_drawer.pendown()
    
    # Top wall
    maze_drawer.setheading(0)
    maze_drawer.forward(600)
    
    # Right wall
    maze_drawer.right(90)
    maze_drawer.forward(500)
    
    # Bottom wall
    maze_drawer.right(90)
    maze_drawer.forward(600)
    
    # Left wall (with opening for start)
    maze_drawer.right(90)
    maze_drawer.forward(200)
    maze_drawer.penup()
    maze_drawer.forward(50)  # Opening for start
    maze_drawer.pendown()
    maze_drawer.forward(250)
    
    # Draw inner walls to create maze paths
    walls = [
        # Horizontal walls (x1, y1, length, direction)
        (-250, 200, 150, 0),   # Top horizontal wall
        (-50, 200, 200, 0),    # Top right horizontal
        (-250, 150, 100, 0),   # Upper left horizontal
        (0, 150, 150, 0),      # Upper right horizontal
        (-200, 100, 100, 0),   # Middle left horizontal
        (50, 100, 150, 0),     # Middle right horizontal
        (-250, 50, 200, 0),    # Lower left horizontal
        (100, 50, 100, 0),     # Lower right horizontal
        (-150, 0, 100, 0),     # Bottom middle horizontal
        (100, 0, 100, 0),      # Bottom right horizontal
        
        # Vertical walls
        (-200, 200, 50, 270),  # Upper left vertical
        (-100, 150, 100, 270), # Left middle vertical
        (50, 200, 50, 270),    # Upper right vertical
        (150, 150, 100, 270),  # Right middle vertical
        (-250, 100, 50, 270),  # Lower left vertical
        (0, 100, 50, 270),     # Center vertical
        (200, 100, 100, 270),  # Right vertical
        (-100, 50, 50, 270),   # Bottom left vertical
        (50, 50, 50, 270),     # Bottom center vertical
    ]
    
    # Draw all the walls
    for wall in walls:
        x, y, length, direction = wall
        maze_drawer.penup()
        maze_drawer.goto(x, y)
        maze_drawer.setheading(direction)
        maze_drawer.pendown()
        maze_drawer.forward(length)
    
    # Hide the drawing turtle
    maze_drawer.hideturtle()

def create_start_and_finish():
    # Create start marker (green circle)
    start_marker = t.Turtle()
    start_marker.shape("circle")
    start_marker.color("lightgreen")
    start_marker.penup()
    start_marker.goto(-175, -25)
    start_marker.stamp()
    start_marker.hideturtle()
    
    # Create finish marker (red circle)
    finish_marker = t.Turtle()
    finish_marker.shape("circle")
    finish_marker.color("red")
    finish_marker.penup()
    finish_marker.goto(175, -25)
    finish_marker.stamp()
    finish_marker.hideturtle()

def create_player():
    # Create player turtle
    player = t.Turtle()
    player.shape("turtle")
    player.color("green")
    player.penup()
    player.goto(-175, -25)  # Start position
    player.speed(1)
    return player

# Movement functions
def move_up():
    player.setheading(90)
    player.forward(25)

def move_down():
    player.setheading(270)
    player.forward(25)

def move_left():
    player.setheading(180)
    player.forward(25)

def move_right():
    player.setheading(0)
    player.forward(25)

# Draw the maze
draw_maze()
create_start_and_finish()

# Create player
player = create_player()

# Set up key bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Keep the window open
screen.exitonclick()