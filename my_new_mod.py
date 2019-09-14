#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     02-04-2019
# Copyright:   (c) user 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
#from diceware import *
from random import *
#import tkMessageBox
import ast
import json
import os
import xlsxwriter
root=Tk()
my_font1=('times',20,'bold')
my_font2=('times',10,'bold')
l1=Label(root,text="RANDOM PASSPHRASE GENERATOR",fg="white",bg="green",height=3)
l1.config(font=my_font1)
l1.pack(side=TOP,fill=X)
f=Frame(root,width=600,height=600)
f.pack()
sec_frame=Frame(root,width=600,height=600)
#sec_frame.pack()

#f.bind("<Button-1>",leftClick)

pass_l1=Label(f,text="ENTER THE NUMBR OF WORDS YOU WANT IN YOUR PASSPHRASE",fg="black",bg="white")
pass_l1.config(font=my_font2)
pass_l1.place(x=20,y=40,width=410,height=20)
e1=Entry(f)
e1.place(x=440,y=40,width=150,height=20)
pass_l2=Label(f,fg="black",bg="white")
#pass_l2.place(x=20,y=70,width=250,height=20)
v1=StringVar()
e2=Entry(f,textvariable=v1)
#e2.place(x=280,y=70,width=280,height=20)
t1=Text(f)
t1.place(x=160,y=130,width=400,height=50)
pass_l3=Label(f,text="YOUR PASSPHRASE\nAPPEARS HERE ->",fg="black",bg="white")
pass_l3.config(font=my_font2)
pass_l3.place(x=160,y=90,width=140,height=30)

pass_l4=Label(f,text="Enter the website name")
pass_l4.config(font=my_font2)
pass_l4.place(x=20,y=200,width=250,height=20)
e3=Entry(f)
e3.place(x=270,y=200,width=250,height=20)
pass_l5=Label(f,text="Enter the master key to view your passwords")
pass_l5.config(font=my_font2)
pass_l5.place(x=20,y=230,width=250,height=20)
e4=Entry(f,show="*")
e4.place(x=270,y=230,width=250,height=20)
t2=Text(f)
t2.place(x=20,y=330,width=500,height=200)
#l4.pack()

def dicenumber():
    diceout =""
    for i in range(5):  # 5 dice rolls
        diceout += str(randint(1,6)) # add result of dice roll to variable
    return diceout

def diceware(x):
    wordlist=open('diceware_wordlist.txt',"r")
    line = wordlist.readline()
    while(line):
        if line.startswith(x):
            wordlist.close()
            line=line[6:]
            return line
        else:
            line=wordlist.readline()

    ''' for line in wordlist:
        if line.startswith(x):
            wordlist.close()
            return line'''
    wordlist.close()

def cal(n):
    s=""
    s1=""
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    for i in range(n):
        s=diceware(dicenumber())# increase number for longer passphrases
        t1.insert(END,s.strip('\n')+" ")
        print(s)
        s1=s1+" "+s
    t1.config(state=DISABLED)



def hello():
    print("hello")
    v2=int(e1.get())
    print(v2)
    cal(v2)
    e1.delete(0)

def hello2():
    t2.delete(END)
    str1=""
    v=str(e4.get())
    if v=="fiona":
        w=open('password.txt',"a+")
        v1=str(e3.get())
        w.write(v1+"\t"+t1.get("1.0",END)+"\n")
    #w1=xlsxwritew.close()

    #tkMessageBox.showMessage("Message","Saved")
        w.close()
        v=str(e3.get())
        #os.system("notepad.exe password.txt")
        w=open('password.txt',"r")
        for line in w:
            str1+=line
        t2.insert(END,str1)
        w.close()
    e4.delete(0)
    e3.delete(0)
    t2.config(state=DISABLED)


def numeric():
    t1.config(state=NORMAL)
    t1.delete(1.0,END)
    nnn=int(e1.get())
    num1=""
    for i in range(nnn):
        num1+=str(randint(0,9))
    t1.insert(END,num1)
    t1.config(state=DISABLED)

var1=IntVar()
cb1=Checkbutton(f,text="FOR NUMERIC PASSWORDS",variable=var1)
#cb1.place(x=280,y=100)
b2=Button(f,text="For numeric passwords click here",command=numeric)
#b2.place(x=280,y=140)

b1=Button(f,text="Click here\nto get your\npassword",fg="black",bg="yellow",command=hello)
b1.config(font=my_font2)
b1.place(x=20,y=90,width=100,height=100)

b2=Button(f,text="Click here to use your new passphrase",fg="black",bg="yellow",command=hello2)
b2.config(font=my_font2)
b2.place(x=20,y=270,width=250,height=30)

root.mainloop()
