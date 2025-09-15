"""Test with an image as the background."""
import turtle as t
from time import sleep
from PIL import Image  # requires Pillow
from PIL.Image import Resampling

# Resize the GIF (change scale as needed)
orig = "background.gif"
scaled = "background_scaled.gif"
scale = 1.5  # 2 = double size, 1.5 = 150%, etc.
img = Image.open(orig)
new_size = (int(img.width * scale), int(img.height * scale))
img = img.resize(new_size, Resampling.LANCZOS)
img.save(scaled, format="GIF")

# Create screen
screen = t.Screen()
screen_width = new_size[0] + 100  # 100 pixels wider than image
screen_height = new_size[1] + 100  # 100 pixels taller than image
screen.setup(width=screen_width, height=screen_height)  # optional: match window to image
screen.bgpic(scaled)
t.penup()
t.goto(-200, 170)

t.pendown()
t.shape("turtle")
t.color("blue")
t.speed(1)
def move_up():
    t.setheading(90)
    t.forward(10)

def move_down():
    t.setheading(270)
    t.forward(10)

def move_left():
    t.setheading(180)
    t.forward(10)

def move_right():
    t.setheading(0)
    t.forward(10)
screen.listen()
screen.onkey(move_up, "Up") 
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.exitonclick()

