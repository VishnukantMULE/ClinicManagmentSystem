from email.mime import image
from tkinter import *
from PIL import Image, ImageTk



Clinic_Managment_System = Tk()
Clinic_Managment_System.geometry("1150x750")
#Clinic_Managment_System.minsize(900,640)
#Clinic_Managment_System.maxsize(1150,750)
Clinic_Managment_System.title("Clinic Managment System with Akshay Mule")



#wlc lable
welcome = Label(text ="WELCOME TO CLINIC MANAGMENT SYSTEM",bg="lightgreen",fg="red",padx=450,font=("avenir next",15,"bold"))
welcome.pack()

#bg lable
cms_bg = Image.open("cms_bg.jpg")
bg =ImageTk.PhotoImage(cms_bg)
bg_lable = Label(image=bg)
bg_lable.pack()

#buttons
#Button(text="PATIENT").pack(anchor="n",padx=40,pady=0)


# Code Outer ends
Clinic_Managment_System.mainloop()