from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
root.title("Image")
root.config(bg='darkgrey')

upload = Image.open("app_img.jpg")

Image = ImageTk.PhotoImage(upload)

label = Label(root, image=Image, height=700, width=700)
label.place(x=50, y=0)

#creating a button

def msg(): 
    MsgBox = messagepbox.showinfo("Alert, Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg="white")
button1.place(x=260, y=360)

#creating a top-window

def topwin(): 
    top = Toplevel()
    top.geometry("600x400")
    top.title("Denomination calculator")
    top.configure(bg="lightgrey")
    label = Label(top, text="Eenter total amount: ", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are numebrs of notes for each denomination", bg='light grey')
    l1 = Label(top, text='2000', bg='light grey')
    l2 = Label(top, text='500', bg='light grey')
    l3 = Label(top, text='100', bg='light grey')
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

#creating a calculator
def calculator(): 
    try: 
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %=500
        note100 = amount // 100
        amount %=100

        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t2.insert(END, str(note100))
    except ValueError: 
        label.place(x=230, y=50)
        entry.place(x=200, y=80)
        btn.place(x=240, y=120)
        lbl.place(x=140, y=170)

        l1.place(x=180, y=200)
        l2.place(x=180, y=230)
        l3.place(x=180, y=260)

        t1.place(x=270, y=200)
        t2.place(x=270, y=230)
        t3.place(x=270, y=260)
top.mainloop()