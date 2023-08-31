from tkinter import *
import ast
from tkinter import messagebox
from PIL import Image, ImageTk

# Tkinter
root0 = Tk()
root0.title("Book Bank System Online")
root0.geometry("925x500+200+100")
root0.resizable(False, False)
# root0.minsize(925, 500)
# root0.maxsize(1366, 768)
root0.configure(bg='#fff')
# Image
img0 = PhotoImage(file="Front page.png")
bg_img0 = Label(root0, image=img0, bg="white")
bg_img0.place(x=65, y=85)
# Frame for Buttons
frame0 = Frame(root0, width=370, height=370, bg='white')
frame0.place(x=480, y=70)
# Title Label
heading0 = Label(frame0, text="Book Bank System", fg='blue', bg='White', font=('Popins', 20, 'bold'))
heading0.place(x=70, y=5)


def login():
    root0.destroy()
    root1 = Tk()
    root1.title("Login")
    root1.geometry("925x500+200+100")
    root1.resizable(False, False)
    root1.configure(bg='#fff')

    def check():
        username1 = username.get()
        passingword = Password.get()

        file = open('data.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)

        try:
            if username1 in r.keys() or Password == r[username1]:
                messagebox.showinfo("Login", "Sign in sucessfully")
            else:
                messagebox.showerror("Invalid", "Invalid Information")
        except:
            messagebox.showerror("Invalid", "Invalid Information")

    # Background Image
    img = PhotoImage(file="Login page.png")
    bg_img = Label(root1, image=img, bg="white")
    bg_img.place(x=50, y=75)
    # Frame for Login

    frame = Frame(root1, width=350, height=350, bg='white')
    frame.place(x=480, y=70)
    # Sign in text
    heading = Label(frame, text="Sign In", fg='blue', bg='White', font=('Popins', 23, 'bold'))
    heading.place(x=100, y=5)

    # Entry for Username

    # on_click function
    def on_click(key):
        username.delete(0, END)

    # on_leave function
    def on_leave(key):
        name = username.get()
        if name == '':
            username.insert(0, 'Username')

    username = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0,
                     font=('Popins', 11, 'italic'))
    username.place(x=30, y=80)
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_click)
    username.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    # Entry for Password

    # on_click function
    def on_click(key):
        Password.delete(0, END)

    # on_leave function
    def on_leave(key):
        name = Password.get()
        if name == '':
            Password.insert(0, 'Password')

    def register():
        root1.destroy()
        screen1 = Tk()
        screen1.title("Register")
        screen1.geometry("925x500+200+100")
        screen1.resizable(False, False)
        screen1.configure(bg='#fff')
        # Background Image
        img1 = Image.open("Register page.png")
        img1 = ImageTk.PhotoImage(img1)
        bg_img1 = Label(screen1, image=img1, bg="white")
        bg_img1.place(x=50, y=90)
        # Frame for Login
        frame1 = Frame(screen1, width=350, height=390, bg='white')
        frame1.place(x=480, y=50)
        # Sign in text
        heading = Label(frame1, text="Register", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=100, y=5)

        def get_data():
            username1 = username.get()
            CPassword1 = CPassword.get()
            RPassword1 = RPassword.get()

            if CPassword1 == RPassword1:
                try:
                    file1 = open("data.txt", 'r+')
                    d = file1.read()
                    r = ast.literal_eval(d)

                    dict2 = {username1: CPassword1}
                    r.update(dict2)
                    file1.truncate(0)
                    file1.close()

                    file1 = open('data.txt', 'a')
                    w = file1.write(str(r))
                    messagebox.showinfo("Register", "Sucessfully Registered")
                except:
                    file1 = open("data.txt", 'a')
                    pp = str({'username1': 'CPassword1'})
                    file1.write(pp)
                    file1.close()
            else:
                messagebox.showerror("Invalid", "Retry")

        def signin():
            screen1.destroy()

        # Entry for Username

        # on_click function
        def on_click(key):
            username.delete(0, END)

        # on_leave function
        def on_leave(key):
            name = username.get()
            if name == '':
                username.insert(0, 'Username')

        username = Entry(frame1, width=25, fg='black', bg='white', highlightthickness=0, border=0,
                         font=('Popins', 11, 'italic'))
        username.place(x=30, y=80)
        username.insert(0, 'Username')
        username.bind('<FocusIn>', on_click)
        username.bind('<FocusOut>', on_leave)
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=107)

        # Entry for Create Password

        # on_click function
        def on_click(key):
            CPassword.delete(0, END)

        # on_leave function
        def on_leave(key):
            name = CPassword.get()
            if name == '':
                CPassword.insert(0, 'Create Password')

        CPassword = Entry(frame1, width=25, fg='black', bg='white', highlightthickness=0, border=0,
                          font=('Popins', 11, 'italic'))
        CPassword.place(x=30, y=150)
        CPassword.insert(0, 'Create Password')
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=177)
        CPassword.bind('<FocusIn>', on_click)
        CPassword.bind('<FocusOut>', on_leave)

        # Entry for Re-enter Password

        # on_click function
        def on_click(key):
            RPassword.delete(0, END)

        # on_leave function
        def on_leave(key):
            name = RPassword.get()
            if name == '':
                RPassword.insert(0, 'Re-Enter Password')

        RPassword = Entry(frame1, width=25, fg='black', bg='white', highlightthickness=0, border=0,
                          font=('Popins', 11, 'italic'))
        RPassword.place(x=30, y=220)
        RPassword.insert(0, 'Re-Enter Password')
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=247)
        RPassword.bind('<FocusIn>', on_click)
        RPassword.bind('<FocusOut>', on_leave)
        # Register Button
        Button(frame1, text="Register", width=39, pady=6, fg='black', bg='blue', border=0, command=get_data).place(x=35,
                                                                                                                   y=280)
        # Already Have an Account? label
        label = Label(frame1, text="I Have an Account?", fg="black", bg="white", font=('Popins', 9))
        label.place(x=90, y=340)
        # Sign in button
        sign_in = Button(frame1, width=6, text='Sign in', bg='white', fg='blue', border=0, cursor='hand2',
                         command=signin)
        sign_in.place(x=200, y=340)
        screen1.mainloop()

    Password = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
                     font=('Popins', 11, 'italic'))
    Password.place(x=30, y=150)
    Password.insert(0, 'Password')
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
    Password.bind('<FocusIn>', on_click)
    Password.bind('<FocusOut>', on_leave)
    # Sign in Button
    Button(frame, text="Sign in", width=39, pady=6, fg='black', bg='blue', border=0
           , command=check).place(x=35, y=217)
    # new user? label
    new_user = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Popins', 9))
    new_user.place(x=75, y=277)
    # Register button
    register = Button(frame, width=6, text='Register', bg='white', fg='blue', font=('Popins', 10), border=0,
                      highlightthickness=0, cursor="hand2", command=register)
    register.place(x=220, y=276)

    root1.mainloop()


# Buttons
btn1 = Button(frame0, text="Login/Register", bg='blue', fg='black', border=0, font=('Popins', 10), command=login)
btn1.place(relx=0.28, rely=0.2, relwidth=0.40, relheight=0.10)
btn2 = Button(frame0, text="Select Book", bg='blue', fg='black', border=0, font=('Popins', 10))
btn2.place(relx=0.28, rely=0.36, relwidth=0.40, relheight=0.10)
btn3 = Button(frame0, text="Return Book", bg='blue', fg='black', border=0, font=('Popins', 10))
btn3.place(relx=0.28, rely=0.52, relwidth=0.40, relheight=0.10)
btn4 = Button(frame0, text="Exit", bg='blue', fg='black', command=root0.destroy, font=('Popins', 10), border=0)
btn4.place(relx=0.28, rely=0.68, relwidth=0.40, relheight=0.10)
root0.mainloop()
