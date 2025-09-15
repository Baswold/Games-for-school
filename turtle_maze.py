import turtle as t
screen = t.Screen()

print("this is a game where you have to get the turtle to the end of the maze.") #print an introduction
print("use the arrow keys to move the turtle.") #print instructions
print("you can only move up, down, left, and right.") #print instructions
print("you can only move in straight lines.") #print instructions   

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

# Call the function to draw the maze
draw_maze()
screen.exitonclick()