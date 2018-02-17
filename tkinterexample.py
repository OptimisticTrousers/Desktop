import tkinter

#ALL RIGHTS RESERVED RAFALE GARCIA

top = tkinter.Tk()

top.title('Not Skype')


def helloCallBack():
    print("Message: %s" % (e.get()))
    var.set(e.get())

B = tkinter.Button(top, text ='Send', command = helloCallBack)

#w = tkinter.Menu(top, bg ='blue')

var = tkinter.StringVar()

label = tkinter.Message(top, textvariable =var)

menubar  = tkinter.Menu(top)
menubar.add_command(label ="File")

label.pack()

#menubar.add_command(label='Open')

top.config(menu=menubar)






label.pack()

e = tkinter.Entry(top)

r = tkinter.Message(top)

r.pack(side = 'top')


e.pack(side = 'left')

B.pack(side = 'right')
top.mainloop()
