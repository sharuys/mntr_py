import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def get_icon():
   filename = filedialog.askopenfilename(filetypes=[("Icons", "*.ico")])

   with open(filename, 'rb') as file:
       icon = tk.PhotoImage(file.read())
       icon.write('icon.ico')

if __name__ == "__main__":
    get_icon()

    window.mainloop()
