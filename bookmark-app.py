import tkinter as tk
import webbrowser

def linkedin(event):
    webbrowser.open_new_tab('https://www.linkedin.com/in/stephanie-ashdown')

def github(event):
    webbrowser.open_new_tab('https://github.com/stephanie-ash')

window = tk.Tk()
window.geometry("300x200")
window.title("Social Media Bookmark App")
label1 = tk.Label(text = "My Social Media")
label1.grid(column=0, row=0)

button1 = tk.Button(window, text= "LinkedIn", bg="orange")
button1.grid(column=1, row=1)
button2 = tk.Button(window, text="GitHub", bg="pink")
button2.grid(column=3, row=1)
button1.bind("<Button-1>", linkedin)
button2.bind("<Button-1>", github)

window.mainloop()
