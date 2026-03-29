from tkinter import*
from tkinter import font
from tkinter.filedialog import * 


gui = Tk()
gui.title ("Address Book")
gui.geometry("800x400")

intro = Label(text="My Address Book", font=("Georgia", 16))
intro.pack()
open = Button(text = "Open", font = ("Georgia", 16),)
open.pack()

box = Frame(gui)
box.place(x=500,y=70)

namelbl = Label(box,text="Name:", font=("Georgia", 14))
namelbl.grid(row=0,column=0)
name = Entry(box, fg ="black", bg = "white")
name.grid(row=0,column=1)

addresslbl = Label(box,text="Address:", font=("Georgia", 14))
addresslbl.grid(row=1,column=0)
address = Entry(box,fg ="black", bg = "white")
address.grid(row=1,column=1)


mobilelbl = Label(box,text="Mobile:", font=("Georgia", 14))
mobilelbl.grid(row=2,column=0)
mobile = Entry(box,fg ="black", bg = "white")
mobile.grid(row=2,column=1)

emaillbl = Label(box,text="Email:", font=("Georgia", 14))
emaillbl.grid(row=3,column=0)
email = Entry(box,fg ="black", bg = "white")
email.grid(row=3,column=1)

birthdaylbl = Label(box,text="Birthday:", font=("Georgia", 14))
birthdaylbl.grid(row=4,column=0)
birthday = Entry(box,fg ="black", bg = "white")
birthday.grid(row=4,column=1)

listbox = Listbox(width=50,bg="white",)
listbox.place(x=30,y=70)

edit = Button(text = "Edit", font = ("Georgia", 14),)
edit.place(x=30,y=240)

delete = Button(text = "Delete", font = ("Georgia", 16),)
delete.place()

update = Button(text = "Update/add", font = ("Georgia", 16),)
update.place()

save = Button(text = "Save", font = ("Georgia", 16),)
save.place()


gui.mainloop()