
from tkinter import *


def getvals():
    print(f"F name : {f_name.get()}")
    print(f"The value of password is {m_name.get()}")

Clinic_Managment_System = Tk()
Clinic_Managment_System.geometry("1150x750")
#Clinic_Managment_System.minsize(900,640)
#Clinic_Managment_System.maxsize(1150,750)
Clinic_Managment_System.title("Clinic Managment System with Akshay Mule")

# creating the frames in the master
registration=Frame(Clinic_Managment_System,width=1150,height=700,borderwidth=2,bg="grey",relief=SUNKEN)
registration.grid()

f_name=StringVar()
m_name=StringVar()
l_name=StringVar()
e_mail=StringVar()
m_no=StringVar()
DOB=StringVar()
address=StringVar()
pincode=StringVar()
state=StringVar()

f_name = Entry(registration, textvariable = f_name)
m_name = Entry(registration, textvariable = m_name)
l_name = Entry(registration, textvariable = l_name)
e_mail = Entry(registration, textvariable = e_mail)
m_no = Entry(registration, textvariable = m_no)
DOB = Entry(registration, textvariable = DOB)
address = Entry(registration, textvariable = address)
pincode = Entry(registration, textvariable = pincode)
city = Entry(registration, textvariable = state)

f_name.grid(row=5,column=20)
m_name.grid(row=6,column=20)
l_name.grid(row=7,column=20)
e_mail.grid(row=8,column=20)
m_no.grid(row=9,column=20)
DOB.grid(row=10,column=20)
address.grid(row=11,column=20)
pincode.grid(row=12,column=20)
city.grid(row=13,column=20)

f_nameL=Label(registration,text="First Name :").grid(row=5,column=19)
m_nameL=Label(registration,text="Middle Name :").grid(row=6,column=19)
l_nameL=Label(registration,text="Last Name :").grid(row=7,column=19)
e_mailL=Label(registration,text="E mail :").grid(row=8,column=19)
m_noL=Label(registration,text="M no :").grid(row=9,column=19)
DOBL=Label(registration,text="D-O-B :").grid(row=10,column=19)
addressL=Label(registration,text="Adress :").grid(row=11,column=19)
pincodeL=Label(registration,text="Pin Code :").grid(row=12,column=19)
cityL=Label(registration,text="City :").grid(row=13,column=19)

Button(registration,text="Submit", command=getvals).grid(row=14,column=20)
# Code Outer ends
Clinic_Managment_System.mainloop()

#akshay