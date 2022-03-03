def time1():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d:%m:%y")
    clock.config(text="Time"+time_string+"\n"+"Date:"+date_string)
    clock.after(200, time1)




from tkinter import *
from tkinter import ttk
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
#import pymysql
import time
root=Tk()
root.title("Clinic Management system")
root.configure(bg="sky blue")
root.geometry("1000x600+200+50")
root.resizable(False,False)

####DTAENTRYFRAME
dataentryframe= Frame(root, bg="sky blue", relief=GROOVE, borderwidth=5)
dataentryframe.place(x=15, y=15, width=300, height=575)

clock=Label(dataentryframe, font=('time', 15, ' bold '), relief=GROOVE, bg='sky blue', foreground='black')
clock.place(x=5, y=5, width=270)
time1()


la1=Label(dataentryframe, text="=====>Menu<=====", font=('time', 20, 'bold'), bg="sky blue", fg="black")
la1.place(x=0, y=70)

####BUTTON
addbtn=Button(dataentryframe, text="1.ADD PATIENT", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
addbtn.place(x=20, y=130)

searchbtn=Button(dataentryframe, text="2.SHOW PATIENT", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
searchbtn.place(x=20, y=180)

Updatebtn=Button(dataentryframe, text="3.UPDATE PATIENT", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
Updatebtn.place(x=20, y=230)

DELETEbtn=Button(dataentryframe, text="4.DELETE PATIENT", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
DELETEbtn.place(x=20, y=280)

EXITbtn=Button(dataentryframe, text="5.EXIT ", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
EXITbtn.place(x=20, y=330)

addbtn=Button(dataentryframe, text="6.SHOW PATIENT", font=("times", 12, 'bold'), width=25, relief=GROOVE, fg="black", bg="sky blue", bd=6,
              activebackground="black", activeforeground="white")
addbtn.place(x=20, y=380)


showdataframe=Frame(root, bg="skyblue", relief=GROOVE, borderwidth=5)
showdataframe.place(x=320, y=120, width=659, height=470)

#######STYLE
style = ttk.Style()
style.theme_use("clam")
style.configure('Treeview.Heading', font=('times', 10, 'bold'),fg="white",bg="black")
style.configure('Treeview.Heading', font=('times', 10, 'bold'),fg="white",bg="black",fieldground="black")
scroll_x=Scrollbar(showdataframe, orient=HORIZONTAL)
scroll_y=Scrollbar(showdataframe, orient=VERTICAL)
dataentrytable=Treeview(showdataframe, columns=('Id', 'NAME', 'MOBILE NO', 'EMAIL', 'ADDRESS'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.config(command=dataentrytable.xview)
scroll_y.config(command=dataentrytable.yview)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)

#######DTAENTRYTABLE HEADING
dataentrytable.heading('Id', text="Id")
dataentrytable.heading('NAME', text="NAME")
dataentrytable.heading('MOBILE NO', text="MOBILE NO")
dataentrytable.heading('EMAIL', text="EMAIL")
dataentrytable.heading('ADDRESS', text="ADDRESS")
dataentrytable['show']='headings'
dataentrytable.column('Id', width=100)
dataentrytable.column('NAME', width=200)
dataentrytable.column('MOBILE NO', width=200)
dataentrytable.column('EMAIL', width=200)
dataentrytable.column('ADDRESS', width=200)
dataentrytable.pack(fill=BOTH, expand=1)

###TITLE FOR DATA FRAME
titledataframe=Frame(root, bg="sky blue", relief=GROOVE, borderwidth=5)
titledataframe.place(x=320, y=13, width=659, height=80)

title=Label(titledataframe, text="CLINIC MANAGEMeNT SYSTEM", font=('time', 20, 'bold'), fg='black', bg='sky blue', width='36')
title.place(x=15, y=15)
root.mainloop()