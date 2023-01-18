from tkinter import *
window = Tk()
window.geometry("500x400+10+20")

window.title("My first Python GUI")

btn = Button(window,text = "Submit", bg="Blue")
btn.place(x=100, y =150)

txtfld = Entry(window,text="This is an entry widget", bd =5)
txtfld.place(x=80,y=100)

def sel():
    selection = "You selected the option" + str(var.get())
    label.config(text = selection)
var = IntVar()
r1 = Radiobutton(window,text="Male", variable= var,value=1,command = sel)
r1.pack(anchor=W)

r2 = Radiobutton(window,text="Female", variable= var,value=2,command = sel)

r2.pack(anchor=W)

label = Label(window)
label.pack()
window.mainloop()