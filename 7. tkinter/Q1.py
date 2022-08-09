from tkinter import *
root = Tk()
root.geometry('1280x720')

nyLabel1 = Label (root, text = "Hello", padx = 20) . pack( )
def onClick () :
    myLabel= Label (root, text="BUTTON WAS CLICKED", relief=RAISED).pack()

myButton= Button (root, text="CLICK ME", fg="red", bg="white", padx=20, command= onClick) . pack()
root.mainloop ()
