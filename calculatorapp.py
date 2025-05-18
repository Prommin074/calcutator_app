from tkinter import *
from tkinter import messagebox,ttk

GUI = Tk()
GUI.title("Calculator_app")
GUI.geometry("500x800")

L = Label(GUI, text="Calculator", font=("Arial", 30), fg="black")
L = Label(GUI, text="User1")
L.pack()

GUI.mainloop()