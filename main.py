# # def tower_of_hanoi(no_of_disks, from_disk, to_disk, temp):
# #     if no_of_disks == 1:
# #         print("Move disk tower {} to tower {}".format(from_disk, to_disk))
# #         return
# #     tower_of_hanoi(no_of_disks - 1, from_disk, to_disk, temp)
# #     print("Move disk {} from tower {} to tower {}".format(no_of_disks, from_disk, to_disk))
# #     tower_of_hanoi(no_of_disks - 1, temp, to_disk, from_disk)
# #
# # no_of_disks = int(input("How many disks? "))



# from tkinter import *
#
# def start_action():
#     new_window = Tk()    #Toplevel() = new window 'on top' of other windows, linked to bottam window
#                                #Tk() = new independent window
#     old_window.destroy()       #close out of old window
#
# old_window = Tk()
#
# # Create a "Start" button
# start_button = Button(old_window, text="Start", command=start_action)
# start_button.pack(side=LEFT, padx=5)
#
# old_window.mainloop()


import tkinter as tk
from tkinter import messagebox

def start_action():
    # Hide the main page
    frame.pack_forget()

    # Create a new page
    new_page = tk.Frame(main, padx=20, pady=20)
    new_page.pack(padx=10, pady=10)

    # Label and entry for number of disks
    label = tk.Label(new_page, text="Enter the number of disks:")
    label.pack()

    # entry widget = textbox that accepts a single line of user input
    entry = tk.Entry(new_page)
    entry.pack()

    # Button to submit the number of disks
    submit_button = tk.Button(new_page, text="Submit", command=lambda: submit_action(entry.get(), new_page))
    submit_button.pack()

def submit_action(num_disks, new_page):
    try:
        num_disks = int(num_disks)
        messagebox.showinfo("Message", f"You entered {num_disks} disks.")

        # canvas = widget that is used to draw graphs, plots, images in a window

        # Destroy widgets in the current page
        for widget in new_page.winfo_children():
            widget.destroy()

        # Create a canvas
        canvas = tk.Canvas(new_page, width=400, height=300)
        canvas.pack()


    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def quit_action():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        main.destroy()

# Create the main window
main = tk.Tk()
main.title("Tower Of Hanoi Program")

# Create and configure a frame
# frame = a rectangular container to group and hold widgets
frame = tk.Frame(main, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Create a "Start" button
start_button = tk.Button(frame, text="Start", command=start_action)
start_button.pack(side=tk.LEFT, padx=5)

# Create a "Quit" button
quit_button = tk.Button(frame, text="Quit", command=quit_action)
quit_button.pack(side=tk.RIGHT, padx=5)

# Run the Tkinter event loop
main.mainloop()


