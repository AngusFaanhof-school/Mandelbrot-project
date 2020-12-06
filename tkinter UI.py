from tkinter import *
import tkinter.colorchooser as tkc
import tkinter.ttk as ttk
root = Tk()
root.title("Project Mandelbrot")
root.geometry("900x600")

#Menu Items
combo_iterations = ttk.Combobox(root)                
combo_iterations["values"] = (50,100,250,500,1000)
combo_iterations.current(0)

variable = StringVar(root)
variable.set("2 X")
text_label = Label(root, text="Zoom", bg="Red")

in_out = StringVar(root)
in_out.set("In")
zoom_in_out = ttk.OptionMenu(root, in_out, "Select", "In", "Out")
zoom_options = ttk.OptionMenu(root, variable, "Select", "2 X","10 X","25 X","50 X")
text_label.grid(row=3, column=0,  padx=0, sticky = W)
zoom_in_out.grid(row=3, column=1, padx=0, sticky = W)
zoom_options.grid(row=3, column= 2, pady = 15, padx=0, sticky = W)

canvas = Canvas(root, width=40, height=40)
canvas.grid(row=2, column = 10, pady = 15)

def ask_color():
    global canvas
    color = tkc.askcolor()
    canvas.create_rectangle(0,0,40,40, fill=color[1])

color_button = Button(root, text="Custom color", command=ask_color)
color_button.grid(row=2, column = 5, pady = 15)



#Labels
max_iterations = Label( text = "MaxIterations:")
red_label = Label( text = "Red")
blue_label = Label( text = "Blue")
green_label = Label( text = "Green")

#Buttons
reset = Button( text="Reset")
# zoom = Button( text = "Zoom in/out by: ")

#Button Functions

#Sliders
#Color_slider
# red = Scale(root, from_=0,to=255,orient=HORIZONTAL, label = "Red")
# blue = Scale(root,from_=0,to=255,orient=HORIZONTAL, label = "Blue")
# green = Scale(root,from_=0,to=255,orient=HORIZONTAL, label = "Green")

#Locations on Grid
reset.grid(row=0, column= 0, sticky= W, padx=15 , ipadx= 5)
max_iterations.grid(row=1, column = 0, pady= 15)
combo_iterations.grid(row=1, column = 1, sticky = W)
# red.grid(row=2, column = 0, pady = 15)
# blue.grid(row=2, column = 1, pady = 15)
# green.grid(row=2, column = 2, pady = 15)
# zoom.grid(row=3, column= 0, pady = 15)
# zoom_options.grid(row=3, column= 1, pady = 15, sticky = W)

    
root.mainloop()