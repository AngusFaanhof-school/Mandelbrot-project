from PIL import ImageTk
import tkinter as tk
import mandelbrot

root = tk.Tk()

img = mandelbrot.MandelbrotImage().image

photo_img =  ImageTk.PhotoImage(image=img)

label = tk.Label(root, image=photo_img)
label.img = photo_img
label.pack()

# def update_image():
#     img = mandelbrot.MandelbrotImage(iterations=40).image
#     photo_img =  ImageTk.PhotoImage(image=img)
#     label = tk.Label(root, image=photo_img)
#     label.img = photo_img

# update_button = tk.Button(root, text="Update Image", command=update_image)
# update_button.pack()

root.mainloop()