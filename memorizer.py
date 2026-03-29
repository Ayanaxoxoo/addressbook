from tkinter import*
from tkinter import font
from tkinter.filedialog import * 

gui = Tk()
gui.title ("Memorizer")
gui.geometry("800x400")

def deleteitem():
    user=listbox.curselection()
    listbox.delete(user)

def additem():
    user=newtext.get()
    listbox.insert(END,user)

def openitem():
    file=askopenfile(title="Open file")
    listbox.delete(0,END)
    content=file.readlines()
    for item in content:
        listbox.insert(END,item.strip())

def saveitem():
    fsave = asksaveasfile(defaultextension=".txt")
    for item in listbox.get(0,END):
        print(item.strip(),file=fsave)
    

save = Button(text = "Save", font = ("Georgia", 16), command=saveitem)
save.pack()

newtext = Entry(fg ="black", bg = "white")
newtext.pack()

add = Button(text = "Add", font = ("Georgia", 16),command=additem)
add.pack() 

open = Button(text = "Open", font = ("Georgia", 16),command=openitem)
open.place(x=50,y=150) 

delete = Button(text = "Delete", font = ("Georgia", 16),command=deleteitem)
delete.place(x=650,y=150)

box = Frame(gui)
box.pack()

scrollbar = Scrollbar(box,orient="vertical")
scrollbar.pack(side = RIGHT, fill=Y)

listbox = Listbox(box,width=50,yscrollcommand=scrollbar.set,bg="lightblue4",)
listbox.pack(side=LEFT,padx=5)
scrollbar.config(command=listbox.yview)


for i in range (100):
    listbox.insert(END,i)

gui.mainloop()