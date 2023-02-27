import turtle
import random


window = turtle.Screen()
window.bgcolor("lightblue")

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green")

leonardo.goto(0,0)



while 1 == 1:
    if leonardo.xcor() > 500 or leonardo.xcor() < -500 or leonardo.ycor() > 500 or leonardo.ycor() < -500:
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

window.exitonclick()