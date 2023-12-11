from turtle import *


class Disc(Turtle):
    def __init__(self, n, turtle):
        Turtle.__init__(self, shape="square", visible=False)
        self.penup()
        self.speed(10)
        self.shapesize(1.5, n * 1.5, 2)
        self.fillcolor(min(1.0, n / 6.0), 0, max(0, 1 - n / 6.0))
        self.showturtle()
        self.n = n
        self.turtle = turtle

    def draw_disc(self, num_discs):
        tower = []
        for i in range(num_discs):
            self.turtle = Disc(num_discs - i)
            self.turtle.goto(-650, i * 30)  # Adjust the spacing as needed
            tower.append(self.turtle)

        return tower

drawing_area = Screen()
drawing_area.bgcolor('white')
drawing_area.title("Demo")

drawing_area.setup(width=1920, height=1080)

Disc.draw_disc(5)

mainloop()
