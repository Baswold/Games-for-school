import turtle as t
import time

screen = t.Screen()
screen.bgcolor("white")
screen.title("Maze Game")
screen.setup(800, 600)

# Store wall segments for collision detection
wall_segments = []
game_over = False
start_time = None

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

    # Store outer wall segments
    # Top wall
    maze_drawer.setheading(0)
    start = maze_drawer.position()
    maze_drawer.forward(600)
    wall_segments.append((start, maze_drawer.position()))

    # Right wall
    maze_drawer.right(90)
    start = maze_drawer.position()
    maze_drawer.forward(500)
    wall_segments.append((start, maze_drawer.position()))

    # Bottom wall
    maze_drawer.right(90)
    start = maze_drawer.position()
    maze_drawer.forward(600)
    wall_segments.append((start, maze_drawer.position()))

    # Left wall (with opening for start)
    maze_drawer.right(90)
    start = maze_drawer.position()
    maze_drawer.forward(200)
    wall_segments.append((start, maze_drawer.position()))
    maze_drawer.penup()
    maze_drawer.forward(50)  # Opening for start
    maze_drawer.pendown()
    start = maze_drawer.position()
    maze_drawer.forward(250)
    wall_segments.append((start, maze_drawer.position()))

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

    # Draw all the walls and store segments
    for wall in walls:
        x, y, length, direction = wall
        maze_drawer.penup()
        maze_drawer.goto(x, y)
        maze_drawer.setheading(direction)
        maze_drawer.pendown()
        start = maze_drawer.position()
        maze_drawer.forward(length)
        wall_segments.append((start, maze_drawer.position()))

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

# Collision detection function
def check_collision(new_x, new_y):
    """Check if a position collides with any wall."""
    collision_distance = 15  # Detection radius

    for wall_start, wall_end in wall_segments:
        # Calculate distance from point to line segment
        x1, y1 = wall_start
        x2, y2 = wall_end

        # Vector from wall start to end
        wall_dx = x2 - x1
        wall_dy = y2 - y1

        # Vector from wall start to player
        player_dx = new_x - x1
        player_dy = new_y - y1

        # Calculate the closest point on the line segment
        wall_length_squared = wall_dx * wall_dx + wall_dy * wall_dy

        if wall_length_squared == 0:
            # Wall is a point
            distance = ((new_x - x1) ** 2 + (new_y - y1) ** 2) ** 0.5
        else:
            # Parameter t represents where along the line segment the closest point is
            t = max(0, min(1, (player_dx * wall_dx + player_dy * wall_dy) / wall_length_squared))

            # Closest point on the line segment
            closest_x = x1 + t * wall_dx
            closest_y = y1 + t * wall_dy

            # Distance from player to closest point
            distance = ((new_x - closest_x) ** 2 + (new_y - closest_y) ** 2) ** 0.5

        if distance < collision_distance:
            return True

    return False

def check_win():
    """Check if player has reached the finish."""
    global game_over, start_time
    if player.distance(175, -25) < 20:
        game_over = True
        elapsed_time = time.time() - start_time

        # Display victory message
        victory = t.Turtle()
        victory.hideturtle()
        victory.penup()
        victory.goto(0, 0)
        victory.color("green")
        victory.write(f"YOU WIN!\nTime: {elapsed_time:.1f} seconds",
                     align="center", font=("Arial", 24, "bold"))
        return True
    return False

# Movement functions with collision detection
def move_up():
    if game_over:
        return
    new_x, new_y = player.xcor(), player.ycor() + 25
    if not check_collision(new_x, new_y):
        player.setheading(90)
        player.forward(25)
        check_win()

def move_down():
    if game_over:
        return
    new_x, new_y = player.xcor(), player.ycor() - 25
    if not check_collision(new_x, new_y):
        player.setheading(270)
        player.forward(25)
        check_win()

def move_left():
    if game_over:
        return
    new_x, new_y = player.xcor() - 25, player.ycor()
    if not check_collision(new_x, new_y):
        player.setheading(180)
        player.forward(25)
        check_win()

def move_right():
    if game_over:
        return
    new_x, new_y = player.xcor() + 25, player.ycor()
    if not check_collision(new_x, new_y):
        player.setheading(0)
        player.forward(25)
        check_win()

# Draw the maze
draw_maze()
create_start_and_finish()

# Create player
player = create_player()

# Start the timer
start_time = time.time()

# Set up key bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Add instructions
instructions = t.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -280)
instructions.color("blue")
instructions.write("Use arrow keys to reach the red finish!",
                  align="center", font=("Arial", 12, "normal"))

# Keep the window open
screen.exitonclick()