from tkinter import *
from tkinter import messagebox
from tkinter import messagebox

class Admin_Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Doctor_Login System")
        self.root.geometry("1030x750")
        self.root.resizable(False, False)

        self.bg = PhotoImage(file="")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #Login Frame
        Frame_login = Frame(self.root, bg="light green")
        Frame_login.place(x=250, y=150, width=500, height=400)

        # ADMIN LOGIN
        title = Label(Frame_login, text="DOCTOR LOGIN", font=("Impact", 35, "bold"), fg="Dark green", bg="light green").place(x=90,y=30)
        subtitle = Label(Frame_login, text="LOGIN HERE", font=("goudy", 15, "bold"), fg="Dark green", bg="light green").place(x=90,y=100)

        # ID
        lbl_user = Label(Frame_login, text="Id", font=("goudy", 15, "bold"), fg="Dark green", bg="light green").place(x=90,y=140)

        self.idname = Entry(Frame_login,  font=("goudy old style", 15 ), bg="white")
        self.idname.place(x=90,y=170,width=320,height=35)

        lbl_password = Label(Frame_login, text="Password", font=("goudy", 15, "bold"), fg="Dark green", bg="lightgreen").place(x=90, y=210)

        self.password = Entry(Frame_login, font=("goudy old style", 15), bg="white")
        self.password.place(x=90, y=240, width=320, height=35)

        #BUTTON
        forgetpassword = Button(Frame_login, text="forget password ?",bd=0,cursor="hand2",font=("goudy old style", 12),fg="darkgreen", bg="lightgreen").place(x=90,y=280)
        submit = Button(Frame_login,command=self.check_function,cursor="hand2", text="LOGIN", bd=0, font=("goudy old style", 12), fg="light green",bg="Dark green").place(x=90, y=320,width=180 ,height=40)



    def check_function(self):
         if self.idname.get() == "" or self.password.get() == "":
             messagebox.showerror("Error", "All fields are required", parent=self.root)
         elif self.idname.get() != "AVINASH" or self.password.get() != "123456":
             messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
         else:
             messagebox.showerror("Welome", f"welcome {self.idname.get()}")
root = Tk()
obj = Admin_Login(root)
root.mainloop()