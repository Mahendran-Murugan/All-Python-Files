from tkinter import*
from tkinter import messagebox
class Login:
    def __init__(self, root):
        self. root=root
        self. root. title("Login System")
        self.root.geometry("1366x768")

#login frame
        Frame_login=Frame(self.root, bg="white")
        Frame_login.place(x=330, y=150, width=500, height=400)

#title nd subtitle
        title=Label(Frame_login, text=" Login here", font=("Bold 30") ,fg="black",bg="white"). place(x=90, y=30)
#username
        lbl_user=Label(Frame_login, text=" Username", font=("Bold 15") ,fg="grey",bg="white"). place(x=90, y=140)
        self. username=Entry(Frame_login, font=("Goudy old style",15) ,bg="white")
        self. username.place(x=90, y=170,width=320,height=35)
#password
        lbl_password=Label(Frame_login, text=" Password", font=("Bold 15") ,fg="grey",bg="white"). place(x=90, y=210)
        self. password=Entry(Frame_login, font=("Goudy old style",15) ,bg="white")
        self. password.place(x=90, y=240,width=320,height=35)
#button
        forget=Button(Frame_login, text="forgot password? ",bd=0,cursor=" hand2", font=("Goudy old style", 12) ,fg="grey",bg="white"). place(x=90, y=280)
        submit=Button(Frame_login,command=self.check_function,cursor=" hand2",text="Login ",bd=0, font=("Goudy old style", 15) ,fg="white",bg="black"). place(x=90, y=320,width=180,height=40)
    def check_function(self) :
        if self. username. get() =="" or slef. password. get() =="":
           messagebox. showerror(" Error", "All fields are required", parent=self.root)
        elif self. username. get() !="lakshprabha" or slef. password. get() =="27082003":
           messagebox. showerror(" Error", "Invalid username or password! ", parent=self.root)
        else:
           messagebox. showinfo(" Welcome", "Welcome {self.username.get()}")

root=Tk()
obj=Login(root)
root. mainloop()