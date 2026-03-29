from tkinter import *
from tkinter.ttk import *

gui = Tk()
gui.title("Pizza App")
gui.geometry("600x300")

pizza = StringVar()
quantity = IntVar()
size = StringVar()

def order():
    result = "You ordered " + str(quantity.get()) + " " + pizza.get() + " " + size.get() + " pizza(s)"
    output.config(text=result)

title = Label(text="Welcome to Pizza Hut", font=("Georgia", 18))
title.pack(pady=10)

label1 = Label(text="Select Your Fav Pizza:")
label1.place(x=50, y=80)

pizza_box = Combobox(gui, textvariable=pizza)
pizza_box["values"] = ("Veg Extravaganza", "Pepperoni", "Margherita", "BBQ Chicken")
pizza_box.place(x=250, y=80)

label2 = Label(text="Enter Quantity:")
label2.place(x=50, y=120)

quantity_box = Combobox(gui, textvariable=quantity, width=5)
quantity_box["values"] = tuple(range(1, 11))
quantity_box.place(x=250, y=120)


Radiobutton(gui, text="S", variable=size, value="Small").place(x=450, y=80)
Radiobutton(gui, text="M", variable=size, value="Medium").place(x=450, y=110)
Radiobutton(gui, text="L", variable=size, value="Large").place(x=450, y=140)

order_btn = Button(text="Order", command=order)
order_btn.place(x=250, y=170)


output = Label(text="", font=("Georgia", 12))
output.place(x=150, y=230)

gui.mainloop()