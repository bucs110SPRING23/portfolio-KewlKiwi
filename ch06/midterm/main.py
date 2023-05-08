import turtle
import math
import random

def background(screen):
    color = "lightgreen"
    screen.bgcolor(color)

def color(donatello):
    donatello.color("black")

def door(donatello):
    donatello.forward(length() / 3.4)
    donatello.left(90)
    donatello.forward(length() / 4)
    donatello.down()
    donatello.fillcolor("brown")
    donatello.begin_fill()
    donatello.right(90)
    donatello.forward(length() / 3.5)
    donatello.left(90)
    donatello.forward(length() / 5)
    donatello.left(90)
    donatello.forward(length() / 3.5)
    donatello.left(90)
    donatello.forward(length() / 5)
    donatello.end_fill()
    donatello.up()
    donatello.right(180)

def house(donatello):
    donatello.down()
    donatello.fillcolor("grey")
    donatello.begin_fill()
    for _ in range(4):
        donatello.left(90)
        donatello.forward(length())
    donatello.end_fill()

    donatello.fillcolor("brown")
    donatello.begin_fill()
    donatello.left(90)
    donatello.forward(length())
    donatello.right(90)
    donatello.forward((0.3*(length()/2)))
    donatello.left(135)
    donatello.forward(math.sqrt((((length()/2) + (0.3*(length()/2)))**2) + (((length()/2) + (0.3*(length()/2)))**2)))
    donatello.left(90)
    donatello.forward(math.sqrt((((length()/2) + (0.3*(length()/2)))**2) + (((length()/2) + (0.3*(length()/2)))**2)))
    donatello.left(135)
    donatello.forward(length() + (0.3*(length()/2)))
    donatello.end_fill()
    donatello.up()
    donatello.right(90)

    windows(donatello)

def initialize():
    screen = turtle.Screen()
    background(screen)
    donatello = turtle.Turtle()
    return donatello

def length():
    length = 123
    return length

def numhouse(donatello):
    donatello.up()
    for _ in range(random.randrange(1,10)):
        house(donatello)
        donatello.goto(randpos())
    
def randpos():
    x = random.randrange(0 - int(turtle.window_width() / 2), int(turtle.window_width() / 2))
    y = random.randrange(0 - int(turtle.window_height() / 2), int(turtle.window_height() / 2))
    return x, y

def shape(donatello):
   donatello.shape("turtle")

def windows(donatello):
    donatello.forward(length() / 6)
    donatello.right(90)
    donatello.forward(length() / 3)
    donatello.down()
    donatello.fillcolor("lightblue")
    donatello.begin_fill()
    for _ in range(4):
        donatello.left(90)
        donatello.forward(length() / 6)
    donatello.end_fill()
    donatello.up()
    donatello.forward(length() / 2)
    donatello.left(90)
    donatello.forward(length() / 4)
    donatello.down()
    donatello.begin_fill()
    for _ in range(4):
        donatello.left(90)
        donatello.forward(length() / 6)
    donatello.end_fill()
    donatello.up()
    door(donatello)

def main():
    donatello = initialize()
    shape(donatello)
    color(donatello)
    numhouse(donatello)

main()