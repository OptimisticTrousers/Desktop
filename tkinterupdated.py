
from tkinter import*

top = Tk()

def helloCallBack():
   print("Message: %s" % (T.get()))
   var.set(T.get())

label = Label(text = "What would you like to do?")
B = Button(top, text ="Send", command = helloCallBack, width =10)

top.title("Not Skype")

if str=="Hello":
    print("\n Hello")
    
menubar = Menu(top)
menubar.add_command(label="File")

menubar.add_command(label="Quit",command=sys.exit)
top.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
menubar.add_cascade(label="File", menu=filemenu)

var = StringVar()

#var.set()

message = Message(top, textvariable = var, width =1000)

message.pack(side ='top')


r = Message(top)

r.pack(side = 'top')

    
T = Entry(top)
T.pack(side = 'left')
B.pack()
top.mainloop()



