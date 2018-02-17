
from tkinter import*

top = Tk()

def helloCallBack():
   print("Hello %s" % (T.get()))

label =Label(text = "What would you like to do?")
B = Button(top, text ="Hello", command = helloCallBack, width =10)

top.title("Not Skype")

if str=="Hello":
    print("\n Hello")
menubar = Menu(top)
menubar.add_command(label="File")

menubar.add_command(label="Quit",command=sys.exit)
sys.exit()
top.config(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open")
menubar.add_cascade(label="File", menu=filemenu)
    
T = Entry(top)
label.pack()
T.pack()
B.pack()
top.mainloop()
