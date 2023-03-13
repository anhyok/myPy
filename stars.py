import turtle as t
import random

def stars(x, y):
    t.setpos(x, y)

    # Set the turtle's pen color
    t.pencolor("yellow")
    # Set the star's fill color
    t.fillcolor("yellow")
    # Begin filling the star
    t.begin_fill()
    # Draw the star
    for i in range(6):
        t.forward(100)
        t.left(144)
    # End filling the star
    t.end_fill()

t.bgcolor("black")
t.speed(20)

for n in range(10):
    x = random.randint(-500, 500)
    y = random.randint(-500, 500)
    stars(x, y)
