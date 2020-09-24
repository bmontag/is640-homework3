from turtle import Turtle

pen = Turtle()
pen.pensize(2)
screen = pen.getscreen()

pen.pencolor("blue")
pen.left(45)
pen.forward(100)
pen.right(90)
pen.forward(200)
pen.right(90)
pen.forward(100)

pen.penup()
pen.setposition(0, 0)
pen.pendown()

pen.pencolor("red")
pen.right(90)
pen.forward(100)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(100)

screen.mainloop()