from tkinter import *
root=Tk()
def getvalue():
    print(f"value is :{VALUE.get()}")
root.geometry("1000x600")
root.title("OTP Confirmation")
otp_frame=Frame(root,borderwidth=20).pack()
VALUE=IntVar()
OTP=Entry(otp_frame,textvariable=VALUE).pack(pady=100)
GENERATE=Button(otp_frame,text="Confirm",font=40,command=getvalue).pack()






root.mainloop()