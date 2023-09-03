from tkinter import *
# Tkinter
root = Tk()
root.title("Book Bank System Online")
root.geometry("925x500+300+200")
root.resizable(False, False)
root.minsize(925, 500)
root.maxsize(1366, 768)
root.configure(bg='#fff')
# Image
img = PhotoImage(file="/Users/mahendran/Downloads/UML/Entry.png")
bg_img = Label(root, image=img, bg="white")
bg_img.place(x=50, y=50)
# Frame for Buttons
frame = Frame(root, width=370, height=370, bg='white')
frame.place(x=480, y=70)
# Title Label
heading = Label(frame, text="Book Bank System", fg='blue', bg='White', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=90, y=3)
# Buttons
btn1 = Button(frame, text="Login/Register", bg='#000000', fg='black', border=0, highlightthickness=0)
btn1.place(relx=0.38, rely=0.2, relwidth=0.35, relheight=0.11)
btn2 = Button(frame, text="Select Book", bg='black', fg='black', border=0, highlightthickness=0)
btn2.place(relx=0.38, rely=0.35, relwidth=0.35, relheight=0.11)
btn3 = Button(frame, text="Return Book", bg='black', fg='black', border=0, highlightthickness=0)
btn3.place(relx=0.38, rely=0.50, relwidth=0.35, relheight=0.11)
btn4 = Button(frame, text="Exit", bg='black', fg='black', command=root.destroy, border=0, highlightthickness=0)
btn4.place(relx=0.38, rely=0.65, relwidth=0.35, relheight=0.11)
root.mainloop()
