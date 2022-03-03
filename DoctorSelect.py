
from tkinter import *

Clinic_Managment_System = Tk()
Clinic_Managment_System.geometry("1150x750")

dr_detail=Frame(Clinic_Managment_System,width=0,height=550,relief=SUNKEN).grid()


#Labke
dr_a_l=Label(dr_detail,text="Dr.SHUBHAMAK SAWANT",font=17).grid(column=1,row=3,padx=2)
dr_ad_l=Label(dr_detail,text="Cardiac Surgeon,M.B.B.S. \n Joint specialist",font=4).grid(column=1,row=4,padx=2,pady=1)

dr_b_l=Label(dr_detail,text="Dr.Mahesh Patil",font=17).grid(column=4,row=3,padx=2)
dr_bd_l=Label(dr_detail,text="MD.[Hom]\n B.H.M.S., N.H.M.C. (mumbai)",font=4).grid(column=4,row=3,padx=2,pady=1)

dr_c_l=Label(dr_detail,text="Dr.Ganesh Karad",font=17).grid(column=8,row=3,padx=2)
dr_bd_l=Label(dr_detail,text="Cardiac Surgeon,M.B.B.S.",font=4).grid(column=8,row=6,padx=2,pady=1)

dr_d_l=Label(dr_detail,text="Dr.Vijita Sharma",font=17).grid(column=15,row=5,padx=2)
dr_bd_l=Label(dr_detail,text="Cardiac Surgeon,M.B.B.S.",font=4).grid(column=12,row=4,padx=2,pady=1)



#Buttons
dr_a=Button(dr_detail,text="BOOK APPOINTMENT",font=17).grid(column=1,row=6,padx=25)
dr_b=Button(dr_detail,text="BOOK APPOINTMENT",font=17).grid(column=4,row=6,padx=25)
dr_c=Button(dr_detail,text="BOOK APPOINTMENT",font=17).grid(column=8,row=6,padx=25)
dr_d=Button(dr_detail,text="BOOK APPOINTMENT",font=17).grid(column=10,row=6,padx=25)





Clinic_Managment_System.mainloop()
