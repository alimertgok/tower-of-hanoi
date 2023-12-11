import turtle


class Disc:
    def __init__(self, no_of_disc, x, y, width, height, turtle):
        self.no_of_disc = no_of_disc
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.turtle = turtle


    def draw_disc(self, n):
        turtle.penup()
        turtle.goto(self.x - size * 5, self.y)
        turtle.pendown()
        turtle.forward(size * 10)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)
        turtle.forward(size * 10)
        turtle.left(90)
        turtle.forward(self.height)
        turtle.left(90)

disc = Disc(5, 5, 10, 10, 10)
disc.draw_disc(5)

turtle.mainloop()