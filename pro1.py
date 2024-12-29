import pyautogui as p
import time
from tkinter import *
wind=Tk()

def Go():
    n=int(e1.get())
    m=e2.get()
    go(n,m)

def go(n,m):
    time.sleep(12)
    count=0
    while (count<n):
        p.typewrite(m)
        p.press("enter")
        count+=1

def Cancel():
    e1.delete(0,END);
    e2.delete(0,END);

l1=Label(wind,text='Number of messages')
l2=Label(wind,text='Enter the messages')
e1=Entry(wind)
e2=Entry(wind)
b1=Button(wind,text='Go',command=Go)
b2=Button(wind,text='Clear',command=Cancel)

l1.grid(row=0,column=1)
l2.grid(row=0,column=2)
e1.grid(row=1,column=1)
e2.grid(row=1,column=2)
b1.grid(row=2,column=1)
b2.grid(row=2,column=2)

wind.mainloop()
