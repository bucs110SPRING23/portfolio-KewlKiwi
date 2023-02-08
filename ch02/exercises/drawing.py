import turtle


sides = int(input("How many sides? "))
length = int(input("What is the length for each side? "))
shapeAngle = 360 / sides
max = int(360/shapeAngle)

turtle1 = turtle.Turtle()
window = turtle.Screen()
turtle1.shape("turtle")
turtle1.color("blue")
turtle1.speed(1)
turtle1.down()

for i in range(max):
    turtle1.forward(length)
    turtle1.left(shapeAngle)




window.exitonclick()
