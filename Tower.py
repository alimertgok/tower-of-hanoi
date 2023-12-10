import turtle
from turtle import *


# class Tower:
#     pensize(15)
#
#     def __init__(self, x, y, width, height, angle):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.angle = angle
#
#     def drawTower(self):
#         for i in range(3):
#             penup()
#             goto(self.x + (i * 300), self.y)
#             pendown()
#
#             forward(self.width)
#             backward(self.height)
#             right(self.angle)
#             forward(self.width)
#
#
# tower_init = Tower(-500, -500, 200, 200, 270)
#
# tower_init.drawTower()
#
# mainloop()

class Tower:

    my_screen = Screen()
    my_screen.screensize(250,200)

    for i in range(3):
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.speed(100)
        t.goto(-400 + (i * 400), 0)
        t.shape("square")
        t.shapesize(20, 0.5)
        t.showturtle()

    mainloop()