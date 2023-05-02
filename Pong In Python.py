# made by ratkinglol 
# to my friends, made by Kasen
# Hey Alex or Kyler, you're the only two friends I have who would think of using this lmao anyways, here it is...
# Also this works on Visual Studio Code, I don't know about others.
# It WILL NOT work on normal python of course
import turtle
import time
import random

# Set up the game window
win = turtle.Screen()
win.title("Pong By ratkinglol")
win.bgcolor("black")
win.setup(width=600, height=400)

# Create the paddles
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-250, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(250, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = -3

# Create the score display
score_a = 0
score_b = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 170)
score.write("Player A: 0  Player B: 0", align="center", font=("Courier", 18, "normal"))

# Move the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Bind the paddle movement to keyboard keys
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collision with top/bottom walls
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    # Check for collision with left/right walls
    if ball.xcor() > 290:
        score_a += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        ball.goto(0, 0)
        ball.dx = -3
        ball.dy = random.uniform(-3, 3)

    if ball.xcor() < -290:
        score_b += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 18, "normal"))
        ball.goto(0, 0)
        ball.dx = 3
        ball.dy = random.uniform(-3, 3)

