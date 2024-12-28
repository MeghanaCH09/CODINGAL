import tkinter as tk
window=tk.Tk()
window.geometry("550x550")
#window.Tk_setPalette("darkblue")
window.title("The New Tayron")
for i in range(3): 
    for j in range(3): 
        frame=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
        frame.grid(row=i, column=j, padx=5, pady=5)
        label=tk.Label(master=frame, text=f"row{j}", bg="grey", height=5, width=10)
        label.pack()
window.mainloop()
                       
