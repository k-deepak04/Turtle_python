import turtle
t =turtle.Turtle()
t.color("white")
turtle.speed(1)
wn =turtle.Screen()
wn.bgcolor("black") 
t.hideturtle()
t.begin_fill()
t.fillcolor("cyan")
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

