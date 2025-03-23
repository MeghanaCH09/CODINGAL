import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 4:
        messagebox.showwarning("Warning", "Password length should be at least 4 characters!")
        return
    
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Success", "Password copied to clipboard!")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")

tk.Label(root, text="Enter Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").pack(pady=5)
password_entry = tk.Entry(root, textvariable=password_var, state='readonly', width=30)
password_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=5)

root.mainloop()
