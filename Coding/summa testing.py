from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime
import mysql.connector as db


# Tkinter
class library:
    def log_check1(self):
        try:
            if ma == True:
                root0.destroy()
                try:
                    self.select_book()
                except Exception as e:
                    print(e, 1)
        except Exception as e:
            print(e, 2)
            messagebox.showerror("Invalid", "Please Login First")

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def log_check2(self):
        try:
            if ka == True:
                root0.destroy()
                self.return_book()
        except Exception as e:
            print(e)
            messagebox.showerror("Invalid", "Please Login First")

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def log_check3(self):
        try:
            if la == True:
                root0.destroy()
                self.add_book()
        except Exception as e:
            print(e)
            messagebox.showerror("Invalid", "Please Login First")

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page(self):
        global root0
        root0 = Tk()
        root0.title("Book Bank System Online")
        root0.geometry("925x500+200+100")
        root0.resizable(False, False)
        # root0.minsize(925, 500)
        # root0.maxsize(1366, 768)
        root0.configure(bg='#fff')
        # Image
        try:
            img0 = PhotoImage(file="/Users/mahendran/Documents/Programming/Python 3.11/Coding/Front page.png")
            bg_img0 = Label(root0, image=img0, bg="white")
            bg_img0.place(x=65, y=85)
        except Exception as e:
            print(e)

        # Frame for Buttons
        frame0 = Frame(root0, width=370, height=370, bg='#fff')
        frame0.place(x=480, y=70)
        # Title Label
        heading0 = Label(frame0, text="Book Bank System", fg='Red', bg='White', font=('Popins', 22, 'bold'))
        heading0.place(x=70, y=5)
        # Buttons
        btn1 = Button(frame0, text="Login/Register", bg='orange', fg='black', border=0, font=('Popins', 10),
                      command=self.signin_1)
        btn1.place(relx=0.34, rely=0.2, relwidth=0.40, relheight=0.10)
        btn3 = Button(frame0, text="Add Book", bg='orange', fg='#000', border=0, font=('Popins', 10),
                      command=self.log_check3)
        btn3.place(relx=0.34, rely=0.36, relwidth=0.40, relheight=0.10)
        btn2 = Button(frame0, text="Select Book", bg='orange', fg='#000', border=0, font=('Popins', 10),
                      command=self.log_check1)
        btn2.place(relx=0.34, rely=0.52, relwidth=0.40, relheight=0.10)
        btn3 = Button(frame0, text="Return Book", bg='orange', fg='#000', border=0, font=('Popins', 10),
                      command=self.log_check2)
        btn3.place(relx=0.34, rely=0.68, relwidth=0.40, relheight=0.10)
        btn4 = Button(frame0, text="Exit", bg='orange', fg='#000', command=root0.destroy, font=('Popins', 10), border=0)
        btn4.place(relx=0.34, rely=0.84, relwidth=0.40, relheight=0.10)
        root0.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def login(self):
        global root1
        root1 = Tk()
        root1.title("Login")
        root1.geometry("925x500+200+100")
        root1.resizable(False, False)
        root1.configure(bg='#fff')

        def check():
            username1 = username.get()
            passingword = Password.get()
            if username1 == '' or passingword == '' or username1 == 'Username' or passingword == 'Password':
                messagebox.showerror("Invalid", "All feilds are required")
            else:
                try:
                    con = db.connect(host="localhost", user="root", password='')
                    cursor = con.cursor()
                    q = "use userinfo"
                    cursor.execute(q)
                except Exception as e:
                    print(e, 1)
                    messagebox.showerror("Sorry", "Database connection failed")
                    return
                query = 'select *from userdata where username=%s and createpassword=%s'
                cursor.execute(query, (username.get(), Password.get()))
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid username or password')
                else:
                    global ma, ka
                    ma = True
                    ka = True
                    cursor.close()
                    con.close()
                    messagebox.showinfo('Login', 'Welcome to Book Bank System')

        # Background Image
        img = PhotoImage(file="/Users/mahendran/Documents/Programming/Python 3.11/Coding/Login page.png")
        bg_img = Label(root1, image=img, bg="white")
        bg_img.place(x=50, y=75)
        # Frame for Login

        frame = Frame(root1, width=350, height=350, bg='#fff')
        frame.place(x=480, y=70)
        # Sign in text
        heading = Label(frame, text="Student Login", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=125, y=5)

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

        Password = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
                         font=('Popins', 11, 'italic'))
        Password.place(x=30, y=150)
        Password.insert(0, 'Password')
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
        Password.bind('<FocusIn>', on_click)
        Password.bind('<FocusOut>', on_leave)

        # Sign in Button
        Button(frame, text="Login", width=32, pady=6, fg='#fff', bg='blue', border=0, command=check).place(x=55, y=217)
        # new user? label
        new_user = Label(frame, text="Don't have an account ?", fg='black', bg='white', font=('Popins', 9))
        new_user.place(x=75, y=267)
        # Register button
        register = Button(frame, width=6, text='Register', bg='white', fg='blue', font=('Popins', 10), border=0,
                          highlightthickness=0, cursor="hand2", command=self.register1)
        register.place(x=220, y=266)
        # Home Button
        Button(root1, text="Home", width=10, pady=6, fg='black', bg='orange', border=0, command=self.Entry_page1).place(
            x=15, y=25)
        # Librarian login
        Button(root1, text="Librarian", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.lib_login).place(x=785, y=25)
        root1.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def librarian_login_page(self):
        global root3
        root3 = Tk()
        root3.title("Login")
        root3.geometry("925x500+200+100")
        root3.resizable(False, False)
        root3.configure(bg='#fff')

        def checking():
            username1 = username.get()
            passingword = Password.get()
            if username1 == '' or passingword == '' or username1 == 'Username' or passingword == 'Password':
                messagebox.showerror("Invalid", "All feilds are required")
            elif username1 == 'Admin' and passingword == 'root@1':
                global la
                la = True
                messagebox.showinfo('Login', 'Welcome to Book Bank System')
            else:
                messagebox.showerror('Error', 'Invalid username or password')

        img = PhotoImage(file="Login page.png")
        bg_img = Label(root3, image=img, bg="white")
        bg_img.place(x=50, y=75)
        # Frame for Login

        frame = Frame(root3, width=350, height=350, bg='#fff')
        frame.place(x=480, y=70)
        # Sign in text
        heading = Label(frame, text="Librarian Login", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=125, y=5)

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

        Password = Entry(frame, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
                         font=('Popins', 11, 'italic'))
        Password.place(x=30, y=150)
        Password.insert(0, 'Password')
        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
        Password.bind('<FocusIn>', on_click)
        Password.bind('<FocusOut>', on_leave)

        # Sign in Button
        Button(frame, text="Login", width=32, pady=6, fg='#fff', bg='blue', border=0, command=checking).place(x=55,
                                                                                                              y=217)
        # Home Button
        Button(root3, text="Home", width=10, pady=6, fg='black', bg='orange', border=0, command=self.Entry_page6).place(
            x=15, y=25)
        # Student login
        Button(root3, text="Student", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.stu_login).place(x=785, y=25)
        root3.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def register(self):

        global screen1
        screen1 = Tk()
        screen1.title("Register")
        screen1.geometry("925x500+200+100")
        screen1.resizable(False, False)
        screen1.configure(bg='#fff')
        # Background Image
        img1 = Image.open("/Users/mahendran/Documents/Programming/Python 3.11/Coding/Register page.png")
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

            if username1 == '' or CPassword1 == '' or RPassword1 == '' or username1 == 'Username' or CPassword1 == 'Create Password' or RPassword1 == 'Re-Enter Password':
                messagebox.showerror("Invalid", "All feilds are required")
            elif CPassword1 != RPassword1:
                messagebox.showerror("Invalid", "Password must be same")
            else:
                try:
                    con = db.connect(host="localhost", user="root", password='')
                    cursor = con.cursor()
                except Exception as e:
                    print(e, 1)
                    messagebox.showerror("Sorry", "Database connection failed")
                    return
                try:
                    q = "create database userinfo"
                    cursor.execute(q)
                    q = "use userinfo"
                    cursor.execute(q)
                except Exception as e:
                    print(e, 2)
                    try:
                        cursor.execute("use userinfo")
                        q = "create table userdata(username varchar(20),createpassword varchar(20),reenteredpassword varchar(20),primary key(username))"
                        cursor.execute(q)
                    except Exception as e:
                        print(e, 'table')

                try:
                    q = "insert into userdata(username,createpassword,reenteredpassword) values(%s,%s,%s)"
                    cursor.execute(q, (username1, CPassword1, RPassword1))
                    k = True
                except Exception as e:
                    print(e, 3)
                    messagebox.showerror("Error", "username is already taken.")
                con.commit()
                cursor.close()
                con.close()
                try:
                    if k == True:
                        messagebox.showinfo("Registration", "Registration Sucessful")
                except:
                    messagebox.showerror("Error", "Try again")

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

        CPassword = Entry(frame1, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
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

        RPassword = Entry(frame1, width=25, fg='black', bg='white', highlightthickness=0, border=0, show='*',
                          font=('Popins', 11, 'italic'))
        RPassword.place(x=30, y=220)
        RPassword.insert(0, 'Re-Enter Password')
        Frame(frame1, width=295, height=2, bg='black').place(x=25, y=247)
        RPassword.bind('<FocusIn>', on_click)
        RPassword.bind('<FocusOut>', on_leave)
        # Register Button
        Button(frame1, text="Register", width=39, pady=6, fg='white', bg='blue', border=0, command=get_data).place(x=35,
                                                                                                                   y=280)
        # Already Have an Account? label
        label = Label(frame1, text="I Have an Account?", fg="black", bg="white", font=('Popins', 9))
        label.place(x=90, y=340)
        # Sign in button
        sign_in = Button(frame1, width=6, text='Login', bg='white', fg='blue', border=0, cursor='hand2',
                         command=self.Entry_page5)
        sign_in.place(x=200, y=340)
        # Home Button
        Button(screen1, text="Home", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.Entry_page5).place(x=15, y=25)
        screen1.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_book(self):
        global screen4
        screen4 = Tk()
        screen4.geometry("925x500+200+100")
        screen4.resizable(False, False)
        screen4.configure(bg='#fff')
        screen4.title("Add book")
        frame4 = Frame(screen4, width=500, height=400, bg='#fff')
        frame4.place(x=250, y=30)
        heading = Label(frame4, text="Add book", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=175, y=5)
        Label(frame4, text="Book Name ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=95)
        Label(frame4, text="Author    ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=145)
        Label(frame4, text="Quantity  ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=195)
        sbmitbtn = Button(frame4, width=10, text="Submit", font=('popins', 15, 'bold'), bg="blue", fg="white",
                          command=self.add_bo).place(x=200, y=280)
        global bu1, au1, qu1
        bu1 = StringVar()
        au1 = StringVar()
        qu1 = StringVar()
        bn = Entry(frame4, textvariable=bu1, width=39, font=('popins', 12)).place(x=170, y=100)
        au = Entry(frame4, textvariable=au1, width=39, font=('popins', 12)).place(x=170, y=150)
        qu = Entry(frame4, textvariable=qu1, width=39, font=('popins', 12)).place(x=170, y=200)
        Button(screen4, text="Home", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.Entry_page7).place(x=15, y=25)
        screen4.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def select_book(self):
        global screen2
        screen2 = Tk()
        screen2.geometry("925x500+200+100")
        screen2.resizable(False, False)
        screen2.configure(bg='#fff')
        screen2.title("Select book")
        frame2 = Frame(screen2, width=500, height=400, bg='#fff')
        frame2.place(x=250, y=30)
        heading = Label(frame2, text="Select Book", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=175, y=5)
        Label(frame2, text="Book Name ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=95)
        Label(frame2, text="Author    ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=145)
        Label(frame2, text="Quantity  ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=30, y=195)
        sbmitbtn = Button(frame2, width=10, text="Submit", font=('popins', 15, 'bold'), bg="blue", fg="white",
                          command=self.sel_bo).place(x=200, y=280)
        option = []
        try:
            global con, cursor
            con = db.connect(host="localhost", user="root", password='')
            cursor = con.cursor()
            q = 'use userinfo'
            cursor.execute(q)
        except Exception as e:
            print(e, 1)
            messagebox.showerror("Invalid", "Database connection failed")
            return
        q = 'select bookname from book'
        cursor.execute(q)
        row = cursor.fetchall()
        for k in row:
            option.append(str(k[0]))
        global var, author1, quantity1
        var = StringVar()
        var.set('--select book--')
        author1 = StringVar()
        quantity1 = StringVar()
        b_name = OptionMenu(frame2, var, *option)
        b_name.configure(width=27, font=('popins', 12), bg='#d3d3d3')
        b_name.place(x=170, y=100)
        b_name.config(width=27, font=('popins', 12), bg='#d3d3d3')
        author = Entry(frame2, textvariable=author1, width=39, font=('popins', 12)).place(x=170, y=150)
        quantity = Entry(frame2, textvariable=quantity1, width=39, font=('popins', 12)).place(x=170, y=200)
        Button(screen2, text="Home", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.Entry_page2).place(x=15, y=25)
        screen2.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def return_book(self):
        global screen3
        screen3 = Tk()
        screen3.geometry("925x500+200+100")
        screen3.resizable(False, False)
        screen3.configure(bg='#fff')
        screen3.title("Return book")
        frame3 = Frame(screen3, width=500, height=400, bg='#fff')
        frame3.place(x=250, y=30)
        heading = Label(frame3, text="Return Book", fg='blue', bg='White', font=('Popins', 23, 'bold'))
        heading.place(x=175, y=5)
        Label(frame3, text="Book Name     ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=25, y=95)
        Label(frame3, text="Quantity ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=25, y=145)
        Label(frame3, text="Borrowed Date ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=25, y=195)
        Label(frame3, text="Returning Date ", font=('popins', 15, 'bold'), bg='#fff', fg='black').place(x=25, y=245)
        option1 = []
        try:
            global con, cursor
            con = db.connect(host="localhost", user="root", password='')
            cursor = con.cursor()
            q = 'use userinfo'
            cursor.execute(q)
        except Exception as e:
            print(e, 1)
            messagebox.showerror("Invalid", "Database connection failed")
            return
        q = 'select bookname from book'
        cursor.execute(q)
        row = cursor.fetchall()
        for k in row:
            option1.append(str(k[0]))
        global bor_date, bk_quntity
        global ret_date
        global bo_name
        bo_name = StringVar()
        bo_name.set('--select book--')
        bk_quntity = StringVar()
        bor_date = StringVar()
        ret_date = StringVar()
        b_name = OptionMenu(frame3, bo_name, *option1)
        b_name.configure(width=27, font=('popins', 12), bg='#d3d3d3')
        b_name.place(x=190, y=100)
        b_qua = Entry(frame3, width=27, font=('popins', 12), bg='#d3d3d3', textvariable=bk_quntity).place(x=190, y=150)
        b_date = DateEntry(frame3, selectmode='day', date_pattern="dd-MM-yyyy", width=25, font=('popins', 12),
                           bg='#d3d3d3', textvariable=bor_date).place(x=190, y=200)
        r_date = DateEntry(frame3, selectmode='day', date_pattern="dd-MM-yyyy", width=25, font=('popins', 12),
                           bg='#d3d3d3', textvariable=ret_date).place(x=190, y=250)

        sbmitbtn2 = Button(frame3, width=10, text="Submit", font=('popins', 15, 'bold'), bg="blue", fg="white",
                           command=self.ret).place(x=200, y=330)

        Button(screen3, text="Home", width=10, pady=6, fg='black', bg='orange', border=0,
               command=self.Entry_page3).place(x=15, y=25)
        screen3.mainloop()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page5(self):
        screen1.destroy()
        self.login()

    # --------------f-------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page1(self):
        root1.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page2(self):
        screen2.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page3(self):
        screen3.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page4(self):
        screen1.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def register1(self):
        root1.destroy()
        self.register()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def signin_1(self):
        root0.destroy()
        self.login()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page6(self):
        root3.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def Entry_page7(self):
        screen4.destroy()
        self.Entry_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def lib_login(self):
        root1.destroy()
        self.librarian_login_page()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def stu_login(self):
        root3.destroy()
        self.login()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_bo(self):
        b1 = bu1.get()
        a1 = au1.get()
        q1 = qu1.get()
        q1 = int(q1)
        try:
            global con, cursor
            con = db.connect(host="localhost", user="root", password='')
            cursor = con.cursor()
            q = 'use userinfo'
            cursor.execute(q)
        except Exception as e:
            print(e, 1)
            messagebox.showerror("Invalid", "Database connection failed")
            return
        try:
            q = 'insert into book(bookname,author,quantity) values(%s,%s,%s)'
            cursor.execute(q, (b1, a1, q1))
            messagebox.showinfo("Addbook", "{} book is sucessfully added".format(b1))
        except Exception as e:
            print(e, 1)
            messagebox.showerror("Error", "Can't insert book")
        con.commit()
        cursor.close()
        con.close()

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def ret(self):
        bname1 = bo_name.get()
        qua1 = bk_quntity.get()
        q1 = int(qua1)
        li = []
        q = 'select * from book'
        cursor.execute(q)
        row = cursor.fetchall()
        for i in row:
            li.append(list(i))
        for j in li:
            if j[0] == bname1:
                j[2] = j[2] + q1
                k = j[2]
                q = "update book set quantity=%s where bookname=%s"
                cursor.execute(q, (k, bname1))
                con.commit()
                cursor.close()
                con.close()
        bo_name.get()
        bor_date1 = bor_date.get()
        ret_date1 = ret_date.get()
        ret_d = datetime.strptime(ret_date1, "%d-%m-%Y")
        bor_d = datetime.strptime(bor_date1, "%d-%m-%Y")
        dif = (ret_d - bor_d).days
        if dif > 2:
            k = (dif - 2) * 20
        if dif <= 2:
            messagebox.showinfo("Fine", "Thank you for returning within time")
        else:
            messagebox.showerror("Fine", "You Need to pay fine amount Rs.{} for delay return".format(k))

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    def sel_bo(self):
        bk_name = var.get()
        au_name = author1.get()
        qua = quantity1.get()
        qua1 = int(qua)
        li = []
        q = 'select * from book'
        cursor.execute(q)
        row = cursor.fetchall()
        for i in row:
            li.append(list(i))
        for j in li:
            if j[0] == bk_name:
                if j[2] == 0:
                    messagebox.showerror("Try again", "Book is not available")
                elif j[2] < qua1:
                    messagebox.showerror("Try again",
                                         "Requirements exceed the limit only {} books are available".format(j[2]))
                else:
                    j[2] = j[2] - qua1
                    k = j[2]
                    q = "update book set quantity=%s where bookname=%s"
                    cursor.execute(q, (k, bk_name))
                    con.commit()
                    cursor.close()
                    con.close()
                    messagebox.showinfo("Info", "Book is Available Come and Get the Book")


o = library()

try:
    global con, cursor
    con = db.connect(host="localhost", user="root", password='')
    cursor = con.cursor()
    q = 'use userinfo'
    cursor.execute(q)
except Exception as e:
    print(e, 1)
    messagebox.showerror("Invalid", "Database connection failed")
try:
    q = 'create table book(bookname varchar(20),author varchar(20),quantity int,primary key(bookname))'
    cursor.execute(q)
except Exception as e:
    print(e, 'Table exists')
o.Entry_page()
