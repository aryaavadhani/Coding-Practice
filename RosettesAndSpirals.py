# RosettesAndSpirals.py
import turtle
t=turtle.Pen()
t.penup()
t.speed(0)
turtle.bgcolor('black')
sides = int(turtle.numinput("Number of sides",
            "How many sides in your spiral?", 7, 2, 12))
colors = ["red", "yellow", "blue", "green", "orange", "purple", "magenta",
          "violet" ,"indigo", "pink", "brown", "grey"]
for m in range(1,100):
    t.forward(m*4)
    t.width(m/25+1)
    position = t.position()
    heading = t.heading()

    if (m % 2 == 0):
        for n in range(sides):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.circle(m/4)
            t.right(360/sides - 2)
            t.penup()
    else:
        for n in range(3,m):
            t.pendown()
            t.pencolor(colors[n%sides])
            t.forward(n*2/3)
            t.right(360/sides - 2)
            t.penup()
    t.setpos(position)
    t.setheading(heading)
    t.left(360/sides + 2)
    print(position, heading)
