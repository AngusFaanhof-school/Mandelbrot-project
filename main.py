import tkinter as tk
import mandelbrot
from helpers import draw_from_pixel_array, get_pixel_array

# tk.Tk.attributes("-fullscreen", True)
root = tk.Tk()
root.state('zoomed')
WIDTH = 1080
HEIGHT = 1080

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, background="black")

mandelbrot1 = mandelbrot.MandelbrotImage(picture_width=WIDTH, picture_height=HEIGHT)
pixel_array = get_pixel_array(mandelbrot1.image_array, WIDTH, 1)
pixel_array2 = get_pixel_array(mandelbrot1.image_array, WIDTH, 2)
draw_from_pixel_array(canvas, pixel_array2, WIDTH)
canvas.pack(side=tk.LEFT)


def update_image():
    global canvas, mandelbrot1, WIDTH
    canvas.delete("all")
    draw_from_pixel_array(canvas, pixel_array, WIDTH)
    

update_button = tk.Button(root, text="Update image", command=update_image)
update_button.pack(side=tk.RIGHT)

root.mainloop()