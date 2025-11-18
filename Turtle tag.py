import turtle as t
import time
import random

'''This is an enhanced game of Turtle Tag with power-ups and scoring!'''

# Game setup
screen = t.Screen()
screen.title("Turtle Tag - Enhanced Edition")
screen.setup(width=800, height=600)
screen.bgcolor("lightgreen")

# Get difficulty
difficulty = screen.textinput("Difficulty", "Choose a difficulty: easy, medium, hard")
final = 0
time_of_play = 0
elapsed_time = 0
score = 0
power_up_active = False
power_up_timer = 0
invincible = False
speed_boost = False

# Set chase speed based on difficulty
if difficulty == "hard":
    final = 60
    chase_speed = 12
elif difficulty == "medium":
    final = 150
    chase_speed = 10
elif difficulty == "easy":
    final = 300
    chase_speed = 8
else:
    screen.textinput("Error", "That's not an option... defaulting to medium")
    final = 150
    chase_speed = 10

# Create player turtle
pen = t.Turtle()
pen.shape("turtle")
pen.color("blue")
pen.penup()
pen.speed(0)

# Create chaser
clone = pen.clone()
clone.color("red")
clone.goto(-100, -100)

# Score display
score_display = t.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-380, 260)
score_display.color("darkblue")

# Status display
status_display = t.Turtle()
status_display.hideturtle()
status_display.penup()
status_display.goto(0, 260)
status_display.color("purple")

# Power-up list
power_ups = []

def create_power_up():
    """Create a random power-up on the screen."""
    if len(power_ups) < 3:  # Max 3 power-ups at once
        power_up = t.Turtle()
        power_up.shape("circle")
        power_up.penup()
        power_up.speed(0)

        # Random type
        power_type = random.choice(["invincible", "speed", "freeze", "teleport"])

        if power_type == "invincible":
            power_up.color("gold")
            power_up.shapesize(0.8, 0.8)
        elif power_type == "speed":
            power_up.color("cyan")
            power_up.shapesize(0.7, 0.7)
        elif power_type == "freeze":
            power_up.color("lightblue")
            power_up.shapesize(0.9, 0.9)
        else:  # teleport
            power_up.color("magenta")
            power_up.shapesize(0.6, 0.6)

        # Random position
        x = random.randint(-350, 350)
        y = random.randint(-250, 250)
        power_up.goto(x, y)

        power_up.type = power_type
        power_ups.append(power_up)

        # Schedule next power-up
        screen.ontimer(create_power_up, random.randint(5000, 10000))

def check_power_up_collision():
    """Check if player collected a power-up."""
    global score, invincible, speed_boost, power_up_timer

    for power_up in power_ups[:]:  # Create a copy to iterate
        if pen.distance(power_up) < 20:
            score += 50

            if power_up.type == "invincible":
                invincible = True
                power_up_timer = time.time()
                clone.color("orange")
                status_display.clear()
                status_display.write("⭐ INVINCIBLE! ⭐", align="center", font=("Arial", 14, "bold"))

            elif power_up.type == "speed":
                speed_boost = True
                power_up_timer = time.time()
                status_display.clear()
                status_display.write("🚀 SPEED BOOST! 🚀", align="center", font=("Arial", 14, "bold"))

            elif power_up.type == "freeze":
                # Freeze chaser for 3 seconds
                screen.ontimer(lambda: None, 3000)  # Pause chase updates
                status_display.clear()
                status_display.write("❄️ CHASER FROZEN! ❄️", align="center", font=("Arial", 14, "bold"))

            elif power_up.type == "teleport":
                # Teleport player to random location
                new_x = random.randint(-300, 300)
                new_y = random.randint(-200, 200)
                pen.goto(new_x, new_y)
                status_display.clear()
                status_display.write("🌀 TELEPORTED! 🌀", align="center", font=("Arial", 14, "bold"))

            # Remove collected power-up
            power_up.hideturtle()
            power_ups.remove(power_up)

def update_power_up_status():
    """Update power-up effects timer."""
    global invincible, speed_boost, power_up_timer

    current_time = time.time()

    # Check if power-up duration expired (5 seconds)
    if (invincible or speed_boost) and current_time - power_up_timer > 5:
        invincible = False
        speed_boost = False
        clone.color("red")
        status_display.clear()

def chase():
    """Make the clone chase the pen."""
    global score, elapsed_time

    # Update power-up status
    update_power_up_status()

    # Check for power-up collection
    check_power_up_collision()

    # Update time and score
    elapsed_time = time.time() - time_of_play
    score = int(elapsed_time * 10)  # Base score on survival time

    # Update score display
    score_display.clear()
    score_display.write(f"Score: {score} | Time: {elapsed_time:.1f}s", font=("Arial", 12, "normal"))

    # Chase logic
    if not invincible:
        clone.setheading(clone.towards(pen))
        clone.forward(chase_speed)

    screen.ontimer(chase, final)

def update_boundaries():
    """Keep player within boundaries."""
    x, y = pen.xcor(), pen.ycor()

    # Bounce off walls
    if x > 380:
        pen.setx(380)
    elif x < -380:
        pen.setx(-380)

    if y > 250:
        pen.sety(250)
    elif y < -280:
        pen.sety(-280)

# User movement code with speed boost
def move_forward():
    move_distance = 15 if speed_boost else 10
    pen.forward(move_distance)
    update_boundaries()

def move_left():
    pen.left(10)

def move_right():
    pen.right(10)

def move_backward():
    move_distance = 15 if speed_boost else 10
    pen.backward(move_distance)
    update_boundaries()

# Turbo mode (hold shift + arrow)
def turbo_forward():
    pen.forward(20)
    update_boundaries()

def turbo_backward():
    pen.backward(20)
    update_boundaries()

# Bind keys
screen.onkey(move_forward, "Up")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_backward, "Down")
screen.onkey(turbo_forward, "w")
screen.onkey(turbo_backward, "s")
screen.listen()

# Display instructions
instructions = t.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(0, -280)
instructions.color("darkblue")
instructions.write("Arrow keys to move | W/S for turbo | Collect power-ups!",
                  align="center", font=("Arial", 10, "normal"))

# Start game
time_of_play = time.time()
chase()
create_power_up()

# Main game loop
game_over = False
while not game_over:
    elapsed_time = time.time() - time_of_play

    # Check for collision (only if not invincible)
    if clone.distance(pen) < 15 and not invincible:
        game_over = True

        # Final score
        final_score = int(elapsed_time * 10) + sum(50 for _ in power_ups)

        # Game over message
        game_over_display = t.Turtle()
        game_over_display.hideturtle()
        game_over_display.penup()
        game_over_display.goto(0, 0)
        game_over_display.color("red")
        game_over_display.write(f"TAGGED!\n\nFinal Score: {final_score}\nSurvival Time: {elapsed_time:.1f}s",
                               align="center", font=("Arial", 24, "bold"))

        print(f"Game Over! You survived for {elapsed_time:.1f} seconds!")
        print(f"Final Score: {final_score}")

        # Try to save high score
        try:
            from high_scores import HighScoreManager
            manager = HighScoreManager()
            manager.add_score("turtle_tag", elapsed_time, "Player")
            if manager.is_high_score("turtle_tag", elapsed_time):
                print("NEW HIGH SCORE!")
        except:
            pass  # High score system not available

        break

    time.sleep(0.01)  # Small delay to prevent CPU overuse

screen.exitonclick()
