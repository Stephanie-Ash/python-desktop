import tkinter as tk

window = tk.Tk()
window.title(" My Python Desktop App ")
window.geometry("600x400")
newlabel = tk.Label(text = " This is my first attempt at a Python desktop app! ")
newlabel.grid(column = 0, row = 0)
window.mainloop()