from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n * 1.5, 2)
        self.fillcolor(min(1.0, n / 6.0), 0, max(0, 1 - n / 6.0))
        self.st()

class Tower(list):
    def __init__(self, x):
        self.x = x

    def push(self, d):
        d.setx(self.x)
        d.sety(-150 + 34 * len(self))
        self.append(d)

    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_, counter_label):
    if n > 0:
        hanoi(n - 1, from_, to_, with_, counter_label)
        to_.push(from_.pop())
        counter_label[0] += 1  # Increment the counter when a movement occurs
        update_counter(counter_label[0])
        hanoi(n - 1, with_, from_, to_, counter_label)

def play(num_discs, counter_label):
    onkey(None, "space")
    clear()

    counter = [0]  # Counter to keep track of movements
    counter_label[0] = 0  # Reset the counter label

    try:
        hanoi(num_discs, t1, t2, t3, counter)
        write("Press STOP to Exit", align="center", font=("courier", 16, "bold"))
    except Terminator:
        pass

def num_discs_input():
    if 'num_discs' not in globals():
        # Prompt the user for the number of discs
        while True:
            try:
                num_discs = int(textinput("Number of Discs", "Enter the number of discs:"))
                if num_discs > 0:
                    globals()['num_discs'] = num_discs
                    return num_discs
                else:
                    print("Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    else:
        # Return the stored value if input has already been received
        return num_discs

def update_counter(count):
    counter_label.clear()
    counter_label.write(f"Number of Movements: {count}", align="center", font=("courier", 14, "normal"))

def main():
    global t1, t2, t3
    ht()
    penup()
    goto(0, -255)

    t1 = Tower(-250)
    t2 = Tower(0)
    t3 = Tower(250)

    # Call num_discs_input to get the number of discs
    num_discs = num_discs_input()

    for i in range(num_discs, 0, -1):
        t1.push(Disc(i))

    write("Press SPACE to Start", align="center", font=("courier", 16, "bold"))
    global counter_label  # Make sure we use the global variable
    counter_label = Turtle()
    counter_label.hideturtle()
    counter_label.penup()
    counter_label.goto(0, 240)  # Adjust the position of the counter label
    counter_label.write("Number of Movements: 0", align="center", font=("courier", 14, "normal"))

    onkey(lambda: play(num_discs, [0, counter_label]), "space")
    listen()
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()