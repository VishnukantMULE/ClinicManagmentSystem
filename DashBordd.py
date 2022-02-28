import tkinter
from tkinter import *

import tk

Clinic_Managment_System = tkinter.Tk()
Clinic_Managment_System.geometry("1150x750")
Clinic_Managment_System.minsize(900,640)
Clinic_Managment_System.maxsize(1150,750)
Clinic_Managment_System.title("Clinic Managment System with Akshay Mule")

maindash=tk.Frame(borderwidth=10).grid(row=0,column=0,sticky='nsew')

#wlc lable
welcome = Label(maindash,text ="WELCOME TO CLINIC MANAGMENT SYSTEM",bg="lightgreen",fg="red",padx=450,font=("avenir next",15,"bold"))
welcome.grid()

#bg lable
#cms_bg = Image.open("cms_bg.jpg")
##bg_lable = Label(image=bg)
#b_lable.pack()

#buttons
#Button(text="PATIENT").pack(anchor="n",padx=40,pady=0)


# Code Outer ends
Clinic_Managment_System.mainloop()
