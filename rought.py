import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import self

LARGEFONT = ("Verdana", 19)

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
        tk.Frame.__init__(self, parent)

        # label of frame Layout 2
        label = ttk.Label(self, text="Startpage", font=10)

        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="ADMIN",
                             command=lambda: controller.show_frame(Adminlogi))

        button1.grid(row=1, column=1, padx=10)

        button2 = ttk.Button(self, text="DOCTOR",
                             command=lambda: controller.show_frame(Doctorlogin))

        button2.grid(row=2, column=1, padx=10)

        button2 = ttk.Button(self, text="PATIENT",
                             command=lambda: controller.show_frame(Pateint))
        button2.grid(row=3, column=1, padx=10)

        button3 = ttk.Button(self, text="DOCTORS DETAILS",
                             command=lambda: controller.show_frame(Sdoctor))
        button3.grid(row=4, column=1, padx=10)


class Adminlogi(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="ADMIN LOGIN", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        # button to show frame 2 with text
        # layout2
        # ADMIN LOGIN

        self.adminid = tk.StringVar()
        self.password = tk.StringVar()

        # title = ttk.Label(self, text="ADMIN LOGIN", font=("Impact", 35, "bold")).grid()
        subtitle = ttk.Label(self, text="LOGIN HERE", font=("goudy", 15, "bold")).grid()
        lbl_user = ttk.Label(self, text="Id", font=("goudy", 15, "bold")).grid()
        self.idname = ttk.Entry(self, font=("goudy old style", 15), textvariable=self.adminid).grid()
        lbl_password = ttk.Label(self, text="Password", font=("goudy", 15, "bold")).grid()
        self.password = ttk.Entry(self, font=("goudy old style", 15), textvariable=self.password).grid()
        submit = ttk.Button(self,command=self.check_function, cursor="hand2", text="LOGIN").grid()

    def check_function(self):
        if self.adminid.get() != "AVINASH" or self.password.get() != "123456":
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showerror("Welcome", f"welcome {self.adminid.get()}")


class Doctorlogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="DOCTOR LOGIN ", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)



        # ID
        lbl_user = ttk.Label(self, text="Id", font=("goudy", 15, "bold")).place(
            x=90, y=140)

        self.idname = ttk.Entry(self, font=("goudy old style", 15))
        self.idname.place(x=90, y=170, width=320, height=35)

        lbl_password = ttk.Label(self, text="Password", font=("goudy", 15, "bold")).place(x=90, y=210)

        self.password = ttk.Entry(self, font=("goudy old style", 15))
        self.password.place(x=90, y=240, width=320, height=35)

        # BUTTON
        self.forgetpassword = ttk.Button(self, text="forget password ?", cursor="hand2").place(x=90, y=280)
        self.submit = ttk.Button(self, command=self.check_function, cursor="hand2", text="LOGIN").place(x=90, y=320, width=180,
                                                                                               height=40)

    def check_function(self):
        if self.idname.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.idname.get() != "abc" or self.password.get() != "123":
            messagebox.showerror("Error", "Invalid Username or Password")
        else:
            messagebox.showerror("Welome", f"welcome {self.idname.get()}")


class Pateint(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text=".", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)



        # creating the frames in the master
        self.registration = ttk.Label(self, text="Patient Registration Form", font="time 20 bold").grid(row=0,
                                                                                                           column=3)

        self.f_name = tk.StringVar()
        self.m_name = tk.StringVar()
        self.l_name = tk.StringVar()
        self.e_mail = tk.StringVar()
        self.m_no = tk.StringVar()
        self.DOB = tk.StringVar()
        self.address = tk.StringVar()
        self.pincode = tk.StringVar()
        self.state = tk.StringVar()
        self.var = tk.StringVar()

        self.f_name = ttk.Entry(self, textvariable=self.f_name)
        self.m_name = ttk.Entry(self, textvariable=self.m_name)
        self.l_name = ttk.Entry(self, textvariable=self.l_name)
        self.e_mail = ttk.Entry(self, textvariable=self.e_mail)
        self.m_no = ttk.Entry(self, textvariable=self.m_no)
        self.DOB = ttk.Entry(self, textvariable=self.DOB)
        self.address = ttk.Entry(self, textvariable=self.address)
        self.pincode = ttk.Entry(self, textvariable=self.pincode)
        self.city = ttk.Entry(self, textvariable=self.state)
        self.Radio_button_male = ttk.Radiobutton(self, text='Male', value="Male", variable=self.var).grid(row=10,column=3)
        self.Radio_button_female = ttk.Radiobutton(self, text='Female', value="Female", variable=self.var).grid(row=11,column=3)

        self.f_name.grid(row=1, column=3)
        self.m_name.grid(row=2, column=3)
        self.l_name.grid(row=3, column=3)
        self.e_mail.grid(row=4, column=3)
        self.m_no.grid(row=5, column=3)
        self.DOB.grid(row=6, column=3)
        self.address.grid(row=7, column=3)
        self.pincode.grid(row=8, column=3)
        self.city.grid(row=9, column=3)

        self.f_nameL = ttk.Label(self, text="First Name :").grid(row=1, column=2)
        self.m_nameL = ttk.Label(self, text="Middle Name :").grid(row=2, column=2)
        self.l_nameL = ttk.Label(self, text="Last Name :").grid(row=3, column=2)
        self.e_mailL = ttk.Label(self, text="E mail :").grid(row=4, column=2)
        self.m_noL = ttk.Label(self, text="M no :").grid(row=5, column=2)
        self.DOBL = ttk.Label(self, text="D-O-B :").grid(row=6, column=2)
        self.addressL = ttk.Label(self, text="Adress :").grid(row=7, column=2)
        self.pincodeL = ttk.Label(self, text="Pin Code :").grid(row=8, column=2)
        self.cityL = ttk.Label(self, text="City :").grid(row=9, column=2)

        ttk.Button(self, text="Submit", command=self.getvals).grid(row=18, column=3)

    def getvals(self):
        selectdovtor=tk()
        selectdovtor.geometry("1000x200")
        selectdovtor.mainloop()
        print(f"F name : {self.f_name.get()}")
        print(f"The value of password is {self.m_name.get()}")


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
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)


class APPbook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page 2", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        self.heading = ttk.Label(self, text="Book Appointment", font='Verdana 20 bold')
        self.heading.place(x=470, y=100)

        # Book DocterLabel
        self.Docter = ttk.Label(self, text="Docter:", font='Verdana 10 bold')
        self.Docter.place(x=480, y=145)

        self.Day = ttk.Label(self, text="Day:", font='Verdana 10 bold')
        self.Day.place(x=480, y=165)

        self.Month = ttk.Label(self, text="Month:", font='Verdana 10 bold')
        self.Month.place(x=480, y=185)

        self.Year = ttk.Label(self, text="Year:", font='Verdana 10 bold')
        self.Year.place(x=480, y=205)

        # Book Docter Entry Box

        self.docter_var = tk.StringVar()
        self.day = tk.StringVar()
        self.month = tk.StringVar()
        self.year = tk.StringVar()

        self.Docter_box = ttk.Combobox(self, width=30, textvariable=self.docter_var, state='readonly')
        self.Docter_box['values'] = ('Dr.SHUBHAMAK SAWANT', 'Dr.Mahesh Patil', 'Dr.Ganesh Karad', 'Dr.Vijita Sharma')
        self.Docter_box.current(0)
        self.Docter_box.place(x=550, y=145)

        self.Day = ttk.Entry(self, width=33, textvariable=self.day)
        self.Day.place(x=550, y=168)

        self.Month_Box = ttk.Combobox(self, width=30, textvariable=self.month, state='readonly')
        self.Month_Box['values'] = (
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
            'November',
            'December')
        self.Month_Box.current(0)
        self.Month_Box.place(x=550, y=188)

        self.Year = ttk.Entry(self, width=33, textvariable=self.year)
        self.Year.place(x=550, y=208)


# Driver Code

app = tkinterApp()
app.geometry("1150x750")
app.title("CLINI MANAGMENT SYSTEM")
app.mainloop()
