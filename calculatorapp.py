from tkinter import *
from tkinter import messagebox,ttk

GUI = Tk()
GUI.title("Calculator_app")
GUI.geometry("500x800")

L = Label(GUI, text="Calculator", font=("Arial", 30), fg="black")
L.pack()

x1 = StringVar()
e1 = ttk.Entry(GUI, textvariable=x1, font=("Arial", 20), width=10)
e1.pack()

x2 = StringVar()
e2 = ttk.Entry(GUI, textvariable=x2, font=("Arial", 20), width=10)
e2.pack()

def cal():
    y = float(x1.get()) * float(x2.get())
    z1 = x1.get()
    z2 = x2.get()
    result = f"{z1} * {z2} = {y}"
    messagebox.showinfo("Result", result)

b1 = Button(GUI, text="Calculate Now!!!" , font=("Arial", 50), command=cal)
b1.pack()
GUI.mainloop()