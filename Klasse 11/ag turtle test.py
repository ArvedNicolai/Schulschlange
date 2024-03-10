import turtle

# edit this line to control where window appears
turtle.setup(width=500, height=500, startx=-1, starty=0)

window = turtle.Screen()

i = 0
while (i<5):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

    turtle.left(90)
    turtle.forward(100)

    turtle.left(90)
    turtle.forward(100)
    i += 1
window.exitonclick()


