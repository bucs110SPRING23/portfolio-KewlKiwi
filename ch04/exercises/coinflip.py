import turtle
import random


window = turtle.Screen()
window.bgcolor("lightblue")

leonardo = turtle.Turtle()
leonardo.shape("turtle")
leonardo.color("green")

done = False

leonardo.goto(0,0)

height = turtle.window_height() / 2
width = turtle.window_width() / 2

def is_in_screen(w, leonardo):
   if leonardo.xcor() > width or leonardo.xcor() < -(width) or leonardo.ycor() > height or leonardo.ycor() < -(height):
      done = True
      return done

while not done:
    if is_in_screen(window, leonardo):
       turtle.Screen().bye()
       break
    coinflip = random.randrange(0,2)
    if coinflip == 0:
       coinflip = "Heads"
    else:
       coinflip = "Tails"

    if coinflip == "Heads":
       leonardo.left(90)
       leonardo.forward(50)
    else:
       leonardo.right(90)
       leonardo.forward(50)
