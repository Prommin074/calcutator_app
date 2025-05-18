from tkinter import *
from tkinter import messagebox,ttk

GUI = Tk()
GUI.title("Calculator_app")
GUI.geometry("500x800")

L = Label(GUI, text="Calculator", font=("Arial", 30), fg="black")
L1 = Label(GUI, text="User1", font=("Arial", 30), fg="black")
L2 = Label(GUI, text="User2", font=("Arial", 30), fg="black")
L.pack()
L1.pack()
L2.pack()

GUI.mainloop()