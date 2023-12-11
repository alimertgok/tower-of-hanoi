import tkinter as tk

def draw_on_canvas(canvas, color):
    canvas.create_rectangle(20, 20, 80, 80, fill=color)

# Create the main Tkinter window
root = tk.Tk()
root.title("Multiple Canvases Example")

# Create and pack the first canvas
canvas1 = tk.Canvas(root, width=100, height=100, bg="white")
canvas1.pack(side=tk.LEFT)
draw_on_canvas(canvas1, "red")

# Create and pack the second canvas
canvas2 = tk.Canvas(root, width=100, height=100, bg="white")
canvas2.pack(side=tk.RIGHT)
draw_on_canvas(canvas2, "blue")

# Create and pack additional canvases as needed

# Start the Tkinter event loop
root.mainloop()
