from turtle import *
size = 800
minimum = 64
pf = 0.8660254  # pythagoras factor: sqrt(3)/2


def sierpinski(l, x, y):  # fix this code
    if l > minimum:
        l = l/2
        sierpinski(l, x, y)
        sierpinski(l, x + 1, y)
        sierpinski(l, x + l / 2, y + l * pf)
    else:
        goto(x, y)
        pendown()
        begin_fill()
        forward(l)
        left(120)
        forward(l)
        left(120)
        end_fill()
        setheading(0)
        penup()
        goto(x, y)


if __name__ == '__main__':
    penup()
    speed('fastest')
    sierpinski(size, -size / 2, -size * pf / 2.0)
    done()
