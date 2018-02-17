
from tkinter import*

top = Tk()
msgArray=[]

def helloCallBack():
    #For debug
    #print("Message: %s" % (T.get()))
    #var.set(T.get())

    msgArray.append(T.get())
    #var.set(msgArra)

    listbox.insert(END, T.get())
    
    #B/command= helloCallBack calls the function
    # T.delete deletes the text after the function is executed
    T.delete(0, END) 
    

label = Label(text = "What would you like to do?")
B = Button(top, text ="Send", command = helloCallBack, width =10)

top.title("Not Skype")

top.geometry("640x480")

menubar = Menu(top)
menubar.add_command(label="File")

menubar.add_command(label="Quit",command=sys.exit)
top.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
menubar.add_cascade(label="File", menu=filemenu)

var = StringVar()

#var.set()

message = Message(top, textvariable = var)

message.pack(side ='top')

listbox = Listbox(top, width=40, height=20, justify=LEFT)
listbox.pack(side=LEFT)

listbox.insert(END, "a list entry")

r = Message(top)

#r.place()
def enter(event=None):
    helloCallBack()    
    
T = Entry(top)
T.bind('<Return>', enter)
T.pack()
T.place(x = 0, y = 450)
B.pack()
B.place(x = 450, y = 450)
top.mainloop()


