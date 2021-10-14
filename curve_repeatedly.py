import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1920, 1080)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def choose_next_points():
    global index
    begin = index % 4
    end = begin + 4
    points = more_long_points[begin:end]
    index += 1

    return points

def draw_repeatedly_4_points():
    global index
    global p1, p2, p3, p4

    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    p1, p2, p3, p4 = choose_next_points()

    for i in range(0, 100, 2):
        t = i / 100
        dx = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        dy = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((dx, dy))

p1 = (100, 100); p2 = (-50, 400); p3 = (-200, -200); p4 = (400, -50)
running = True

long_points = []

long_points.append(p1)
long_points.append(p2)
long_points.append(p3)
long_points.append(p4)

more_long_points = long_points + long_points[:3]
index = -1

prepare_turtle_canvas()

while running:
    draw_repeatedly_4_points()

turtle.done()