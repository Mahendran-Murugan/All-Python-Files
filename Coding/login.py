from tkinter import *
# from tkinter import messagebox
# Tkinter
root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.resizable(False, False)
root.minsize(925, 500)
root.maxsize(1366, 768)
root.configure(bg='#fff')
# Background Image
img = PhotoImage(file="/Users/mahendran/Downloads/UML/login.png")
bg_img = Label(root, image=img, bg="white")
bg_img.place(x=50, y=50)
# Frame for Login
frame = Frame(root, width=350, height=350, bg='white')
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


username = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, font=('Microsoft YaHei UI Light', 11, 'italic'))
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


Password = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*', font=('Microsoft YaHei UI Light', 11, 'italic'))
Password.place(x=30, y=150)
Password.insert(0, 'Password')
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
Password.bind('<FocusIn>', on_click)
Password.bind('<FocusOut>', on_leave)
# Sign in Button
Button(frame, text="Sign in", width=25, pady=7, fg='black', border=0, highlightthickness=0, bg='blue', font=('Microsoft YaHei UI Light', 15)).place(x=47, y=217)
# new user? label
new_user = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 11))
new_user.place(x=75, y=277)
# Register button
register = Button(frame, width=6, text='Register', bg='white', fg='blue', font=('Microsoft YaHei UI Light', 11), border=0, highlightthickness=0, cursor="hand2")
register.place(x=215, y=277)
root.mainloop()
