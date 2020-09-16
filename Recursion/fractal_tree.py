import turtle

if __name__ == '__main__':
    wn = turtle.Screen()
    wn.bgcolor("yellow")
    me = turtle.Turtle()
    me.speed('fastest')
    me.color('red')
    me.pensize(4)
    me.left(90)
    length = 100
    me.forward(length)


    def fractal_tree(x, le):
        if x == 0:
            return
        else:  # fix this
            angle = 35
            h = me.heading()
            a, b = me.pos()
            me.left(angle)
            me.forward(le)
            fractal_tree(x-1, le/1.5)

            me.goto(a, b)
            me.setheading(h)

            me.right(angle)
            me.forward(le)
            fractal_tree(x - 1, le/1.5)
            me.goto(a, b)

    me.pendown()
    fractal_tree(5, length)
    me.penup()

    wn.exitonclick()