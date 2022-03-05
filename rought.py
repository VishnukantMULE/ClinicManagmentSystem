import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random as r
import smtplib
import mysql.connector

LARGEFONT = ("Verdana", 15)

def otpgen():
    otp=""
    for i in range(4):
        otp+=str(r.randint(1,9))
    return otp

finalotp=otpgen()





class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Adminlogi, Doctorlogin, Pateint, Admindash, Dotordash, Sdoctor, Pateintdetail, OtpCon, APPbook,sawantINFO,patilINFO,karadINFO,muleIINFO):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]
                  )
        tk.Frame.__init__(self, parent,bg="skyblue")


        # label of frame Layout 2
        label = tk.Label(self, text="WELCOME TO CLINIC MANAGMENT SYSTEM", font=40,bg="red",fg="white",borderwidth=15,padx=450)
        label.place(x=0, y=5)
        img = Image.open('hospital.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage,bg='red').place(x=150, y=180)
        label = tk.Label(self, text="aninash andhale(led)     prathamesh naik      jemin bhanushali     vishnukant mule", font=30, bg="orange", fg="white", padx=380)
        label.place(x=0, y=680)

        button1 = ttk.Button(self, text="ADMIN",
                             command=lambda: controller.show_frame(Adminlogi),style="C.TButton")

        button1.place(x=700,y=200,width=220,height=50)

        button2 = ttk.Button(self, text="DOCTOR",
                             command=lambda: controller.show_frame(Doctorlogin),style="C.TButton")

        button2.place(x=700,y=300,width=220,height=50)

        button2 = ttk.Button(self, text="PATIENT",
                             command=lambda: controller.show_frame(Pateint),style="C.TButton")
        button2.place(x=700,y=400,width=220,height=50)

        button3 = ttk.Button(self, text="DOCTORS DETAILS",
                             command=lambda: controller.show_frame(Sdoctor),style="C.TButton")
        button3.place(x=700,y=500,width=220,height=50)
class Adminlogi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="skyblue")
        label = tk.Label(self, text="ADMIN LOGIN", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('adminlogo.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage).place(x=500, y=90)
        label = tk.Label(self, text="if you want to become admin please contact devloper",
                         font=40, bg="orange", fg="white", padx=500)
        label.place(x=0, y=680)
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'black'), ('active', 'white')],
                  background=[('pressed', '!disabled', 'green'), ('active', 'lightgreen')]
                  )

        # button to show frame 2 with text
        # layout2
        # ADMIN LOGIN

        self.adminid=tk.StringVar()
        self.password=tk.StringVar()



        lbl_user = tk.Label(self, text="ADMIN ID  :", font=("goudy", 15, "bold"),bg='skyblue').place(x=400,y=350)
        self.idname = tk.Entry(self, font=("calibre", 16),borderwidth=1,bg='lightyellow',textvariable=self.adminid).place(x=550,y=350)
        lbl_password = tk.Label(self, text="PASSWORD :", font=("goudy", 15, "bold"),bg='skyblue').place(x=390,y=400)
        self.passwordentry = tk.Entry(self, font=("calibre", 16),borderwidth=1,bg='lightyellow',show = '*',textvariable=self.password).place(x=550,y=400)
        self.submit = ttk.Button(self, text="LOGIN", style="C.TButton", command=self.check_function).place(x=500, y=480, width=248, height=45)

    def check_function(self):

        if self.adminid.get()=="" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.adminid.get() != "abc" or self.password.get() != "123":
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showerror("Welome", f"welcome {self.adminid.get()}")
class Doctorlogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DOCTOR LOGIN ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('adminlogo.png')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage).place(x=500, y=90)
        label = tk.Label(self, text="if you want to become admin please contact devloper",
                         font=40, bg="orange", fg="white", padx=500)
        label.place(x=0, y=680)
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'black'), ('active', 'white')],
                  background=[('pressed', '!disabled', 'green'), ('active', 'lightgreen')]
                  )

        self.adminid = tk.StringVar()
        self.password = tk.StringVar()

        lbl_user = tk.Label(self, text="DOCTOR ID  :", font=("goudy", 15, "bold"), bg='skyblue').place(x=390, y=350)
        self.idname = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow',
                               textvariable=self.adminid).place(x=550, y=350)
        lbl_password = tk.Label(self, text="PASSWORD :", font=("goudy", 15, "bold"), bg='skyblue').place(x=390, y=400)
        self.passwordentry = tk.Entry(self, font=("calibre", 16), borderwidth=1, bg='lightyellow', show='*',
                                      textvariable=self.password).place(x=550, y=400)
        self.submit = ttk.Button(self, text="LOGIN", style="C.TButton", command=self.check_function).place(x=500, y=480,
                                                                                                           width=248,
                                                                                                           height=45)

    def check_function(self):

        if self.adminid.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.adminid.get() != "abc" or self.password.get() != "123":
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showerror("Welome", f"welcome {self.adminid.get()}")
class Pateint(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="PATEINT REGISTRATION FORM ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=470)
        label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)




        # creating the frames in the master

        self.f_name = tk.StringVar()
        self.l_name = tk.StringVar()
        self.e_mail = tk.StringVar()
        self.m_no = tk.StringVar()
        self.DOB = tk.StringVar()
        self.address = tk.StringVar()
        self.pincode = tk.StringVar()
        self.state = tk.StringVar()
        self.var = tk.StringVar()

        self.f_nameE = tk.Entry(self,width=20,font=5, textvariable=self.f_name)
        self.l_nameE = tk.Entry(self, width=20,font=5,textvariable=self.l_name)
        self.e_mailE = tk.Entry(self,width=25,font=5, textvariable=self.e_mail)
        self.m_noE = tk.Entry(self, width=20,font=5,textvariable=self.m_no)
        self.DOBE = tk.Entry(self,width=20,font=5, textvariable=self.DOB)
        self.addressE = tk.Entry(self,width=30,font=5, textvariable=self.address)
        self.pincodeE = tk.Entry(self,width=20,font=5, textvariable=self.pincode)
        self.cityE = tk.Entry(self,width=20,font=5, textvariable=self.state)
        self.Radio_button_maleE = tk.Radiobutton(self, text='Male', fg='black',value="Male",bg='skyblue',font=20,variable=self.var).place(x=450,y=220)
        self.Radio_button_femaleE = tk.Radiobutton(self, text='Female',fg='black', value="Female", bg='skyblue',font=20,variable=self.var).place(x=540,y=220)

        self.f_nameE.place(x=450,y=100)
        self.l_nameE.place(x=450,y=160)
        self.e_mailE.place(x=450,y=280)
        self.m_noE.place(x=450,y=340)
        self.DOBE.place(x=450,y=400)
        self.addressE.place(x=450,y=460)
        self.pincodeE.place(x=450,y=520)
        self.cityE.place(x=450,y=580)

        self.f_nameL = tk.Label(self, text="First Name :",font=6,bg="skyblue").place(x=300,y=100)
        self.l_nameL = tk.Label(self, text="Last Name :",font=6,bg="skyblue").place(x=300,y=160)
        self.gender = tk.Label(self, text="Gender :",font=6,bg="skyblue").place(x=300,y=220)
        self.e_mailL = tk.Label(self, text="E mail :",font=6,bg="skyblue").place(x=300,y=280)
        self.m_noL = tk.Label(self, text="M no :",font=6,bg="skyblue").place(x=300,y=340)
        self.DOBL = tk.Label(self, text="D-O-B :",font=6,bg="skyblue").place(x=300,y=400)
        self.addressL = tk.Label(self, text="Address :",font=6,bg="skyblue").place(x=300,y=460)
        self.pincodeL = tk.Label(self, text="Pin Code :",font=6,bg="skyblue").place(x=300,y=520)
        self.cityL = tk.Label(self, text="City :",font=6,bg="skyblue").place(x=300,y=580)

        self.submit = ttk.Button(self, text="Next", style="C.TButton",command=lambda:[self.sendmail(),self.dataB(), controller.show_frame(OtpCon)] ).place(x=840, y=630,
                                                                                                           width=200,
                                                                                                           height=50)

    def dataB(self):
        conn = mysql.connector.connect(
            user='root', password='', host='127.0.0.1', database='clinic_managment_system')

        emailid = self.e_mail.get()
        fname = self.f_name.get()
        lname = self.l_name.get()
        gender = self.var.get()
        mob = self.m_no.get()
        dob = self.DOB.get()
        address = self.address.get()
        pincode = self.pincode.get()
        state = self.state.get()

        insert_stmt = (
            "INSERT INTO pateint_details(First_Name, Last_Name,Gender,Mobile,Email,D_O_B,Address,Pincode,State)"
            "VALUES (%s, %s, %s, %s, %s ,%s ,%s ,%s ,%s)"
        )
        data = (fname, lname, gender, mob, emailid, dob, address, pincode, state)
        cursor = conn.cursor()

            # Executing the SQL command
        cursor.execute(insert_stmt, data)


            # Commit your changes in the database
        conn.commit()


            # Rolling back in case of error
        #conn.rollback()
        conn.close()
    def sendmail(self):
        emailid = self.e_mail.get()



        try :
          s = smtplib.SMTP('smtp.gmail.com', 587)
          s.starttls()
          s.login("vishnukantmule@gmail.com", "cgezqyarhsxghdfy")
          SUBJECT="Verify your Email address"
          TEXT=f"""TO book your appointment with doctor ,we just need to make sure that this email address is yours.
        
           To verify your email address,use this security code:{finalotp}
        
           if you didnt request this code. you can safely ignore this email.Someone else might have typed youremail address by mistake.
        
           Thanks,
           The Clinic Managment Team"""

          message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

          s.sendmail("vishnukantmule@gmail.com", emailid, message,)
          s.quit()
        except:
            messagebox.showerror("Error", "YOU ENTER WRONG EMAIL-ID PLEASE TRY TO CORRECT")


class Admindash(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ADMIN DASHBORD", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
class Dotordash(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
class Sdoctor(tk.Frame):
    def __init__(self, parent, controller):
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'white'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]
                  )
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="OUR BEST DOCTORS", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)

        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)
        tk.Button(self,text="🢀",bg='white').place(x=30, y=12)


        img3 = Image.open('mahesh.jpg')
        self.tkimage3 = ImageTk.PhotoImage(img3)
        tk.Label(self, image=self.tkimage3,bg='red').place(x=770, y=70)

        img2 = Image.open('shubhamak.jpg')
        self.tkimage2 = ImageTk.PhotoImage(img2)
        tk.Label(self, image=self.tkimage2,bg='red').place(x=150, y=70)

        img1 = Image.open('ganesh.jpg')
        self.tkimage1 = ImageTk.PhotoImage(img1)
        tk.Label(self, image=self.tkimage1,bg='red').place(x=150, y=380)

        img = Image.open('vijita.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage,bg='red').place(x=770, y=380)

        img4 = Image.open('showd.png')
        self.tkimage4 = ImageTk.PhotoImage(img4)
        tk.Label(self, image=self.tkimage4,bg='skyblue').place(x=410, y=200)
        tk.Label(self,text="Keeping You Well",bg="skyblue",font=30).place(x=500,y=450)


        # Buttons
        self.dr_a = ttk.Button(self, text="Dr.Shubhamak SawantT",style="C.TButton",command=lambda: controller.show_frame(sawantINFO)).place(x=160,y=330,width=155,height=32)
        self.dr_b = ttk.Button(self, text="Dr.Mahesh Patil",style="C.TButton",command=lambda: controller.show_frame(patilINFO)).place(x=800,y=330,width=155,height=32)
        self.dr_c = ttk.Button(self, text="Dr.Ganesh Karad",style="C.TButton",command=lambda: controller.show_frame(karadINFO)).place(x=160,y=640,width=155,height=32)
        self.dr_d = ttk.Button(self, text="Dr.Anjali Mule",style="C.TButton",command=lambda: controller.show_frame(muleIINFO)).place(x=800,y=640,width=155,height=32)
class Pateintdetail(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
class OtpCon(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]
                  )
        label = tk.Label(self, text="EMAI-ID CONFIRMATION ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=470)
        label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        self.VALUE = tk.IntVar()
        OTP = tk.Entry(self,width=20,font=20, textvariable=self.VALUE).place(x=500,y=200,height=30)
        self.GENERATE = ttk.Button(self, text="Confirm", style="C.TButton", command=lambda:[self.confirmfn]).place(x=460,y=400,width=300,height=45)


    def confirmfn(self,parent, controller):
        otpsended=finalotp

        if self.VALUE.get() ==otpsended:
            messagebox.showerror("Success", "YOUR EMAIL IS CONFIRMED")
            return lambda : controller.show_frame(APPbook)
        else:
            messagebox.showerror("Error", "INVALID OTP")
            return 0
class APPbook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]

                  )
        self.label = tk.Label(self, text="EMAI-ID CONFIRMATION ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=470)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        self.label.place(x=0, y=5)



        # Book DocterLabel
        self.Docter = tk.Label(self, text="Docter:",bg='skyblue', font='Verdana 15 bold')
        self.Docter.place(x=450, y=200)

        self.Day = tk.Label(self, text="Day:",bg='skyblue', font='Verdana 15 bold')
        self.Day.place(x=450, y=250)

        self.Month = tk.Label(self, text="Month:",bg='skyblue', font='Verdana 15 bold')
        self.Month.place(x=450, y=300)

        self.Year = tk.Label(self, text="Year:",bg='skyblue', font='Verdana 15 bold')
        self.Year.place(x=450, y=350)

        # Book Docter Entry Box

        self.docter_var = tk.StringVar()
        self.day = tk.StringVar()
        self.month = tk.StringVar()
        self.year = tk.StringVar()

        self.Docter_box = ttk.Combobox(self, width=25,font=20, textvariable=self.docter_var, state='readonly')
        self.Docter_box['values'] = ('Dr.SHUBHAMAK SAWANT', 'Dr.MAHESH PATIL', 'Dr.GANESH KARAD', 'Dr.VIJITA SHARMA')
        self.Docter_box.current(0)
        self.Docter_box.place(x=550, y=200)

        self.Day = ttk.Entry(self, width=25,font=20, textvariable=self.day)
        self.Day.place(x=550, y=250)

        self.Month_Box = ttk.Combobox(self, width=25,font=20, textvariable=self.month, state='readonly')
        self.Month_Box['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December')
        self.Month_Box.current(0)
        self.Month_Box.place(x=550, y=300)

        self.Year = ttk.Entry(self, width=25,font=20, textvariable=self.year)
        self.Year.place(x=550, y=350)
        self.submit = ttk.Button(self, text="BOOK OPPOINTMENT",style="C.TButton").place(x=550,y=450,width=250,height=50)
class sawantINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]

                  )
        self.label = tk.Label(self, text="Dr.Shubhamak Sawant", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('shubhamak.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Shubhamak Sawant", bg='skyblue', font=LARGEFONT).place(x=60, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   Scoliosis surgery, minimally invasive and endoscopic spine surgery", fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Spine Surgeon ", fg='black', bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺   MBBS - NSCB Medical college, Jabalpur (2006) ", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                                            y=240)
        self.label = tk.Label(self, text="⏺   MS (ortho) - MGM Medical college, Indore (2009) ", fg='black', bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   Experience of 10 years in spine surgery with special expertise in scoliosis surgery ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)
        self.label = tk.Label(self, text="⏺   Dr.Sawant was Professor in Orthopedics and head of spine unit at (SAIMS), Indores ", fg='black', bg='skyblue',
                              font=20).place(x=390, y=390)
        self.label = tk.Label(self, text="⏺   Role of posterior approach in multisegmental cervical myelopathy  ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=420)
        self.label = tk.Label(self,
                              text="⏺   Predictive factors for progression of spondylolisthesis  ",
                              fg='black', bg='skyblue', font=20).place(x=390, y=450)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺   Prof. K.T. Dholakia Gold Medal- best paper (IOACON 2008) ", fg='black', bg='skyblue', font=20).place(
            x=390, y=540)
        self.label = tk.Label(self, text="⏺   Prof. Sudhir Kapoor gold medal for best case report of the year 2014 ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=570)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● MONDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● TUESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                             y=420)
        self.label = tk.Label(self, text="● WEDNESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                               y=450)
        self.label = tk.Label(self, text="● THRUSDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                              y=480)
        self.label = tk.Label(self, text="● FRIDAY:OFF", fg='black', bg='skyblue', font=10).place(x=30, y=510)
        self.label = tk.Label(self, text="● SATURDAY:  10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                                y=540)
        self.label = tk.Label(self, text="● SUNDAY :  OFF", fg='black', bg='skyblue', font=10).place(x=30, y=570)

        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-9326513775 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)



        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class patilINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]

                  )
        self.label = tk.Label(self, text="Dr.Mahesh Patil", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('mahesh.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Mahesh Patil", bg='skyblue', font=LARGEFONT).place(x=80, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   General Surgery ", fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Laparoscopic Surgery & General Surgery ", fg='black', bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺  MBBS", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                                            y=240)
        self.label = tk.Label(self, text="⏺   MS ", fg='black', bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   2 Years Experience in General surgery ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺  Vice President Centra zone IAGES 2014-2018 ", fg='black', bg='skyblue', font=20).place(
            x=390, y=540)
        self.label = tk.Label(self, text="⏺   Secretary Atysi From 2016 to Till  date. ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=570)

        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● MONDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● TUESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                             y=420)
        self.label = tk.Label(self, text="● WEDNESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                               y=450)
        self.label = tk.Label(self, text="● THRUSDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                              y=480)
        self.label = tk.Label(self, text="● FRIDAY:OFF", fg='black', bg='skyblue', font=10).place(x=30, y=510)
        self.label = tk.Label(self, text="● SATURDAY:  10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                                y=540)
        self.label = tk.Label(self, text="● SUNDAY :  OFF", fg='black', bg='skyblue', font=10).place(x=30, y=570)

        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)
        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-8754236978 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class karadINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]

                  )
        self.label = tk.Label(self, text="Dr.Ganesh Karad", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('ganesh.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label = tk.Label(self, text="Dr.Ganesh Karad", bg='skyblue', font=LARGEFONT).place(x=80, y=290)
        self.label = tk.Label(self, text="Specializations :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=60)
        self.label = tk.Label(self, text="⏺   Internal Medicine ", fg='black', bg='skyblue', font=20).place(x=390, y=100)
        self.label = tk.Label(self, text="⏺   Consultant - Internal Medicine ", fg='black', bg='skyblue', font=20).place(
            x=390, y=130)

        self.label = tk.Label(self, text="Qualification :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=200)
        self.label = tk.Label(self, text="⏺   M.B.B.S. MGM Medical College, Indore ", fg='black', bg='skyblue', font=20).place(x=390,
                                                                                                            y=240)
        self.label = tk.Label(self, text="⏺   M.D. Medicine MGM Medical College, Indore ", fg='black', bg='skyblue', font=20).place(x=390, y=270)

        self.label = tk.Label(self, text="Experience :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=320)
        self.label = tk.Label(self, text="⏺   9 Years Clinical Experience ", fg='black',
                              bg='skyblue', font=20).place(x=390, y=360)

        self.label = tk.Label(self, text="Awards :", fg='red', bg='skyblue', font=LARGEFONT).place(x=370, y=500)
        self.label = tk.Label(self, text="⏺   Attended many conferences ", fg='black', bg='skyblue', font=20).place(
            x=390, y=540)


        self.label = tk.Label(self, text="OPD :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=350)
        self.label = tk.Label(self, text="● MONDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30, y=390)
        self.label = tk.Label(self, text="● TUESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                             y=420)
        self.label = tk.Label(self, text="● WEDNESDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                               y=450)
        self.label = tk.Label(self, text="● THRUSDAY:10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                              y=480)
        self.label = tk.Label(self, text="● FRIDAY:OFF", fg='black', bg='skyblue', font=10).place(x=30, y=510)
        self.label = tk.Label(self, text="● SATURDAY:  10 am to 2 pm", fg='black', bg='skyblue', font=10).place(x=30,
                                                                                                                y=540)
        self.label = tk.Label(self, text="● SUNDAY :  OFF", fg='black', bg='skyblue', font=10).place(x=30, y=570)
        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330, y=50)
        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-9821400548 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)


class muleIINFO(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]

                  )
        self.label = tk.Label(self, text="Dr.Anjali Mule", font=40, bg="red", fg="white", borderwidth=5,
                              padx=530)
        self.label.place(x=0, y=5)
        tk.Button(self,text="⌂",bg='white',command=lambda: controller.show_frame(StartPage)).place(x=10, y=12)

        img = Image.open('vijita.jpg')
        self.tkimage = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.tkimage, bg='red').place(x=60, y=50)
        self.label=tk.Label(self,text="Dr.Anjali S Mule",bg='skyblue',font=LARGEFONT).place(x=80,y=290)
        self.label=tk.Label(self,text="Specializations :",fg='red',bg='skyblue',font=LARGEFONT).place(x=370,y=60)
        self.label=tk.Label(self,text="⏺   Chest Medicine ",fg='black',bg='skyblue',font=20).place(x=390,y=100)
        self.label=tk.Label(self,text="⏺   Consultant - Chest Physician ",fg='black',bg='skyblue',font=20).place(x=390,y=130)




        self.label=tk.Label(self,text="Qualification :",fg='red',bg='skyblue',font=LARGEFONT).place(x=370,y=200)
        self.label=tk.Label(self,text="⏺   M.D ( Chest & TB) ",fg='black',bg='skyblue',font=20).place(x=390,y=240)
        self.label=tk.Label(self,text="⏺   DNBE ",fg='black',bg='skyblue',font=20).place(x=390,y=270)


        self.label=tk.Label(self,text="Experience :",fg='red',bg='skyblue',font=LARGEFONT).place(x=370,y=320)
        self.label=tk.Label(self,text="⏺   Consultant Chest Physician at Jupiter Hospital ",fg='black',bg='skyblue',font=20).place(x=390,y=360)
        self.label=tk.Label(self,text="⏺   Practising Chest Physician since 17years ",fg='black',bg='skyblue',font=20).place(x=390,y=390)
        self.label=tk.Label(self,text="⏺   Ex-Honorary TB specialist and Unit head at GTB Hospital, Seweri ",fg='black',bg='skyblue',font=20).place(x=390,y=420)
        self.label=tk.Label(self,text="⏺   Teaching experience of 9 years in Rajiv Gandhi Medical College ",fg='black',bg='skyblue',font=20).place(x=390,y=450)

        self.label=tk.Label(self,text="Awards :",fg='red',bg='skyblue',font=LARGEFONT).place(x=370,y=500)
        self.label=tk.Label(self,text="⏺   Presented papers at SRSC ",fg='black',bg='skyblue',font=20).place(x=390,y=540)
        self.label=tk.Label(self,text="⏺   Management of MDR TB in resource limited setting in India. ",fg='black',bg='skyblue',font=20).place(x=390,y=570)

        self.label=tk.Label(self,text="OPD :",fg='red',bg='skyblue',font=LARGEFONT).place(x=40,y=350)
        self.label=tk.Label(self,text="● MONDAY:10 am to 2 pm",fg='black',bg='skyblue',font=10).place(x=30,y=390)
        self.label=tk.Label(self,text="● TUESDAY:10 am to 2 pm",fg='black',bg='skyblue',font=10).place(x=30,y=420)
        self.label=tk.Label(self,text="● WEDNESDAY:10 am to 2 pm",fg='black',bg='skyblue',font=10).place(x=30,y=450)
        self.label=tk.Label(self,text="● THRUSDAY:10 am to 2 pm",fg='black',bg='skyblue',font=10).place(x=30,y=480)
        self.label=tk.Label(self,text="● FRIDAY:OFF",fg='black',bg='skyblue',font=10).place(x=30,y=510)
        self.label=tk.Label(self,text="● SATURDAY:  10 am to 2 pm",fg='black',bg='skyblue',font=10).place(x=30,y=540)
        self.label=tk.Label(self,text="● SUNDAY :  OFF",fg='black',bg='skyblue',font=10).place(x=30,y=570)
        self.label = tk.Label(self, text="COTACT :", fg='red', bg='skyblue', font=LARGEFONT).place(x=40, y=610)
        self.label = tk.Label(self, text="● +91-7842513674 ", fg='black', bg='skyblue', font=10).place(x=30, y=650)

        self.label = tk.Label(self, text="", font=40, bg="green", fg="white", borderwidth=0.2,
                              pady=330).place(x=330,y=50)

        button2 = ttk.Button(self, text="REQUEST AN APPOINTMENT",
                             command=lambda: controller.show_frame(Pateint), style="C.TButton")
        button2.place(x=810, y=620, width=220, height=50)




# Driver Code

app = tkinterApp()
app.geometry("1150x750")
app.title("CLINI MANAGMENT SYSTEM")
app.iconbitmap(r'iconico.ico')
app.mainloop()
