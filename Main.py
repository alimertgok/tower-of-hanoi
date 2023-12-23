import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import turtle as t
import time

from Tower import Tower
from Disc import Disc

def printRecursiveTime(elapsedTime):

    recursiveTimeTurtle.write(f"Time elapsed: {elapsedTime:.3f} seconds", font=("Arial", 16, "bold"))

def printIterativeTime(elapsedTime):

    iterativeTimeTurtle.write(f"Time elapsed: {elapsedTime:.3f} seconds", font=("Arial", 16, "bold"))

def start_action():

    global iterativeMoveCounter
    iterativeMoveCounter = 0
    updateIterativeCounter()

    global recursiveMoveCounter
    recursiveMoveCounter = 0
    updateRecursiveCounter()

    recursiveTimeTurtle.clear()
    iterativeTimeTurtle.clear()

    discNumber = 0
    try:
        discNumber = entry.getint(entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    # Filling with discs
    prepareDisks(discNumber)

    recursiveStartTime = time.time()
    startRecursiveGame(discNumber)
    recursiveElapsedTime = time.time() - recursiveStartTime
    printRecursiveTime(recursiveElapsedTime)


    iterativeStartTime = time.time()
    startIterativeGame(discNumber)
    iterativeElapsedTime = time.time() - iterativeStartTime
    printIterativeTime(iterativeElapsedTime)

def quit_action():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

def prepareDisks(discNumber):

    for disc in tower3:
        disc.hideturtle()
    tower3.clear()

    for disc in tower6:
        disc.hideturtle()
    tower6.clear()

    if discNumber == 0:
        return

    for i in range(discNumber, 0, -1):
        tower1.push(Disc(i, canvas1))
        tower4.push(Disc(i, canvas2))


def startRecursiveGame(discNumber):
    recursiveHanoi(discNumber, tower1, tower2, tower3)

def startIterativeGame(discNumber):
    iterativeHanoi(discNumber, tower4, tower5, tower6)

def recursiveHanoi(n, from_, with_, to_):  # n -> number of Disc: int
    if n > 0:
        recursiveHanoi(n - 1, from_, to_, with_)
        to_.push(from_.pop())

        global recursiveMoveCounter
        recursiveMoveCounter = recursiveMoveCounter + 1
        updateRecursiveCounter()

        recursiveHanoi(n - 1, with_, from_, to_)


def iterativeHanoi(discNumber, src, aux, dest):
    numberOfMoves = (2 ** discNumber) - 1

    if discNumber % 2 == 1:

        for i in range(1, (numberOfMoves + 1)):

            if i % 3 == 1:
                moveDisk(src, dest)
            if i % 3 == 2:
                moveDisk(src, aux)
            if i % 3 == 0:
                moveDisk(dest, aux)

    else:

        for i in range(1, (numberOfMoves + 1)):
            if i % 3 == 1:
                moveDisk(src, aux)
            if i % 3 == 2:
                moveDisk(src, dest)
            if i % 3 == 0:
                moveDisk(aux, dest)


def moveDisk(src, dest):
    if not src and not dest:
        return

    elif not dest and src:
        dest.push(src.pop())

    elif not src and dest:
        src.push(dest.pop())

    elif src and dest:
        if src[-1].getR() > dest[-1].getR():
            src.push(dest.pop())
        else:
            dest.push(src.pop())

    global iterativeMoveCounter
    iterativeMoveCounter = iterativeMoveCounter + 1
    updateIterativeCounter()

def updateIterativeCounter():
    global iterativeMoveCounter

    iterativeMovesTurtle.clear()
    iterativeMovesTurtle.write(f"Moves: {iterativeMoveCounter}", font=("Arial", 16, "bold"))

def updateRecursiveCounter():
    global recursiveMoveCounter

    recursiveMovesTurtle.clear()
    recursiveMovesTurtle.write(f"Moves: {recursiveMoveCounter}", font=("Arial", 16, "bold"))


root = tk.Tk()
root.geometry("1300x800")
root.title("Tower Of Hanoi")

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

frame = tk.Frame(root, padx=1, pady=1)
frame.pack(padx=10, pady=10)

# Label and entry for number of disks
label = tk.Label(frame, text="Enter the number of disks:")
label.pack()

# entry widget = textbox that accepts a single line of user input
entry = tk.Entry(frame)
entry.pack()

# Create a "Start" button
start_button = tk.Button(frame, text="Start", command=start_action, width=20, height=1)
start_button.pack(side=tk.TOP, padx=5, pady=5)

# Create a "Quit" button
quit_button = tk.Button(frame, text="Quit", command=quit_action, width=20, height=1)
quit_button.pack(side=tk.TOP, padx=5, pady=5)

canvas1 = tk.Canvas(frame, width=600, height=600, bg="white")
canvas1.place(x=-150, y=-150)
canvas1.pack(side=tk.LEFT)
canvas2 = tk.Canvas(frame, width=600, height=600, bg="white")
canvas2.place(x=150, y=150)
canvas2.pack(side=tk.RIGHT)

# Playgrounds for solving algorithms
recursiveScreen = t.TurtleScreen(canvas1)
iterativeScreen = t.TurtleScreen(canvas2)

# Titles for Algorithms
recursiveText = t.RawTurtle(recursiveScreen)
recursiveText.penup()
recursiveText.hideturtle()
recursiveText.speed(10)
recursiveText.goto(-50, 280)
recursiveText.pendown()
recursiveText.pencolor("red")
recursiveText.write("Recursive Solution", font=("Arial", 16, "bold"))

recursiveMovesTurtle = t.RawTurtle(canvas=recursiveScreen, visible=False)
recursiveMovesTurtle.speed(100)
recursiveMovesTurtle.penup()
recursiveMovesTurtle.goto(-290, -220)
recursiveMoveCounter = 0
recursiveMovesTurtle.write(f"Moves: {recursiveMoveCounter}", font=("Arial", 16, "bold"))


recursiveTimeTurtle = t.RawTurtle(canvas=recursiveScreen, visible=False)
recursiveTimeTurtle.speed(100)
recursiveTimeTurtle.penup()
recursiveTimeTurtle.goto(-290, -250)

iterativeText = t.RawTurtle(iterativeScreen)
iterativeText.penup()
iterativeText.hideturtle()
iterativeText.speed(10)
iterativeText.goto(-50, 280)
iterativeText.pendown()
iterativeText.pencolor("blue")
iterativeText.write("Iterative Solution", font=("Arial", 16, "bold"))

iterativeMovesTurtle = t.RawTurtle(canvas=iterativeScreen, visible=False)
iterativeMovesTurtle.speed(100)
iterativeMovesTurtle.penup()
iterativeMovesTurtle.goto(-290, -220)
iterativeMoveCounter = 0
iterativeMovesTurtle.write(f"Moves: {iterativeMoveCounter}", font=("Arial", 16, "bold"))

iterativeTimeTurtle = t.RawTurtle(canvas=iterativeScreen, visible=False)
iterativeTimeTurtle.speed(100)
iterativeTimeTurtle.penup()
iterativeTimeTurtle.goto(-290, -250)


# Draw Towers
tower1 = Tower(-200, recursiveScreen)
tower2 = Tower(0, recursiveScreen)
tower3 = Tower(200, recursiveScreen)

tower4 = Tower(-200, iterativeScreen)
tower5 = Tower(0, iterativeScreen)
tower6 = Tower(200, iterativeScreen)

root.mainloop()
