# import turtle
#
# drawing_area = turtle.Screen()
# drawing_area.bgcolor('white')
# drawing_area.title("Demo")
#
# drawing_area.setup(width=1920, height=1080)
#
# turtle.mainloop()

import turtle
import tkinter as tk


def on_button_click():
    my_turtle.forward(50)


# Create a Tkinter window
root = tk.Tk()
root.title("Turtle with Tkinter")

# Create a tkinter.Canvas to serve as the drawing canvas for turtle
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create a turtle.TurtleScreen associated with the canvas
turtle_screen = turtle.TurtleScreen(canvas)

# Create a turtle.RawTurtle associated with the turtle screen
my_turtle = turtle.RawTurtle(turtle_screen)
my_turtle.penup()
my_turtle.goto(0, 0)

# Create a button in the Tkinter window
button = tk.Button(root, text="Move Turtle Forward", command=on_button_click)
button.pack()

# Bind the turtle command directly to the Tkinter event
button.bind("<Button-1>", lambda event: my_turtle.forward(50))

# Start the Tkinter event loop
root.mainloop()
