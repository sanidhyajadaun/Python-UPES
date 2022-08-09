from tkinter import *
root =Tk()
root.geometry('1500x600')
myLabel1= Label(root, text="NAME OF THE STUDENT", padx=5)
myLabel1.grid(row=0, column=0)
e1= Entry(root)
e1.grid(row=0, column=1)
myLabel2= Label(root, text="SELECT YOUR GENDER: ", padx=5)
myLabel2.grid(row=2, column=0)

global var
var = StringVar()
var.set(None)
R1 = Radiobutton(root, text="MALE",variable=var, value="MALE")
R2 = Radiobutton(root, text="FEMALE",variable=var, value="FEMALE")
R3 = Radiobutton(root, text="OTHERS",variable=var, value="OTHERS")
R1.grid(row=3, column=0)
R2.grid(row=3, column=1)
R3.grid(row=3, column=2)

myLabel7= Label(root, text="SELECT YOUR QUALIFICATION: ", padx=5)
myLabel7.grid(row=5, column=0)
listbox= Listbox(root,
                height=5,
                width =15,
                bg="grey",
                activestyle="dotbox",
                fg="yellow",
                selectmode= SINGLE)
listbox.insert(1,"class 12")
listbox.insert(2,"undergraduate")
listbox.insert(3,"graduated")
listbox.insert(4,"mastered")
listbox.grid(rowspan=1, column=0)
myLabel3= Label(root, text="GIVE YOUR MARKS IN FOLLOWING SUBJECTS: ", padx=10)
myLabel3.grid(row=12, column=0)
myLabel4= Label(root, text="PYTHON: ", padx=10)
myLabel4.grid(row=13, column=0)
e2= Entry(root)
e2.grid(row=13, column=1)
myLabel5= Label(root, text="PHYSICS: ", padx=10)
myLabel5.grid(row=14, column=0)
e3= Entry(root)
e3.grid(row=14, column=1)
myLabel6= Label(root, text="MATHS: ", padx=10)
myLabel6.grid(row=15, column=0)
e4= Entry(root)
e4.grid(row=15, column=1)

def clicked():
    name= e1.get()
    x=int(e2.get())
    y=int(e3.get())
    z=int(e4.get())
    total= x+y+z
    avg= total / 3
    l1= Label(root, text="NAME OF STUDENT IS : " + name.upper() , padx=10)
    l1.grid(row=19, column=0)
    l2= Label(root, text="YOUR GENDER IS: "+ var.get(), padx=10)
    l2.grid(row=20, column=0)
    for i in listbox.curselection():
        h=listbox.get(i)
    l3= Label(root, text="YOUR QUALIFICATION IS: "+ h.upper(), padx=10)
    l3.grid(row=21, column=0)
    l4= Label(root, text="TOTAL MARKS: "+ str(total), padx=10)
    l4.grid(row=23, column=0)
    l5= Label(root, text="YOUR PERCENTAGE: ", padx=10)
    l5.grid(row=24, column=0)
    e5= Entry(root)
    e5.grid(row=24, column=1)
    e5.insert(0, str(avg)+"%")

myButton= Button(root, text="SUBMIT", fg="red", bg="white", padx=20, command= clicked)
myButton.grid(row=17, column=1)
root.mainloop()
