from settings import settings, notes
from mandelbrot import Mandelbrot
from helpers import process_iterations_array, hex_to_rgba

import tkinter as tk
import tkinter.colorchooser as colorchooser

# import the pillow libraries only if pillow is installed
if settings["pil_installed"]:
    from PIL import Image, ImageTk
    from helpers import get_mandelbrot_image

WIDTH = 500
HEIGHT = 500

root = tk.Tk()
root.title("Project Mandelbrot")

# frame for the left side of the program
main_frame = tk.Frame(root)
main_frame.pack(side = tk.LEFT)

# Mode menu
if settings["pil_installed"]:
    # variable containing the mode 
    fast_mode = True

    # frame for the "flip switch"
    flip_switch_frame = tk.Frame(main_frame)
    flip_switch_frame.pack()

    # label for the "flip switch"
    tk.Label(flip_switch_frame, text="Mode:").pack(side=tk.LEFT)

    # function to toggle the fast mode
    def change_mode():
        global fast_mode
        fast_mode = not fast_mode
        # update the buttons text
        switch.configure(text="Fast" if fast_mode else "Slow")

    switch = tk.Button(flip_switch_frame, text="Fast", command=change_mode)
    switch.pack()

else:
    # a label containing a note if pillow is not installed
    tk.Label(root, text=f'Note: {notes[0]}', fg="red").pack()

if not settings["numba_installed"]:
    # a label containing a note if numba is not installed
    tk.Label(root, text=f'Note: {notes[1]}', fg="red").pack()

# option select menu
# this variable contains the selected option. It defaults to 1
option = tk.IntVar()
option.set(1)

edge_mandelbrot = tk.Radiobutton(main_frame, text="Edge", variable=option, value=1)
edge_mandelbrot.pack()

full_mandelbrot = tk.Radiobutton(main_frame, text="Full", variable=option, value=2)
full_mandelbrot.pack()

special_mandelbrot = tk.Radiobutton(main_frame, text="Special", variable=option, value=3)
special_mandelbrot.pack()

# iterations slider
iterations_slider = tk.Scale(main_frame, from_=20, to=300, orient=tk.HORIZONTAL, label="Iterations")
iterations_slider.pack()

# Button menu to change the color, default color is black
color = "#000000"

color_label = tk.Label(main_frame, text = "Custom color")
color_label.pack()

def change_color():
    global color
    color = colorchooser.askcolor()[1]
    color_button.configure(bg=color)

color_button = tk.Button(main_frame, width=10, command=change_color, text="CLICK ME!")
color_button.pack()

# display for the mandelbrot
canvas = tk.Canvas(main_frame, width=WIDTH, height=HEIGHT)
canvas.pack()

def redraw():
    # initializing a new mandelbrot object
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get(), option.get(), x_start, y_start, x_width, y_height, color)
    
    # remove all the objects except the select area rectangle and reset the rectangle's points
    canvas.delete("!select_area")
    canvas.coords("select_area" , 0, 0, 0,0)

    # checks if the faster mode is selected (only if pillow is installed)
    if settings["pil_installed"] and fast_mode:
        pixel_array = process_iterations_array(mandelbrot, True, canvas)
        photo_image = get_mandelbrot_image(pixel_array, WIDTH, HEIGHT)
        canvas.img = photo_image

        canvas.create_image(WIDTH / 2, HEIGHT / 2, image=photo_image)
    else:
        process_iterations_array(mandelbrot, False, canvas)

# Gia start
# The points for the area select rectangle
pixel_area = [(0,0), (0,0)]
area_select_rect = canvas.create_rectangle(0,0,0,0, dash=(2,2), fill="", outline="red", tags="select_area")

# default area
x_start=-2
y_start=-1.5
x_width=3
y_height=3

# Initializing the mouse starting points
mouse_start_x, mouse_start_y = 0,0

# Show the start of the area select rectangle and set the starting points of the zoomed in area
def set_start_mandelbrot_area(event):
    global mouse_start_x, mouse_start_y
    mouse_start_x = event.x
    mouse_start_y = event.y

    pixel_area[0] = (mouse_start_x, mouse_start_y)

    # move the area select rectangle above all objects
    canvas.tag_raise("select_area", 'all')

# Bind the set_start_mandelbrot_area function to mouse click
canvas.bind('<ButtonPress>', set_start_mandelbrot_area)

# Updates the rectangle so you can clearly see the slected area
def update_area_select_rect(event):
    pixel_area[1] = (event.x, event.y)

    canvas.coords("select_area", pixel_area[0][0], pixel_area[0][1], pixel_area[1][0], pixel_area[1][1])

# Bind the update_area_select_rect function to moving the mouse
canvas.bind('<B1-Motion>', update_area_select_rect)

# Scale the points to the domain of the mandelbrot set
# and redraw the mandelbrot set in the zoomed in area
def update_start_area(event):
    global x_width, y_height, x_start, y_start

    # make sure the zoom works in both y directions
    if mouse_start_y > event.y:
        y_start = y_start + event.y / HEIGHT * y_height
    else :
        y_start = y_start + mouse_start_y / HEIGHT * y_height

    # make sure the zoom works in both x directions
    if mouse_start_x > event.x:
        x_start = x_start + event.x / WIDTH * x_width
    else :
        x_start = x_start + mouse_start_x / WIDTH * x_width

    # rescale the width and the height to the domain of the mandelbrot set
    x_width = abs(event.x - mouse_start_x) / WIDTH * x_width
    y_height = abs(event.y - mouse_start_y) / HEIGHT * y_height 

    # redraw the mandelbrot set with the new area
    redraw()

# bind the update_start_area function to the release of the mouse button
canvas.bind('<ButtonRelease>', update_start_area)

def reset_zoom():
    global x_start, y_start, x_width, y_height
    x_start=-2
    y_start=-1.5
    x_width=3
    y_height=3

    redraw()

tk.Button(main_frame, text="Reset zoom", command= reset_zoom).pack()
# Gia end
tk.Button(main_frame, text="Generate", command=redraw).pack()

# explenation of the mandelbrot set
explanation_image = tk.PhotoImage(file="explanation.png")
tk.Label(image=explanation_image).pack(side=tk.RIGHT)

# draw the mandelbrot for the first time
redraw()

root.mainloop()
