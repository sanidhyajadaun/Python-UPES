from tkinter import *
root = Tk ()

root.geometry('1280x720')
myLabel1 = Label(root, text="Hello", padx=20)
myLabel1.grid(row=0, column=2)

def clicked ():
    selection = "You age is " + var.get()
    l9.config(text = selection, fg="green")

def onClick ():
    n = e1.get ( )
    l3 = Label (root, text="BUTTON WAS CLICKED", relief=RAISED)
    l4 =Label (root , text = "your username is " + n)
    l3.grid(row= 3, column = 2)
    l4.grid(row = 4, column = 2)
    l5 = Label(root, text = "WHATS YOUR AGE?", relief = RAISED)
    l6 = Label(root, text = "option 1: below 19:")
    l7 = Label(root, text = "option 2:between 18 and 36")
    l8 = Label(root, text = "option 3: above 30")
    l5.grid(row = 6, column = 2)
    l6.grid(row = 7, column = 2)
    l7.grid(row = 8, column = 2)
    l8.grid(row = 9, column = 2)
    global var
    var = StringVar()
    var.set(None)
    R1 = Radiobutton(root, text = "Option 1", variable = var, value = "below 18", command = clicked)
    R2 = Radiobutton(root, text = "Option 2", variable = var, value = "between 18 and 30", command = clicked)
    R3 = Radiobutton(root, text = "Option 3", variable = var, value = "above 30", command = clicked)
    R1.grid(row = 10, column = 1)
    R2.grid(row = 10, column = 2)
    R3.grid(row = 10, column = 3)

l1 = Label(root, text = "Username")
l1.grid(row = 1, column = 0)

e1 = Entry(root)
e1.grid(row = 1, column = 1)

l9 = Label(root)
l9.grid(row = 11, column = 2)

myButton = Button(root, text = "CLICK ME", fg = "red", bg = "white", padx = 20, command = onClick)

myButton.grid(row = 2, column = 2)
root.mainloop()
