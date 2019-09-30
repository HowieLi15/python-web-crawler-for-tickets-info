from tkinter import *

def GUI():
    top = Tk()
    top.geometry('500x300+500+200')
    L1 = Label(top, text="出发站: ").grid(row=1,column=0)
    L2 = Label(top, text="到达站: ").grid(row=2,column=0)
    L3 = Label(top, text="日期: ").grid(row=3,column=0)
    E1 = Entry(top, bd =5).grid(row=1,column=1)
    E2 = Entry(top, bd =5).grid(row=2,column=1)
    E3 = Entry(top, bd =5).grid(row=3,column=1)
    B = Button(top, text ="查询").grid(row=4,column=0)#, command = )
    top.mainloop()