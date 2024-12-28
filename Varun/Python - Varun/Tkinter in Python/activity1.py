#creating  Tkinter
from tkinter import *
window=Tk()
window.geometry("600x600")
window.title("Carwow India")
window.config(bg='grey')
#creating label
label=Label(text="Volkswagen is the second richest company in the world", bg="white", fg="blue", font=("stockcar", 17, "bold", "italic"))
label.pack()
label.config(bg="white")
#creating button
button=Button(text="Discover wondors beyond horizon! Check out the all new Tayron", fg="grey", bg="black")
button.pack()
#Creating frame
frame=Frame(master=window, bg="white", relief=RAISED, borderwidth=6,)
frame.pack()
window.mainloop()