import turtle as t
import random

def stars(x, y, n):
    t.up()
    t.setpos(x, y)
    t.down()

    # Set the turtle's pen color
    t.pencolor(random.choice(["red", "green", "blue"]))
    # Set the star's fill color
    t.fillcolor(random.choice(["red", "green", "blue"]))
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

while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    n = random.randint(1, 10)
    stars(x, y, n)
