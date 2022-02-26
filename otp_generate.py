from tkinter import *
root=Tk()
def getvalue():
    print(f"value is :{VALUE.get()}")
root.geometry("1000x600")
root.title("OTP Confirmation")
VALUE=IntVar()
OTP=Entry(root,textvariable=VALUE).pack(pady=100)
GENERATE=Button(root,text="Confirm",font=40,command=getvalue).pack()





root.mainloop()