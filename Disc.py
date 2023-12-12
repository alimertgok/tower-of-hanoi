import turtle as t

class Disc(t.Turtle):
    def __init__(self, r):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, r * 1.5, 2)  # (vertical length, horizontal length, outline)
        self.fillcolor(min(1.0, r / 6.0), 0, max(0, 1 - r / 6.0))
        self.st()