#Part A

import random
import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("red")
turtle2.shape("turtle")
turtle2.color("blue")
turtle1.up()
turtle2.up()
turtle1.goto(-100,20)
turtle2.goto(-100,-20)

#Race 1

x1 = random.randrange(1,101)
x2 = random.randrange(1,101)

turtle1.forward(x1)
turtle2.forward(x2)

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

#Race 2

racelength = random.randrange(20, 50)

for _ in range(racelength):
   x1 = random.randrange(1,11)
   x2 = random.randrange(1,11)

   turtle1.forward(x1)
   turtle2.forward(x2)

turtle1.goto(-100,20)
turtle2.goto(-100,-20)

window.exitonclick()

#Part B

import pygame
import math
pygame.init()
screen = pygame.display.set_mode()
screen.fill("lightblue")
screen_size = screen.get_size()

points = []
num_sides = 3
side_length = 200
xpos = 850
ypos = 500

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)

screen.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 4

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)

screen.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 6

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)

screen.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 10

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)

screen.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 100

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)

screen.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 360

for _ in range(num_sides):
   angle = 360/num_sides
   radians = math.radians(angle * _)
   x = xpos + side_length * math.cos(radians)
   y = ypos + side_length * math.sin(radians)
   points.append([x,y])

pygame.draw.polygon(screen, "purple", points)
pygame.display.flip()

pygame.time.wait(2000)
