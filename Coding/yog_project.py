from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector



def admin():
    messagebox.showinfo("ADMIN", "ADD ADMIN PAGE")

# Gets the "radio" value and returns a string.


def selection():
    gender = ""
    selected = int(radio.get())
    if selected == 1:
        gender = "male"
    elif selected == 2:
        gender = "female"
    else:
        gender = "others"
    return gender

def selection():
    availablecourse=""
    selected=int(radio.get())
    if selected==1:
        availablecourse="c"
    elif selected ==2:
        availablecourse="c++"
    else:
        availablecourse="python"
    return availablecourse




def existing_user():
    top = Toplevel()
    top.title('Login')
    top.geometry("600x300")

    head = Label(top,
                 text='SIGNIN',
                 font=('bold', 15))
    head.place(relx=0.5, rely=0.2, anchor=CENTER)

    b_name = Label(top,
                   text='GMAIL',
                   font=('bold', 15))
    # anchor=W indicates WEST Direction.
    b_name.place(relx=0.1, rely=0.4, anchor=W)
   

    global login_name
    login_name = Entry(top)
    # anchor=E indicates EAST Direction.
    login_name.place(relx=0.9, rely=0.4, anchor=E)
    login_name.config(width=30)

    b_auth = Label(top,
                   text='PASSWORD',
                   font=('bold', 15))
    b_auth.place(relx=0.1, rely=0.6, anchor=W)

    global login_password
    login_password = Entry(top, show="*")
    login_password.place(relx=0.9, rely=0.6, anchor=E)
    login_password.config(width=30)

    bname = Button(top,
                   text="SUBMIT",
                   font=("bold", 10), bg="blue",
                   command=login)   # Triggers the "login" function.
    bname.place(relx=0.2, rely=0.8, anchor=W)
    bname.config(height=1, width=10)

    bauth = Button(top,
                   text="CANCEL",
                   font=("bold", 10), bg="red",
                   command=top.destroy)  # Window is destroyed.
    bauth.place(relx=0.8, rely=0.8, anchor=E)
    bauth.config(height=1, width=10)


def detail_view():
    top = Toplevel()
    top.title('Detail View')
    top.geometry('800x400')

   
    data = get_from_db()



    tv = ttk.Treeview(top)

    # create a column
    tv['columns'] = ("NAME", "AGE", "DoB",  "GENDER",
                     "FATHER'S NAME", "QUALIFICATION", "ADDRESS")

    # Add the column
    tv.column("#0", width=0)  # --> This is a default empty column
    tv.column("NAME", anchor=W)
    tv.column("AGE", anchor=W)
    tv.column("DoB", anchor=W)
    tv.column("AVAILABLE COURSE",anchor=W)
    tv.column("GENDER", anchor=W)
    tv.column("FATHER'S NAME", anchor=W)
    tv.column("QUALIFICATION", anchor=W)
    tv.column("ADDRESS", anchor=W)

    # Add the Headings
    tv.heading("#0")  # --> Again this is a default column
    tv.heading("NAME", text="NAME", anchor=W)
    tv.heading("AGE", text='AGE', anchor=W)
    tv.heading("DoB", text='DoB', anchor=W)
    tv.heading("AVAILABLE COURSE",text='AVAILABLE COURSES',anchor=W)
    tv.heading("FATHER'S NAME", text="FATHER'S NAME", anchor=W)
    tv.heading("QUALIFICATION", text="QUALIFICATION", anchor=W)
    tv.heading("ADDRESS", text='ADDRESS', anchor=W)

    # It makes the "data" list as a iterator like ((0, [1,2,3,4]), (1, [5,6,7,8]))
    for i, row in enumerate(data):
        tv.insert(parent='', index='end', iid=i, values=(
            row[1], row[2], row[3], row[4], row[5], row[6],row[7]))

    # we pack all the widgets to the Table
    tv.pack()

    paymentBtn = Button(top,
                        text="PAYMENT", font=("bold", 10), bg="yellow",
                        command=payment)
    paymentBtn.place(x=200, y=300)
    exitBtn = Button(top, text="RESET", font=(
        "bold", 10), bg="red", command=del_db)
    exitBtn.place(x=400, y=300)



# Button "bname" triggers this Function "new_user"


def new_user():
    def register():
        pass

   
    top = Toplevel()
    top.title('Registration')
    top.geometry("500x500")
    global radio,radio1

    radio = IntVar()
    radio1 = IntVar()
    frame1 = Frame(top, bg='white')

    frame1.place(relx=0, rely=0, width=500, height=500)


   
    registerTitle = Label(frame1,
                          # Specifys the text to de displayed in the Label "registerTitle".
                          text="REGISTRATION",
                          # Specifys the font, text size, background and font color.
                          font=("bold", 15), bg="white", fg="black")
    # It anchors the widget "id" to the CENTER and Specifys the position of label relative to the x and y axis.
    registerTitle.place(relx=0.5, rely=0.03, anchor=CENTER)

    # --> Name Label and Field

    # This Global Variable is used such that all the functions can access this variable.
    global nameField
    nameLabel = Label(frame1,
                      text="Name:",
                      font=("Helvetica", 13), bg="white", fg="gray")
    nameLabel.place(x=20, y=70)
    nameField = Entry(frame1, font=("Helvetica", 13), bg="white")
    nameField.place(x=150, y=70, width=250)

    # --> Age Label and Age Field
    global ageField
    ageLabel = Label(frame1,
                     text="Age:",
                     font=("Helvetica", 13), bg="white", fg="gray")
    ageLabel.place(x=20, y=110)

    ageField = Entry(frame1,
                     font=("Helvetica", 13), bg='white')
    ageField.place(x=150, y=110, width=250)

    # --> DoB Label and Field
    global dobField
    dobLabel = Label(frame1,
                     text="Date of Birth:",
                     font=("Helvetica", 13), bg="white", fg="gray")
    dobLabel.place(x=20, y=150)

    dobField = Entry(frame1,
                     font=("Helvetica", 13), bg='white')
    dobField.place(x=150, y=150, width=250)
#new
    availablecourseLabel=Label(frame1,
                           text="Available Course:",
                           font=("Helvetica",13),bg="white",fg="gray").place(x=20,y=190)
    cField=Radiobutton(frame1,
                   text="c",
                   variable=radio,
                   value=1,
                   command=selection,
                   bg='white').place(x=150,y=190)
    cField=Radiobutton(frame1,
                   text="c++",
                   variable=radio,
                   value=2,
                   command=selection,
                   bg='white').place(x=220,y=190)
    pythonField=Radiobutton(frame1,
                   text="python",
                   variable=radio,
                   value=3,
                   command=selection,
                   bg='white').place(x=290,y=190)
                       
   
    # --> Gender Label and Field
    genderLabel = Label(frame1,
                        text="Gender:",
                        font=("Helvetica", 13), bg="white", fg="gray").place(x=20, y=230)

    maleField = Radiobutton(frame1,
                            text="Male",
                            variable=radio1,
                            value=1,
                            command=selection,
                            bg='white').place(x=150, y=230)

    femaleField = Radiobutton(frame1,
                              text="Female",
                              variable=radio1,
                              value=2,
                              command=selection,
                              bg='white').place(x=220, y=230)

    otherField = Radiobutton(frame1,
                             text="Others",
                             variable=radio1,
                             value=3,
                             command=selection,
                             bg='white').place(x=290, y=230)

    # --> Father's name Label and Field
    global fatherField
    fatherLabel = Label(frame1,
                        text="Father's Name:",
                        font=("Helvetica", 13), bg="white", fg="gray").place(x=20, y=270)
    fatherField = Entry(frame1,
                        font=("Helvetica", 13), bg='white')
    fatherField.place(x=150, y=270, width=250)


    global qualificationField
    motherLabel = Label(frame1,
                        text="Qualification:", font=("Helvetica", 13), bg="white", fg="gray").place(x=20, y=310)

    qualificationField = Entry(frame1,
                        font=("Helvetica", 13), bg='white')
    qualificationField.place(x=150, y=310, width=250)

    # --> address Label and Age Field
    global addrField
    addrLabel = Label(frame1,
                      text="Address:", font=("Helvetica", 13), bg="white", fg="gray").place(x=20, y=350)

    addrField = Entry(frame1,
                      font=("Helvetica", 13), bg='white')
    addrField.place(x=150, y=350, width=250)

    # T&C
    tandc = Checkbutton(frame1,
                        text="I Agree to the Terms & Conditions", bg='white', font=("Times", 12),
                        onvalue=1,
                        offvalue=0).place(x=20, y=390)

    # Register
    registerBtn = Button(frame1,
                         text='Register',
                         font=('Helvetica', 13), padx=15, pady=5,
                         # This just changes the mouse pointer to a hand icon.
                         cursor="hand2",
                         # It Triggers the function "register" on click.
                         command=register
                         ).place(x=20, y=430)

    cancelBtn = Button(frame1,
                       text='Cancel',
                       font=('Helvetica', 13), padx=15, pady=5,
                       cursor="hand2",
                       # It simply destroys the window (or) closes it.
                       command=top.destroy
                       ).place(x=200, y=430)


# Button "a" triggers this Function "continue_window"
def continue_window():
    # Instantiates a child window and assigns to the variable "top".
    top = Toplevel()
    # This specifys the title of the child window using the object "top".
    top.title('YSY ACADEMY')
    # This specifys the dimensions of the child window using the object "top".
    top.geometry("600x300")
    # We are creating a Label widget to display text and assigning to the variable "head".

    # --> We specify "top" to position the widget in the "top" window.
    head = Label(top,
                 # Specifys the text to de displayed in the Label "head".
                 text='ENROLLMENT OPEN',
                 font=('bold', 15))     # Specifys the font and the text size.
    # It anchors the widget "id" to the CENTER and Specifys the position of label relative to the x and y axis.
    head.place(relx=0.5, rely=0.2, anchor=CENTER)
    # Creates a Button Widget and Assigns it to a variable "bname"

    # --> We specify "top" to position the widget in the "top" window
    bname = Button(top,
                   # Specifys the text to de displayed in the Button.
                   text="LOG IN AS A STUDENT",
                   # Specifys the font and the text size.
                   font=("bold", 10), bg="white",
                   # Triggers the function "new_user" on button click.
                   command=new_user,
                   # Adds some Padding to x (padx) and y (pady) directions.
                   padx=15, pady=10)
    # Specifys the position of Button relative to the x and y axis.
    bname.place(relx=0.1, rely=0.4,)
    # Specifys the dimension of the button "bname"
    bname.config(height=1, width=20)

    # Creates a Button Widget and Assigns it to a variable "bauth"

    # --> We specify "top" to position the widget in the "top" window
    bauth = Button(top,
                   # Specifys the text to de displayed in the Button.
                   text="LOG IN AS A TEACHER",
                   # Specifys the font and the text size.
                   font=("bold", 10), bg="white",
                   # Triggers the function "existing_user" on button click
                   command=existing_user,
                   # Adds some Padding to x (padx) and y (pady) directions.
                   padx=15, pady=10)
    # Specifys the position of Button relative to the x and y axis.
    bauth.place(relx=0.5, rely=0.5)
    # Specifys the dimension of the button "bauth"
    bauth.config(height=1, width=20)

    # Creates a Button Widget and Assigns it to a variable "adminBtn"

   


# =============================== Main ================================= #

# --> MAIN PROGRAM STARTS HERE.
def main():
    # This instantiates an object of Tk() class to create the base window.
    root = Tk()
    # This specifys the dimensions of theh base window using the object root.
    root.geometry("600x300")
    # This specifys the title of the base window using the object root.
    root.title("COURSE RESERVATION ")

    # We are creating a Label widget to display text and assigning to the variable "id".

    # --> We specify "root" to position the widget in the "root" window
    id = Label(root,
               # Specifys the text to de displayed in the Label.
               text='COURSE ENROLLMENT',
               font=('bold', 15))                                 # Specifys the font and the text size.
    # It anchors the widget "id" to the CENTER and Specifys the position of label relative to the x and y axis.
    id.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Creates a Button Widget and Assigns it to a variable "a"

    # --> We specify "root" to position the widget in the "root" window
    a = Button(root,
               # Specifys the text to de displayed in the Button.
               text="LOGIN",
               # Specifys the font and the text size.
               font=("bold", 10), bg="white",
               command=continue_window)                           # Triggers the function "continue_window" on button click.
    # It anchors the widget "a" to the CENTER and Specifys the position of Button relative to the x and y axis.
    a.place(relx=0.5, rely=0.4, anchor=CENTER)
    # Specifys the dimension of the button "a"
    a.config(height=1, width=15)

    # Creates a Button Widget and Assigns it to a variable "b"

    # --> We specify "root" to position the widget in the "root" window
    b = Button(root,
                   # Specifys the text to de displayed in the Button.
               text="CANCEL",
               # Specifys the font and the text size.
               font=("bold", 10), bg="white",
               # Terminates / Closes the window on click.
               command=root.destroy)

    # It anchors the widget "b" to the CENTER and Specifys the position of Button relative to the x and y axis.
    b.place(relx=0.5, rely=0.6, anchor=CENTER)
    # Specifys the dimension of the button "b"
    b.config(height=1, width=10)


   
       

    # Keeps the Window Running.
    mainloop()










if __name__ == '__main__':
    main()
