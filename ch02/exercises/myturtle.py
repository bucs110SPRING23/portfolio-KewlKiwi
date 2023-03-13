import turtle


turtle1 = turtle.Turtle()
window = turtle.Screen()
turtle1.shape("turtle")
turtle1.color("purple")
turtle1.speed(1)
turtle1.up()
turtle1.goto(50,50)

turtle1.down()
turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)

turtle1.up()
turtle1.goto(-50,-50)
turtle1.color("red")

turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)
turtle1.left(90)
turtle1.forward(50)

window.exitonclick()
