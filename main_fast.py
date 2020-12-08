from mandelbrot import Mandelbrot
from PIL import Image, ImageTk, ImageColor
import tkinter.colorchooser as tkc
from helpers import get_color
import tkinter as tk

def get_pixel_array_from_option(iterations_array, option, color):
    pixel_array = [(255,255,255)] * len(iterations_array)
    # Option 1 draws the edge of the mandelbrot set
    if option == 1:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] > 17:
                pixel_array[pixel] = color

    # Option 2 draws the inside of the mandelbrot set
    if option == 2:
        for pixel in range(len(iterations_array)):
            if iterations_array[pixel] == 0:
                pixel_array[pixel] = color

    # Option 3 draws whole mandelbrot set with a coloring scheme
    if option == 3:
        for pixel in range(len(iterations_array)):
            pixel_array[pixel] = get_color(iterations_array[pixel], True)

    return pixel_array

WIDTH = 500
HEIGHT = 500

color = "#000000"

root = tk.Tk()
root.title("Project Mandelbrot")

label = tk.Label(root)
label.pack()

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

# Generates a new mandelbrot set and draws it
def redraw_canvas():
    x_start, y_start, x_width, y_height = get_area_variables(zoom_scale.get())
    mandelbrot = Mandelbrot(WIDTH, HEIGHT, iterations_slider.get(),x_start, y_start, x_width, y_height)

    image = Image.new(mode="RGB", size=(WIDTH,HEIGHT))
    pixel_array = get_pixel_array_from_option(mandelbrot.iterations_array, option.get(), ImageColor.getcolor(color, "RGB"))
    image.putdata(pixel_array)
    photo_image = ImageTk.PhotoImage(image)
    label.configure(image=photo_image)
    label.img = photo_image

redraw_canvas()

button = tk.Button(root, text="Generate", command=redraw_canvas)
button.pack()

root.mainloop()