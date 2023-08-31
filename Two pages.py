from tkinter import *
from PIL import Image, ImageTk
# Tkinter
root0 = Tk()
root0.title("Book Bank System Online")
root0.geometry("925x500+300+200")
root0.resizable(False, False)
root0.minsize(925, 500)
root0.maxsize(1366, 768)
root0.configure(bg='#fff')
# Image
img0 = Image.open("/Users/mahendran/Downloads/UML/Entry.png")
img0 = ImageTk.PhotoImage(img0)
bg_img0 = Label(root0, image=img0, bg="white")
bg_img0.place(x=50, y=50)
# Frame for Buttons
frame0 = Frame(root0, width=370, height=370, bg='white')
frame0.place(x=480, y=70)
# Title Label
heading0 = Label(frame0, text="Book Bank System", fg='blue', bg='White', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading0.place(x=90, y=3)


# page 2
def login():
    root0.destroy()
    screen = Tk()
    screen.title("Login")
    screen.geometry("925x500+300+200")
    screen.resizable(False, False)
    screen.minsize(925, 500)
    screen.maxsize(1366, 768)
    screen.configure(bg='#fff')
    # Background Image
    img = Image.open("/Users/mahendran/Downloads/UML/login.png")
    img = ImageTk.PhotoImage(img)
    bg_img = Label(screen, image=img, bg="white")
    bg_img.place(x=50, y=50)
    # Frame for Login
    frame = Frame(screen, width=350, height=350, bg='white')
    frame.place(x=480, y=70)
    # Sign in text
    heading = Label(frame, text="Sign In", fg='blue', bg='White', font=('Microsoft YaHei UI Light', 23, 'bold'))
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
                     font=('Microsoft YaHei UI Light', 11, 'italic'))
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

    Password = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
                     font=('Microsoft YaHei UI Light', 11, 'italic'))
    Password.place(x=30, y=150)
    Password.insert(0, 'Password')
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
    Password.bind('<FocusIn>', on_click)
    Password.bind('<FocusOut>', on_leave)
    # Sign in Button
    Button(frame, text="Sign in", width=25, pady=7, fg='black',bg='blue', border=0, highlightthickness=0,
           font=('Microsoft YaHei UI Light', 15)).place(x=47, y=217)
    # new user? label
    new_user = Label(frame, text="New user? click here -->", fg='black', bg='white',
                     font=('Microsoft YaHei UI Light', 11))
    new_user.place(x=75, y=277)
    # Register button
    register = Button(frame, width=6, text='Register', bg='white', fg='blue', font=('Microsoft YaHei UI Light', 11),
                      border=0, highlightthickness=0, cursor='hand')
    register.place(x=215, y=277)
    screen.mainloop()


# Buttons
btn1 = Button(frame0, text="Login/Register", bg='#000000', fg='black', border=0, highlightthickness=0, command=login)
btn1.place(relx=0.38, rely=0.2, relwidth=0.35, relheight=0.11)
btn2 = Button(frame0, text="Select Book", bg='black', fg='black', border=0, highlightthickness=0)
btn2.place(relx=0.38, rely=0.35, relwidth=0.35, relheight=0.11)
btn3 = Button(frame0, text="Return Book", bg='black', fg='black', border=0, highlightthickness=0)
btn3.place(relx=0.38, rely=0.50, relwidth=0.35, relheight=0.11)
btn4 = Button(frame0, text="Exit", bg='black', fg='black', command=root0.destroy, border=0, highlightthickness=0)
btn4.place(relx=0.38, rely=0.65, relwidth=0.35, relheight=0.11)
root0.mainloop()
