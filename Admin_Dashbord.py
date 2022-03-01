def time1():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d:%m:%y")
    clock.config(text="Time"+time_string+"\n"+"Date:"+date_string)
    clock.after(200,time1)




from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter import ttk
from tkinter.ttk import Treeview
#import pymysql
import time
root=Tk()
root.title("Clinic Management system")
root.configure(bg="skyblue")
root.geometry("1000x600+200+50")
root.resizable(False,False)

dataentryframe=Frame(root,bg="skyblue",relief=GROOVE,borderwidth=5)
dataentryframe.place(x=15,y=15,width=300,height=575)

clock=Label(dataentryframe,font=('time,75,bold'),relief=GROOVE,bg='skyblue',foreground='black')
clock.place(x=5,y=5,width=270)
time1()


la1=Label(dataentryframe,text="=====>Menu<=====",font=('time', 20 , 'bold'),bg="skyblue",fg="black")
la1.place(x=0,y=70)


addbtn=Button(dataentryframe, text="1.ADD PATIENT", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
addbtn.place(x=20,y=130)

searchbtn=Button(dataentryframe, text="1.PATIENT LIST", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
searchbtn.place(x=20,y=180)

addbtn=Button(dataentryframe, text="1.PATIENT DETAILS", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
addbtn.place(x=20,y=230)

addbtn=Button(dataentryframe, text="1.DELETE PATIENT", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
addbtn.place(x=20,y=280)

addbtn=Button(dataentryframe, text="1.DOCTOR AVAILABLE", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
addbtn.place(x=20,y=330)

addbtn=Button(dataentryframe, text="1.SHOW APPOINTMENTS", font=("times", 12 ,'bold'), width=25,relief=GROOVE,fg="black", bg="skyblue",bd=6,
              activebackground="black",activeforeground="white")
addbtn.place(x=20,y=380)


showdataframe=Frame(root,bg="skyblue",relief=GROOVE,borderwidth=5)
showdataframe.place(x=320,y=120,width=659,height=470)

titledataframe=Frame(root,bg="skyblue",relief=GROOVE,borderwidth=5)
titledataframe.place(x=320,y=13,width=659,height=80)

title=Label(titledataframe,text="CLINIC MANAGEMeNT SYSTEM",font=('time',20,'bold'),fg='black',bg='skyblue',width='36')
title.place(x=15,y=15)
root.mainloop()