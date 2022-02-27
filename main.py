import tkinter as tk
from tkinter import messagebox

def show_frame(frame):
   frame.tkraise()
window=tk.Tk()
window.geometry("1150x750")
window.title("CLINI MANAGMENT SYSTEM")

window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

maindashF1=tk.Frame(window,background="skyblue")
adminloginF2=tk.Frame(window,background="green")
admindashF3=tk.Frame(window,background="orange")
#maindash.grid(row=0,column=0,sticky='nsew')


for frame in (maindashF1,adminloginF2,admindashF3):
   frame.grid(row=0,column=0,sticky='nsew')

#main dashbord Code
welcome = tk.Label(maindashF1,text ="WELCOME TO CLINIC MANAGMENT SYSTEM",bg="lightgreen",fg="red",padx=450,font=("avenir next",15,"bold"))
welcome.grid()
adminB=tk.Button(maindashF1,text="ADMIN",font=60,command=lambda:show_frame(adminloginF2)).grid(row=2,pady=70)
DoctorB=tk.Button(maindashF1,text="DOCTOR",font=60).grid(row=3,pady=70)
pateintB=tk.Button(maindashF1,text="PATEINT",font=60).grid(row=4,pady=70)



#admin login code
#bg = tk.PhotoImage(file="")
#tk.Label(adminloginF2, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

# ADMIN LOGIN
title = tk.Label(adminloginF2, text="ADMIN LOGIN", font=("Impact", 35, "bold"), fg="blue", bg="sky blue").grid()
subtitle = tk.Label(adminloginF2, text="LOGIN HERE", font=("goudy", 15, "bold"), fg="blue", bg="sky blue").grid()


# ID
lbl_user = tk.Label(adminloginF2, text="Id", font=("goudy", 15, "bold"), fg="blue", bg="sky blue").grid()

idname= tk.StringVar()
password=tk.StringVar()

idnameG = tk.Entry(adminloginF2, font=("goudy old style", 15), bg="white",textvariable=idname).grid()
lbl_password = tk.Label(adminloginF2, text="Password", font=("goudy", 15, "bold"), fg="blue", bg="sky blue").grid()

password = tk.Entry(adminloginF2, font=("goudy old style", 15), bg="white",textvariable=password)
password.grid()

def checkfun() :
   if(idname.get()=="123"):
      print("you are right")
   elif(idname.get()==""):
      messagebox.showerror("Error", "All fields are required")
   else:
      messagebox.showerror("Error", "Invalid Username or Password")
# BUTTON
forgetpassword = tk.Button(adminloginF2, text="forget password ?", bd=0, cursor="hand2", font=("goudy old style", 12),fg="darkblue", bg="skyblue").grid()
submit = tk.Button(adminloginF2, cursor="hand2", text="LOGIN", bd=0,font=("goudy old style", 12), fg="skyblue", bg="darkblue",command=checkfun).grid()








show_frame(maindashF1)
window.mainloop()