from turtle import *


class Tower:
    pensize(15)

    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle

    def drawTower(self):
        for i in range(3):
            penup()
            goto(self.x + (i * 300), self.y)
            pendown()

            forward(self.width)
            backward(self.height)
            right(self.angle)
            forward(self.width)


tower_init = Tower(-500, -500, 200, 200, 270)

tower_init.drawTower()

mainloop()
