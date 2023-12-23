import turtle as t

class Tower(list):


    def __init__(self, x, canvas):
        self.x = x

        self.stick = t.RawTurtle(canvas, shape="square")
        self.stick.penup()
        self.stick.shapesize(15, 0.5, 2)  # (vertical length, horizontal length, outline)
        self.stick.speed(1000)
        self.stick.setx(self.x)

    def push(self, disc):
        disc.setx(self.x)
        disc.sety(-150 + 15 * len(self))
        self.append(disc)

    def pop(self):
        disc = list.pop(self)
        disc.sety(150)
        return disc