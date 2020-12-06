from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("Project Mandelbrot")
root.geometry("900x600")

#Menu Items
combo_iterations = Combobox(root)                
combo_iterations["values"] = (50,100,250,500,1000)
combo_iterations.current(0)

variable = StringVar(root)
variable.set("2 X")
zoom_options = OptionMenu(root, variable, "2 X","10 X","25 X","50 X")
zoom_options.grid(row=3, column= 1, pady = 15, sticky = W)



#Labels
max_iterations = Label( text = "MaxIterations:")
red_label = Label( text = "Red")
blue_label = Label( text = "Blue")
green_label = Label( text = "Green")

#Buttons
reset = Button( text="Reset")
zoom = Button( text = "Zoom in/out by: ")

#Button Functions

#Sliders
#Color_slider
red = Scale(root, from_=0,to=255,orient=HORIZONTAL, label = "Red")
blue = Scale(root,from_=0,to=255,orient=HORIZONTAL)
green = Scale(root,from_=0,to=255,orient=HORIZONTAL)

#Locations on Grid
reset.grid(row=0, column= 0, sticky= W, padx=15 , ipadx= 5)
max_iterations.grid(row=1, column = 0, pady= 15)
combo_iterations.grid(row=1, column = 1, sticky = W)
red.grid(row=2, column = 0, pady = 15)
blue.grid(row=2, column = 1, pady = 15)
green.grid(row=2, column = 2, pady = 15)
zoom.grid(row=3, column= 0, pady = 15)
zoom_options.grid(row=3, column= 1, pady = 15, sticky = W)

    
root.mainloop()
