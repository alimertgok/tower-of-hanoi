class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n * 1.5, 2)  # (vertical length, horizontal length, outline)
        self.fillcolor(min(1.0, n / 6.0), 0, max(0, 1 - n / 6.0))
        self.st()