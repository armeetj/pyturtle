import turtle

SIDE = 200
COLOR = "orange"

turtle.speed(1)
turtle.pencolor(COLOR)
turtle.pensize(5)

turtle.forward(SIDE)
turtle.setheading(90)
turtle.forward(SIDE)
turtle.setheading(180)
turtle.forward(SIDE)
turtle.setheading(-90)
turtle.forward(SIDE)
