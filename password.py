import tkinter as tk
from tkinter import messagebox
import random
import string


#pass
def generate_password():
    l = lbox.get()
    up = upbox.get()
    lo = lobox.get()
    di = dibox.get()
    sy = sybox.get()

    if not (up or lo or di or sy):
        messagebox.showwarning("Warning", "Select at least one character type!")
        return

    ch = ""
    if up:
        ch += string.ascii_uppercase
    if lo:
        ch += string.ascii_lowercase
    if di:
        ch += string.digits
    if sy:
        ch += string.punctuation

    passw = ''.join(random.choice(ch) for i in range(l))
    passbox.delete(0, tk.END)
    passbox.insert(0, passw)


#copy
def copy_password():
    passw= passbox.get()
    if passw:
        r.clipboard_clear()
        r.clipboard_append(passw)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy.")



# mm
r = tk.Tk()
r.title("Password Generator")
r.geometry("400x350")
r.resizable(False, False)
r.configure(bg="#1E1E1E")
r.iconbitmap("lock.ico")


lbox = tk.IntVar(value=12)
upbox = tk.BooleanVar(value=True)
lobox = tk.BooleanVar(value=True)
dibox = tk.BooleanVar(value=True)
sybox = tk.BooleanVar(value=True)


tk.Label(r, text="🔐 Password Generator", font=("Arial", 20, "bold"), fg="#769EDB", bg="#1E1E1E").pack(pady=10)


fl = tk.Frame(r, bg="#1E1E1E")
fl.pack(pady=5)
tk.Label(fl, text="Password length:", fg="white", bg="#1E1E1E").pack(side=tk.LEFT)
tk.Entry(fl, textvariable=lbox, width=5).pack(side=tk.LEFT, padx=5)


of = tk.Frame(r, bg="#1E1E1E")
of.pack(pady=10)
tk.Checkbutton(of, text="Uppercase (A-Z)", variable=upbox, fg="white", bg="#1E1E1E", selectcolor="#333").pack(anchor="w")
tk.Checkbutton(of, text="Lowercase (a-z)", variable=lobox, fg="white", bg="#1E1E1E", selectcolor="#333").pack(anchor="w")
tk.Checkbutton(of, text="Digits (0-9)", variable=dibox, fg="white", bg="#1E1E1E", selectcolor="#333").pack(anchor="w")
tk.Checkbutton(of, text="Symbols (!@#$%)", variable=sybox, fg="white", bg="#1E1E1E", selectcolor="#333").pack(anchor="w")


passbox = tk.Entry(r, font=("Consolas", 12), justify="center", width=30)
passbox.pack(pady=10)


bf = tk.Frame(r, bg="#1E1E1E")
bf.pack(pady=5)
tk.Button(bf, text="Generate", command=generate_password, bg="#769EDB", fg="black", width=12).pack(side=tk.LEFT, padx=5)
tk.Button(bf, text="Copy", command=copy_password, bg="#333333", fg="white", width=12).pack(side=tk.LEFT, padx=5)


tk.Label(r, text="© 2025 Abdelaziz Ounissi", fg="#769EDB", bg="#1E1E1E", font=("Arial", 8)).pack(side=tk.BOTTOM, pady=5)

r.mainloop()