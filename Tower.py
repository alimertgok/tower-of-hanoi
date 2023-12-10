import turtle as t


# from turtle import *


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

    def __init__(self, n, turtle):
        self.turtle = t.Turtle()
        self.n = n

    def draw_tower(self):
        self.turtle.penup()
        self.turtle.hideturtle()
        self.turtle.speed(100)
        self.turtle.goto(-400 + (self.n * 400), 0)
        self.turtle.shape("square")
        self.turtle.shapesize(20, 0.5)
        self.turtle.showturtle()


my_screen = t.Screen()
my_screen.screensize(250, 200)


turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()

tower0 = Tower(0, turtle1)
tower0.draw_tower()

tower1 = Tower(1, turtle2)
tower1.draw_tower()

tower2 = Tower(2, turtle3)
tower2.draw_tower()

t.hideturtle()

t.mainloop()
