import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import turtle as t

from Tower import Tower
from Disc import Disc


# def draw_on_canvas(canvas, color):
#     canvas.create_rectangle(20, 20, 80, 80, fill=color)
#
# # Create the main Tkinter window
# root = tk.Tk()
# root.title("Multiple Canvases Example")
#
# # Create and pack the first canvas
# canvas1 = tk.Canvas(root, width=100, height=100, bg="white")
# canvas1.pack(side=tk.LEFT)
# draw_on_canvas(canvas1, "red")
#
# # Create and pack the second canvas
# canvas2 = tk.Canvas(root, width=100, height=100, bg="white")
# canvas2.pack(side=tk.RIGHT)
# draw_on_canvas(canvas2, "blue")
#
# # Create and pack additional canvases as needed
# git
# # Start the Tkinter event loop
# root.mainloop()


# def draw_rectangle(canvas, disc_number):
#     # TODO

def start_action():
    discNumber = 0
    try:
        discNumber = entry.getint(entry.get())
        print(discNumber)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    # Filling with discs
    prepareDisks(discNumber)

    # Start recursive game
    startRecursiveGame(discNumber)

    # Start iterative game
    startIterativeGame(discNumber)


def quit_action():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()


def prepareDisks(discNumber):
    if discNumber == 0:
        return

    for i in range(discNumber, 0, -1):
        tower1.push(Disc(i, canvas1))
        tower4.push(Disc(i, canvas2))


def startRecursiveGame(discNumber):
    recursiveHanoi(discNumber, tower1, tower2, tower3)


def recursiveHanoi(n, from_, with_, to_):  # n -> number of Disc: int
    if n > 0:
        recursiveHanoi(n - 1, from_, to_, with_)
        to_.push(from_.pop())
        # counter_label[0] += 1  # Increment the counter when a movement occurs
        # update_counter(counter_label[0])
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
        print("2 empty")
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


def startIterativeGame(discNumber):
    iterativeHanoi(discNumber, tower4, tower5, tower6)


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

tower1 = Tower(-200, recursiveScreen)
tower2 = Tower(0, recursiveScreen)
tower3 = Tower(200, recursiveScreen)

tower4 = Tower(-200, iterativeScreen)
tower5 = Tower(0, iterativeScreen)
tower6 = Tower(200, iterativeScreen)

root.mainloop()
