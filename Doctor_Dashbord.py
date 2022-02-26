from tkinter import *
from tkinter import messagebox
from tkinter import messagebox

class DOCTOR_DASHBOARD:
    def __init__(self, root):
        self.root = root
        self.root.title("DOCTOR_DASHBOARD ")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        # Login Frame
        Frame_login = Frame(self.root, bg="sky blue")
        Frame_login.place(x=0, y=0, width=250, height=750)


        PLANE_login = Frame(self.root, bg="sky blue")
        PLANE_login.place(x=260, y=0, width=700, height=500)


        title = Label(Frame_login, text="DOCTOR DASHBOARD", font=("bold", 11, "bold"), fg="dark blue", bg="sky blue").place(x=20, y=30)
        subtitle = Label(Frame_login, text="", font=("goudy", 15, "bold"), fg="dark blue", bg="sky blue").place(x=20, y=40)





        forgetpassword = Button(Frame_login, text="PATIENT LIST", bd=0, cursor="hand2",font=("goudy old style", 12),fg="skyblue", bg="darkblue").place(x=0, y=70, width=230,height=40)
        submit = Button(Frame_login, cursor="hand2", text="MEDECINE LIST", bd=0,font=("goudy old style", 12), fg="skyblue", bg="darkblue").place(x=0, y=120, width=230,height=40)

        forgetpassword = Button(Frame_login, text="APPOINTMENT STATUS", bd=0, cursor="hand2", font=("goudy old style", 12), fg="skyblue", bg="darkblue").place(x=0, y=170, width=230, height=40)
        submit = Button(Frame_login, cursor="hand2", text="RECEPTIONIST", bd=0, font=("goudy old style", 12),fg="skyblue", bg="darkblue").place(x=0, y=220, width=230, height=40)




root = Tk()
obj = DOCTOR_DASHBOARD(root)
root.mainloop()
