import turtle as t
import random
import math

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def draw_pos1(): # 원 그림을 그리는 draw_pos 함수
    while t.ycor() > 0:
        t.forward(15)
        t.right(3)
    
def draw_pos2(): # 포물선 그림을 그리는 draw_pos 함수
    x = t.xcor()
    y = t.ycor()
    angle = t.heading()
    v = 70 # 발사 속도

    #t.stamp()
    tm=0 #시간변수 초기화
    
    while True:
        X = (v * math.cos(angle*math.pi/180)) * tm
        Y = (v * math.sin(angle*math.pi/180)) * tm - (9.8*tm*tm*(1/2))
        nx = x + int(X)
        ny = y + int(Y)
        if ny >= 0:
            t.goto(nx, ny)
            #t.stamp()
            tm = tm + 0.1
        else:
            break
        
def fire():
    ang = t.heading()
    draw_pos2()
    d = t.distance(target, 0)
    t.sety(random.randint(10, 100))
    if d <= 35:
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
    else:
        t.color("red")
        t.write("Bed!", False, "center", ("", 15))
    t.color("black")
    t.goto(-200, 10)
    t.setheading(ang)


t.goto(-300, 0)
t.down()
t.goto(350, 0)

target = random.randint(50, 300)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 30, -2)
t.down()
t.goto(target + 30, -2)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")

t.listen()
