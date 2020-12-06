import tkinter as tk
import tkinter.colorchooser as tkc
from mandelbrot import Mandelbrot
from helpers import draw_from_iterations_array, hex_from_rgb, get_area_variables

WIDTH = 500
HEIGHT = 500

color = "#000000"

root = tk.Tk()
root.title("Project Mandelbrot")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack(side=tk.LEFT)

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

color_button = ""

def change_color():
    global color
    color = tkc.askcolor()[1]
    color_button.configure(bg=color)

color_button = tk.Button(root, width=10, command=change_color, text="CLICK ME!")
color_button.pack()

# zoom slider scale
zoom_scale = tk.Scale(root, from_=-5, to=5, orient=tk.HORIZONTAL, label='zoom')
zoom_scale.pack()

# create the initial mandelbrot set
x_start, y_start, x_width, y_height = get_area_variables(zoom_scale.get())

mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get(), x_start, y_start, x_width, y_height)
draw_from_iterations_array(canvas, mandelbrot.iterations_array, WIDTH, option.get())

# Generates a new mandelbrot set and draws it
def redraw_canvas():
    x_start, y_start, x_width, y_height = get_area_variables(zoom_scale.get())
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get(),x_start, y_start, x_width, y_height)

    canvas.delete("all")

    draw_from_iterations_array(canvas, mandelbrot.iterations_array, WIDTH, option.get(), color)

button = tk.Button(root, text="Generate", command=redraw_canvas)
button.pack(side=tk.RIGHT)

root.mainloop()