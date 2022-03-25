import turtle as t
import random

t.colormode(255)
colors = [(211, 154, 97), (52, 107, 132), (176, 78, 34), (238, 246, 243), (200, 142, 33), (116, 155, 171), (124, 79, 98), (122, 175, 157)]
tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.setpos(-200,-200)
tim.speed("fastest")
for _ in range(1,101):
    tim.pencolor(colors[random.randint(0,7)])
    tim.dot(20)
    tim.forward(50)
    if _ % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()
screen = t.Screen()
