import tkinter as tk
from mandelbrot import Mandelbrot
from helpers import draw_from_iterations_array, hex_from_rgb

WIDTH = 500
HEIGHT = 500

root = tk.Tk()

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

# color select menu
# each color scale goes from 0 to 255
red_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="red")
red_scale.pack()

green_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="green")
green_scale.pack()

blue_scale = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label='blue')
blue_scale.pack()

# create the initial mandelbrot set
mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get())
draw_from_iterations_array(canvas, mandelbrot.iterations_array, WIDTH, option.get())

# Generates a new mandelbrot set and draws it
def redraw_canvas():
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get())

    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()

    color = hex_from_rgb(r,g,b)

    canvas.delete("all")

    draw_from_iterations_array(canvas, mandelbrot.iterations_array, WIDTH, option.get(), color)

button = tk.Button(root, text="Generate", command=redraw_canvas)
button.pack(side=tk.RIGHT)

root.mainloop()