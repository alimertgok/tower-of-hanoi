import turtle as t


class Disc(t.RawTurtle):
    def __init__(self, r, canvas):
        t.RawTurtle.__init__(self, canvas=canvas, shape="square", visible=True)
        self.r = r
        self.speed(5)
        self.pu()
        self.shapesize(0.7, r, 1)  # (vertical length, horizontal length, outline)
        self.fillcolor(min(1.0, r / 6.0), 0, max(0, 1 - r / 6.0))
        self.st()

    def getR(self):
        return self.r
