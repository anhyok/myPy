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

def rocket(x, y):
    t.up()
    t.setpos(x, y)
    t.down()

    # Set the turtle's pen color
    t.pencolor("white")
    # Set the rocket's fill color
    t.fillcolor("red")
    # Begin filling the rocket
    t.begin_fill()
    # Draw the rocket
    t.right(90)
    t.forward(50)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(50)
    # End filling the rocket
    t.end_fill()

t.bgcolor("black")
t.speed(20)

while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    n = random.randint(1, 10)
    stars(x, y, n)

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    rocket(x, y)
