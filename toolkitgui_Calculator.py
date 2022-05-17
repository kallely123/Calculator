from tkinter import *
import parser
import math
root=Tk()
display=Entry(root,bg="silver",fg="black")
display.grid(row=0,columnspan=10)
i=0

def display1(num):
    global i
    display.insert(i,num)
    i=i+1
def AC():
    display.delete(0,END)
def undo():
    e=display.get()
    if len(e):
        new=e[:-1]
        AC()
        display.insert(0,new)
    else:
        AC()
        display.insert(0,"Error")
def operation(opr):
    global i
    display.insert(i,opr)
    l=len(opr)
    i+=l
def equal():
    new = display.get()
    try:
        ans=parser.expr(new).compile()
        result=eval(ans)
        AC()
        display.insert(0,result)
    except:
        AC()
        display.insert(0,"ERROR")
def factorial():
    """Calculates the factorial of the number entered."""
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


b_1=Button(root,text="    1",command=lambda :display1(1),bg="ivory")
b_2=Button(root,text="    2",command=lambda :display1(2),bg="ivory")
b_3=Button(root,text="     3",command=lambda :display1(3),bg="ivory")
b_4=Button(root,text="    4",command=lambda :display1(4),bg="ivory")
b_5=Button(root,text="    5",command=lambda :display1(5),bg="ivory")
b_6=Button(root,text="     6",command=lambda :display1(6),bg="ivory")
b_7=Button(root,text="    7",command=lambda :display1(7),bg="ivory")
b_8=Button(root,text="    8",command=lambda :display1(8),bg="ivory")
b_9=Button(root,text="     9",command=lambda :display1(9),bg="ivory")
b_0=Button(root,text="    0",command=lambda :display1(0),bg="ivory")
b11=Button(root,text="   =",command=lambda :equal(),bg="ivory")
b12=Button(root,text="   +",command=lambda :operation("+"),bg="ivory")
b13=Button(root,text="    -",command=lambda :operation("-"),bg="ivory")
b14=Button(root,text="    *",command=lambda :operation("*"),bg="ivory")
b15=Button(root,text="    /",command=lambda :operation("/"),bg="ivory")
b16=Button(root,text="    %",command=lambda :operation("%"),bg="ivory")
b17=Button(root,text="     .",command=lambda :display1("."),bg="ivory")
b18=Button(root,text="SQR",command=lambda :operation("**2"),bg="ivory")
b19=Button(root,text="DEL",command=lambda :undo(),bg="ivory")
b20=Button(root,text=" AC",command=lambda :AC(),bg="ivory")
b21=Button(root,text="     Pi",command=lambda :operation("*3.14"),bg="lightblue")
b22=Button(root,text="  EXP",command=lambda :operation("**"),bg="lightblue")
b23=Button(root,text="        !",command=lambda :factorial,bg="lightblue")
b24=Button(root,text="       (",command=lambda :display1("("),bg="lightblue")
b25=Button(root,text="       )",command=lambda :display1(")"),bg="lightblue")
b_1.grid(row=4,column=0)
b_2.grid(row=4,column=1)
b_3.grid(row=4,column=2)
b_4.grid(row=3,column=0)
b_5.grid(row=3,column=1)
b_6.grid(row=3,column=2)
b_7.grid(row=2,column=0)
b_8.grid(row=2,column=1)
b_9.grid(row=2,column=2)
b_0.grid(row=5,column=1)
b11.grid(row=5,column=3)
b12.grid(row=4,column=3)
b13.grid(row=3,column=3)
b14.grid(row=2,column=3)
b15.grid(row=1,column=3)
b16.grid(row=5,column=2)
b17.grid(row=5,column=0)
b18.grid(row=1,column=2)
b19.grid(row=1,column=0)
b20.grid(row=1,column=1)
b21.grid(row=1,column=4)
b22.grid(row=2,column=4)
b23.grid(row=3,column=4)
b24.grid(row=4,column=4)
b25.grid(row=5,column=4)
root.mainloop()