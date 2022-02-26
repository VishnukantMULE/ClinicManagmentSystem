
from tkinter import *


def getvals():

    print(f"F name : {f_name.get()}")
    print(f"The value of password is {m_name.get()}")
root = Tk()
root.geometry("1150x750")
root.title("Clinic Management By AKSHAY MULE")

#  Frame
Frame_registration = Frame(root,width=100,highlightbackground='black',highlightthickness=3)
Frame_registration.place(x=0, y=0, width=500, height=400)

# creating the frames in the master
registration=Label(root,text="Patient Registration Form",fg="black", font="time 20 bold").grid(row=0,column=3)


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

f_name.grid(row=1,column=3)
m_name.grid(row=2,column=3)
l_name.grid(row=3,column=3)
e_mail.grid(row=4,column=3)
m_no.grid(row=5,column=3)
DOB.grid(row=6,column=3)
address.grid(row=7,column=3)
pincode.grid(row=8,column=3)
city.grid(row=9,column=3)

f_nameL=Label(registration,text="First Name :").grid(row=1,column=2)
m_nameL=Label(registration,text="Middle Name :").grid(row=2,column=2)
l_nameL=Label(registration,text="Last Name :").grid(row=3,column=2)
e_mailL=Label(registration,text="E mail :").grid(row=4,column=2)
m_noL=Label(registration,text="M no :").grid(row=5,column=2)
DOBL=Label(registration,text="D-O-B :").grid(row=6,column=2)
addressL=Label(registration,text="Adress :").grid(row=7,column=2)
pincodeL=Label(registration,text="Pin Code :").grid(row=8,column=2)
cityL=Label(registration,text="City :").grid(row=9,column=2)

Button(registration,text="Submit", command=getvals).grid(row=18,column=3)
# Code Outer ends
root.mainloop()

#akshay