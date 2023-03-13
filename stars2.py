import turtle as t
import random

def stars(x, y, n):
    t.up()
    t.setpos(x, y)
    t.down()

    # Set the turtle's pen color
    t.pencolor("yellow")
    # Set the star's fill color
    t.fillcolor("yellow")
    # Begin filling the star
    t.begin_fill()
    # Draw the star
    for i in range(6):
        t.forward(n*10)
        t.left(144)
    # End filling the star
    t.end_fill()

t.bgcolor("black")
t.speed(20)

for n in range(20):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    stars(x, y, n)
