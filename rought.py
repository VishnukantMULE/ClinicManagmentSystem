import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import random as r
import smtplib

LARGEFONT = ("Verdana", 40)

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
        for F in (
        StartPage, Adminlogi, Doctorlogin, Pateint, Admindash, Dotordash, Sdoctor, Pateintdetail, OtpCon, APPbook):
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
        tk.Label(self, image=self.tkimage).place(x=150, y=180)
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
                             command=lambda: controller.show_frame(APPbook),style="C.TButton")
        button3.place(x=700,y=500,width=220,height=50)


class Adminlogi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="skyblue")
        label = tk.Label(self, text="ADMIN LOGIN", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
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

 #   def check_function(self):
     #   if self.adminid.get() != "AVINASH" or self.password.get() != "123456":
     #       messagebox.showerror("Error", "Invalid Username or Password")
      #  else:
       #     messagebox.showerror("Welcome", f"welcome {self.adminid.get()}")


class Doctorlogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="skyblue")
        label = tk.Label(self, text="DOCTOR LOGIN ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=550)
        label.place(x=0, y=5)
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
        self.Radio_button_maleE = tk.Radiobutton(self, text='Male', fg='#ff6700',value="Male",bg='skyblue',font=20,variable=self.var).place(x=450,y=220)
        self.Radio_button_femaleE = tk.Radiobutton(self, text='Female',fg='#fc46aa', value="Female", bg='skyblue',font=20,variable=self.var).place(x=540,y=220)

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

        self.submit = ttk.Button(self, text="Next", style="C.TButton",command=lambda:[self.sendmail(), controller.show_frame(OtpCon)] ).place(x=840, y=630,
                                                                                                           width=200,
                                                                                                           height=50)




    def sendmail(self):
        print(finalotp)
        emailid = self.e_mail.get()
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
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DOCTORS DETAILS", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # Labke
        self.dr_a_l = ttk.Label(self, text="Dr.SHUBHAMAK SAWANT", font=17).grid(column=1, row=3, padx=2)
        self.dr_ad_l = ttk.Label(self, text="Cardiac Surgeon,M.B.B.S. \n Joint specialist", font=4).grid(column=1, row=4,
                                                                                                     padx=2, pady=1)

        self.dr_b_l = ttk.Label(self, text="Dr.Mahesh Patil", font=17).grid(column=4, row=3, padx=2)
        self.dr_bd_l = ttk.Label(self, text="MD.[Hom]\n B.H.M.S., N.H.M.C. (mumbai)", font=4).grid(column=4, row=4, padx=2,
                                                                                               pady=1)

        self.dr_c_l = ttk.Label(self, text="Dr.Ganesh Karad", font=17).grid(column=8, row=3, padx=2)
        self.dr_bd_l = ttk.Label(self, text="Cardiac Surgeon,M.B.B.S.", font=4).grid(column=1, row=4, padx=2, pady=1)

        self.dr_d_l = ttk.Label(self, text="Dr.Vijita Sharma", font=17).grid(column=10, row=3, padx=2)
        self.dr_bd_l = ttk.Label(self, text="Cardiac Surgeon,M.B.B.S.", font=4).grid(column=1, row=4, padx=2, pady=1)

        # Buttons
        self.dr_a = ttk.Button(self, text="more info").grid(column=1, row=6, padx=25,pady=10)
        self.dr_b = ttk.Button(self, text="more info").grid(column=4, row=6, padx=25)
        self.dr_c = ttk.Button(self, text="more info").grid(column=8, row=6, padx=25)
        self.dr_d = ttk.Button(self, text="more info").grid(column=10, row=6, padx=25)


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
        self.VALUE = tk.IntVar()
        OTP = tk.Entry(self,width=20,font=20, textvariable=self.VALUE).place(x=500,y=200,height=30)
        self.GENERATE = ttk.Button(self, text="Confirm", style="C.TButton", command=lambda:[self.confirmfn,controller.show_frame(APPbook)]).place(x=460,y=400,width=300,height=45)


    def confirmfn(self):
        otpsended=finalotp

        if self.VALUE.get() ==otpsended:
            messagebox.showerror("Success", "YOUR EMAIL IS CONFIRMED")
        else:
            messagebox.showerror("Error", "INVALID OTP")







class APPbook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#00FFFF")
        style = ttk.Style()
        style.map("C.TButton",
                  foreground=[('pressed', 'red'), ('active', 'red')],
                  background=[('pressed', '!disabled', 'red'), ('active', 'lightgreen')]
                  )
        self.label = tk.Label(self, text="EMAI-ID CONFIRMATION ...", font=40, bg="red", fg="white", borderwidth=5,
                         padx=470)
        self.label.place(x=0, y=5)



        # Book DocterLabel
        self.Docter = tk.Label(self, text="Docter:",bg='#00FFFF', font='Verdana 15 bold')
        self.Docter.place(x=450, y=200)

        self.Day = tk.Label(self, text="Day:",bg='#00FFFF', font='Verdana 15 bold')
        self.Day.place(x=450, y=250)

        self.Month = tk.Label(self, text="Month:",bg='#00FFFF', font='Verdana 15 bold')
        self.Month.place(x=450, y=300)

        self.Year = tk.Label(self, text="Year:",bg='#00FFFF', font='Verdana 15 bold')
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


# Driver Code

app = tkinterApp()
app.geometry("1150x750")
app.title("CLINI MANAGMENT SYSTEM")
app.iconbitmap(r'iconico.ico')
app.mainloop()
