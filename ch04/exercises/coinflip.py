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

def is_in_screen(window, leonardo):
   coinflip = random.randrange(0,2)
   if coinflip == 0:
       coinflip = "Heads"
   else:
       coinflip = "Tails"

   if coinflip == "Heads":
       leonardo.left(90)
   else:
       leonardo.right(90)

   leonardo.forward(150)

   if leonardo.xcor() > width or leonardo.xcor() < -(width) or leonardo.ycor() > height or leonardo.ycor() < -(height):
      turtle.Screen().bye()
      done = True

while not done:
    is_in_screen(window, leonardo)
 #  is_in_screen(window, leonardo)
  # if done:
   #    break

is_in_screen(window, leonardo)