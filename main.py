import tkinter as tk
import mandelbrot, time
from helpers import draw_from_iterations_array

root = tk.Tk()
root.state('zoomed')
WIDTH = 1080
HEIGHT = 1080

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

mandelbrot1 = mandelbrot.MandelbrotImage(picture_width=WIDTH, picture_height=HEIGHT)
draw_from_iterations_array(canvas, mandelbrot1.image_array, WIDTH, 1)
canvas.pack(side=tk.LEFT)


# def update_image():
#     global canvas, mandelbrot1, WIDTH, one
#     canvas.delete("all")
#     one = not one
#     if one:
#         draw_from_pixel_array(canvas, pixel_array, WIDTH)
#     else :
#         draw_from_pixel_array(canvas, pixel_array2, WIDTH)
    

# update_button = tk.Button(root, text="Update image", command=update_image)
# update_button.pack(side=tk.RIGHT)

root.mainloop()