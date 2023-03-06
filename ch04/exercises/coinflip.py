import turtle
import random


window = turtle.Screen()
window.bgcolor("lightblue")

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green")

leonardo.goto(0,0)

height = turtle.window_height() / 2
width = turtle.window_width() / 2

while True:
    if leonardo.xcor() > width or leonardo.xcor() < -(width) or leonardo.ycor() > height or leonardo.ycor() < -(height):
        turtle.Screen().bye()
        break
    leonardo.forward(50)
    coinflip = random.randrange(0,2)
    if coinflip == 0:
       coinflip = "Heads"
    else:
       coinflip = "Tails"

    if coinflip == "Heads":
       leonardo.left(90)
    else:
       leonardo.right(90)

