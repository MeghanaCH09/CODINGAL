from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("400x400")
root.title("Image")
root.config(bg='grey')
# Now use Image.open to open and identify the given image file
upload = Image.open("A.jpg")
# Convert this image to Tkinter compatible image 
Image = ImageTk.PhotoImage(upload)
# Add image to Tkinter label
label = Label(root, image=Image, height=700, width=700)
label.place(x=50, y=0)
root.mainloop()
