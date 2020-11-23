from PIL import ImageTk
import tkinter as tk
import mandelbrot

root = tk.Tk()

img = mandelbrot.MandelbrotImage().image

photo_img =  ImageTk.PhotoImage(image=img)

label = tk.Label(root, image=photo_img)
label.img = photo_img
label.pack(side=tk.LEFT)

def update_image():
    img = img = mandelbrot.MandelbrotImage(scale=600, iterations=500, x_width=2.5, y_start=-1, y_height=1).image
    photo_img =  ImageTk.PhotoImage(image=img)
    label.configure(image=photo_img)
    label.img = photo_img

update_button = tk.Button(root, text="Update image", command=update_image)
update_button.pack(side=tk.RIGHT)

root.mainloop()