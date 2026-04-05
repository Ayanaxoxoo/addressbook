from tkinter import*
from tkinter import font
from tkinter.filedialog import * 


gui = Tk()
gui.title ("Address Book")
gui.geometry("800x400")
myAddressBook={}

def clearall():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def update():
    key = name.get()
    if key not in myAddressBook.keys():
        listbox.insert(END,key)
    myAddressBook[key]=(address.get(),mobile.get(),email.get(),birthday.get())
    clearall()

def edits():
    index=listbox.curselection()
    details=myAddressBook[listbox.get(index)] 
    name.insert(0,listbox.get(index))
    address.insert(0,details[0])
    mobile.insert(0,details[1])
    email.insert(0,details[2])
    birthday.insert(0,details[3])

def deletenow():
    index = listbox.curselection()
    del myAddressBook[listbox.get(index)]
    listbox.delete(index )

def savenow():
    content = asksaveasfile(defaultextension=".txt")
    print(myAddressBook,file=content)


intro = Label(text="My Address Book", font=("Georgia", 16))
intro.pack()
open = Button(text = "Open", font = ("Georgia", 16),)
open.pack()

box = Frame(gui)
box.place(x=500,y=70)

namelbl = Label(box,text="Name:", font=("Georgia", 14))
namelbl.grid(row=0,column=0)
name = Entry(box, fg ="black", bg = "white")
name.grid(row=0,column=1,pady=3)

addresslbl = Label(box,text="Address:", font=("Georgia", 14))
addresslbl.grid(row=1,column=0)
address = Entry(box,fg ="black", bg = "white")
address.grid(row=1,column=1,pady=3)


mobilelbl = Label(box,text="Mobile:", font=("Georgia", 14))
mobilelbl.grid(row=2,column=0)
mobile = Entry(box,fg ="black", bg = "white")
mobile.grid(row=2,column=1,pady=3)

emaillbl = Label(box,text="Email:", font=("Georgia", 14))
emaillbl.grid(row=3,column=0)
email = Entry(box,fg ="black", bg = "white")
email.grid(row=3,column=1,pady=3)

birthdaylbl = Label(box,text="Birthday:", font=("Georgia", 14))
birthdaylbl.grid(row=4,column=0)
birthday = Entry(box,fg ="black", bg = "white")
birthday.grid(row=4,column=1,pady=3)

listbox = Listbox(width=50,fg="black",bg="white",)
listbox.place(x=30,y=70)

edit = Button(text = "Edit", font = ("Georgia", 14),command=edits)
edit.place(x=30,y=250)

delete = Button(text = "Delete", font = ("Georgia", 14),command=deletenow)
delete.place(x=120,y=250)

updateadd = Button(text = "Update/add", font = ("Georgia", 14),command=update)
updateadd.place(x=210,y=250)

save = Button(text = "Save", font = ("Georgia", 14),command=savenow)
save.place(x=350,y=250)


gui.mainloop()
