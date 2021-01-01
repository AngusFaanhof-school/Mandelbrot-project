from settings import settings, notes
from mandelbrot import Mandelbrot
from helpers import process_iterations_array, hex_to_rgba

import tkinter as tk
import tkinter.colorchooser as colorchooser

if settings["pil_installed"]:
    from PIL import Image, ImageTk
    from helpers import get_mandelbrot_image

WIDTH = 500
HEIGHT = 500

root = tk.Tk()
root.title("Project Mandelbrot")

# Message if numba is not installed
if not settings["jit_installed"]:
    tk.Label(root, text=f'Note: {notes[1]}', fg="red").pack()

# Mode menu
if settings["pil_installed"]:
    fast_mode = True

    flip_switch_frame = tk.Frame(root)
    flip_switch_frame.pack()

    tk.Label(flip_switch_frame, text="Mode:").pack(side=tk.LEFT)

    def change_mode():
        global fast_mode
        fast_mode = not fast_mode
        switch.configure(text="Fast" if fast_mode else "Slow")

    switch = tk.Button(flip_switch_frame, text="Fast", command=change_mode)
    switch.pack()

else:
    tk.Label(root, text=f'Note: {notes[0]}', fg="red").pack()

# option select menu
# this variable contains the selected option. It defaults to 1
option = tk.IntVar()
option.set(1)

edge_mandelbrot = tk.Radiobutton(root, text="Edge", variable=option, value=1)
edge_mandelbrot.pack()

full_mandelbrot = tk.Radiobutton(root, text="Full", variable=option, value=2)
full_mandelbrot.pack()

special_mandelbrot = tk.Radiobutton(root, text="Special", variable=option, value=3)
special_mandelbrot.pack()

# iterations slider
iterations_slider = tk.Scale(root, from_=20, to=300, orient=tk.HORIZONTAL, label="Iterations")
iterations_slider.pack()

# Button menu to change the color
color = "#000000"

color_label = tk.Label(root, text = "Custom color")
color_label.pack()

def change_color():
    global color
    color = colorchooser.askcolor()[1]
    color_button.configure(bg=color)

color_button = tk.Button(root, width=10, command=change_color, text="CLICK ME!")
color_button.pack()

# display for the mandelbrot
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bd=1)
canvas.pack()

def change_pixel(pixel, hex_color):
    pixel_array[pixel] = hex_to_rgba(hex_color)

def draw_pixel_on_canvas(pixel, color):
    x = pixel % WIDTH
    y = pixel // WIDTH
    canvas.create_rectangle(x, y, x, y, outline=color)

pixel_array = []

def redraw():
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get(), option.get(), x_start, y_start, x_width, y_height, color)
    
    # remove all the objects except the select area object
    canvas.delete("!select_area")
    canvas.coords("select_area" , 0, 0, 0,0)

    if settings["pil_installed"] and fast_mode:
        pixel_array = process_iterations_array(mandelbrot, True, canvas)
        photo_image = get_mandelbrot_image(pixel_array, WIDTH, HEIGHT)
        canvas.img = photo_image

        canvas.create_image(WIDTH / 2, HEIGHT / 2, image=photo_image)
    else:
        process_iterations_array(mandelbrot, False, canvas)

pixel_area = [(0,0), (0,0)]
area_select_rect = canvas.create_rectangle(0,0,0,0, dash=(2,2), fill="", outline="red", tags="select_area")

# default area
x_start=-2
y_start=-1.5
x_width=3
y_height=3

mouse_start_x, mouse_start_y = 0,0

def set_start_mandelbrot_area(event):
    global mouse_start_x, mouse_start_y
    mouse_start_x = event.x
    mouse_start_y = event.y

    pixel_area[0] = (mouse_start_x, mouse_start_y)

    canvas.tag_raise("select_area", 'all')

def update_area_select_rect(event):
    pixel_area[1] = (event.x, event.y)

    canvas.coords("select_area", pixel_area[0][0], pixel_area[0][1], pixel_area[1][0], pixel_area[1][1])

def update_start_area(event):
    global x_width, y_height, x_start, y_start

    if mouse_start_y > event.y:
        y_start = y_start + event.y / HEIGHT * y_height
    else :
        y_start = y_start + mouse_start_y / HEIGHT * y_height

    if mouse_start_x > event.x:
        x_start = x_start + event.x / WIDTH * x_width
    else :
        x_start = x_start + mouse_start_x / WIDTH * x_width

    x_width = abs(event.x - mouse_start_x) / WIDTH * x_width
    y_height = abs(event.y - mouse_start_y) / HEIGHT * y_height 

    redraw()


canvas.bind('<ButtonPress>', set_start_mandelbrot_area)
canvas.bind('<B1-Motion>', update_area_select_rect)
canvas.bind('<ButtonRelease>', update_start_area)

def reset_zoom():
    global x_start, y_start, x_width, y_height
    x_start=-2
    y_start=-1.5
    x_width=3
    y_height=3

    redraw()

tk.Button(root, text="Reset zoom", command= reset_zoom).pack()
tk.Button(root, text="Generate", command=redraw).pack()

redraw()

root.mainloop()