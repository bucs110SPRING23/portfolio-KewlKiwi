import turtle
import random


window = turtle.Screen()
window.bgcolor("lightblue")

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green")

leonardo.goto(0,0)

#print(turtle.screensize())
#print(turtle.window_width)

while 1 == 1:
    if leonardo.xcor() > 100 or leonardo.xcor() < -100 or leonardo.ycor() > 100 or leonardo.ycor() < -100:
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

