from tkinter import *
from tkinter import messagebox,ttk

GUI = Tk()
GUI.title("Calculator")
GUI.geometry("500x800")

L = Label(GUI, text="Calculator", font=("Arial", 30), fg="black")
L.pack()

GUI.mainloop()