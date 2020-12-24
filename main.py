from mandelbrot import Mandelbrot
from helpers import process_iterations_array, get_area_variables, hex_to_rgb

from PIL import Image, ImageTk

import tkinter as tk
import tkinter.colorchooser as colorchooser

WIDTH = 500
HEIGHT = 500

x_start=-2
y_start=-1.5
x_width=3
y_height=3

mouse_start_x, mouse_start_y = 0, 0
mouse_end_x, mouse_end_y = 0, 0
rect_id = None

def get_mouse_posn(event):
    global mouse_start_x, mouse_start_y

    mouse_start_x, mouse_start_y = event.x, event.y

def update_sel_rect(event):
    global rect_id
    global mouse_start_x, mouse_start_y, mouse_end_x, mouse_end_y

    mouse_end_x, mouse_end_y = event.x, event.y
    canvas.coords(rect_id, mouse_start_x, mouse_start_y, mouse_end_x, mouse_end_y)  # Update selection rect.


pixel_array = []
color = "#000000"

root = tk.Tk()
root.title("Project Mandelbrot")

# The image container
label = tk.Label(root)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

fast_option = tk.BooleanVar()
fast_option.set(False)

def change_mode():
    if fast_option.get():
        label.pack(side=tk.LEFT)
        canvas.forget()
    else:
        canvas.pack(side=tk.LEFT)
        label.forget()

change_mode()

edge_mandelbrot = tk.Radiobutton(root, text="Fast", variable=fast_option, value=True, command=change_mode)
edge_mandelbrot.pack()

full_mandelbrot = tk.Radiobutton(root, text="SLOW", variable=fast_option, value=False, command=change_mode)
full_mandelbrot.pack()

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
# the iterations slider goes from 20 to 300
iterations_slider = tk.Scale(root, from_=20, to=300, orient=tk.HORIZONTAL, label='iterations')
iterations_slider.pack()

# Button menu to change the color
color_label = tk.Label(root, text = "Custom color")
color_label.pack()

def change_color():
    global color
    color = colorchooser.askcolor()[1]
    color_button.configure(bg=color)

color_button = tk.Button(root, width=10, command=change_color, text="CLICK ME!")
color_button.pack()

# zoom slider scale
zoom_scale = tk.Scale(root, from_=-5, to=5, orient=tk.HORIZONTAL, label='zoom')
zoom_scale.pack()

def get_scaled_coord(px,py):
    scaled_px = x_start + px / WIDTH * x_width
    scaled_py = y_start - py / HEIGHT * y_height
    return scaled_px, scaled_py

def get_mandelbrot(width, height, iterations, zoom):
    global x_start, y_start, x_width, y_height
    if mouse_start_x != 0 and mouse_start_y != 0 and mouse_end_x != 0 and mouse_end_y != 0:
        x_start, y_start = get_scaled_coord(mouse_start_x, mouse_start_y)
        x_width, y_height = get_scaled_coord(mouse_end_x, mouse_end_y)
        print(x_start, y_start, x_width, y_height)

    # x_start, y_start, x_width, y_height = get_area_variables(zoom)
    return Mandelbrot(width, height, iterations, x_start, y_start, x_width, y_height)

def change_pixel(pixel, hex_color):
    pixel_array[pixel] = hex_to_rgb(hex_color)

def draw_pixel_on_canvas(pixel, color):
    x = pixel % WIDTH
    y = pixel // WIDTH
    canvas.create_rectangle(x, y, x, y, outline=color)

def redraw_mandelbrot():
    if fast_option.get():
        global pixel_array
        mandelbrot = get_mandelbrot(WIDTH, HEIGHT, iterations_slider.get(), zoom_scale.get())
        
        pixel_array = [(255,255,255)] * (WIDTH * HEIGHT)

        process_iterations_array(mandelbrot.iterations_array, option.get(), color, change_pixel)
        
        image = Image.new(mode="RGB", size=(WIDTH,HEIGHT))
        image.putdata(pixel_array)
        photo_image = ImageTk.PhotoImage(image)

        label.configure(image=photo_image)
        label.img = photo_image
    else:
        mandelbrot = get_mandelbrot(WIDTH, HEIGHT, iterations_slider.get(), zoom_scale.get())

        canvas.delete("all")
        canvas.create_rectangle(mouse_start_x, mouse_start_y, mouse_start_x, mouse_start_y, dash=(2,2), fill="", outline="red")
        process_iterations_array(mandelbrot.iterations_array, option.get(), color, draw_pixel_on_canvas)

redraw_mandelbrot()

rect_id = canvas.create_rectangle(mouse_start_x, mouse_start_y, mouse_start_x, mouse_start_y, dash=(2,2), fill="", outline="red")

canvas.bind('<Button-1>', get_mouse_posn)
canvas.bind('<B1-Motion>', update_sel_rect)



def print_area():
    print(mouse_start_x, mouse_start_y, mouse_end_x, mouse_end_y)
    x_start, y_start = get_scaled_coord(mouse_start_x, mouse_start_y)
    x_width, y_height = get_scaled_coord(mouse_end_x, mouse_end_y)
    print(x_start, y_start, x_width, y_height)
tk.Button(root, text="Select Area", command=print_area).pack()

tk.Button(root, text="Generate", command=redraw_mandelbrot).pack()

root.mainloop()