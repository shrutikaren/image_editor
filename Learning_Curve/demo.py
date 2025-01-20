# Name of the file: Demo.py 
# A file to explain the basics of tkinter package for users who
# are willing to learn from this repo and work on a project such 
# as image editing. 

from tkinter import ttk, Tk, PhotoImage, Canvas, filedialog

#Helps to create the empty window 
root = Tk()

# Creating a frame that will currently look the same as the root
# However, further in the project, both the Frame and the current 
# Window will look different
frame_header = ttk.Frame(root)
frame_header.pack()

# Will return an object
# pack() - Places the label on the window 
ttk.Label(frame_header, text="Test Label").pack()
ttk.Label(frame_header, text="Test Two Label").pack()

# Don't put .pack() on the same line you declared the variable 
# Use it after calling the variable on the separate line
my_label_object = ttk.Label(frame_header, text="Test Three Label")
my_label_object.pack()

def triggered_func():
    print ("I was clicked")

# Creating a button object 
# Command attribute will be the user defined attribute 
my_button_obj = ttk.Button(frame_header, text="Click me!", command = triggered_func())
my_button_obj.pack()

# Allows us to add a picture with the help of the PhotoImage module 
# We are resize the image with (5,5)
# We use the label to display our picture on our final canvas
logo = PhotoImage(file="python.gif").subsample(5,5)
ttk.Label(frame_header, image=logo).pack()

canvas = Canvas(frame_header, bg="white", width=300, height=400)
canvas.pack()
canvas.create_image(150, 200, image=logo)

# Everytime we run a file, it will run the dialog file. In the project, 
# we would want that a button asks us to open a specific file instead
filename = filedialog.askopenfilename()
print(filename)

root.mainloop()

