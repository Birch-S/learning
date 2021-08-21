import turtle
import math

bob = turtle.Turtle()


def polygon(n, length):
    for i in range(n):
        bob.fd(length)
        bob.lt(360 / n)


def circle(r):
    n = int(2 * math.pi * r / 3)
    length = 2 * math.pi * r / n
    polygon(n, length)


def polyline(n, length, angle):
    for i in range(n):
        bob.fd(length)
        bob.lt(angle / n)


def arc(r, angle):
    s = 2 * math.pi * r * angle / 360
    n = int(s / 3)
    length = s / n
    polyline(n, length, angle)


def flower(m, angle, t):
    r = t / 2 / math.sin(angle / 2)
    for i in range(m):
        arc(r, angle)
        bob.lt(180 - angle)
        arc(r, angle)
        bob.lt(180 + 360 / m - angle)


flower(7, 180 - 360/7 * 2, 200)
turtle.mainloop()
