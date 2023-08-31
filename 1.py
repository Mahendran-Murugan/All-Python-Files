from tkinter import *
import PIL 
global root0
root0 = Tk()
root0.title("Dummy for testing")
root0.geometry("925x500+200+100")
root0.resizable(False, False)
#root0.minsize(925, 500)
#root0.maxsize(1366, 768)
root0.configure(bg='#fff')
img= Image.open()
resized_image= img.resize((300,205), Image.ANTIALIAS)
Label1=Label(root0,image=resized_image)
Label1.pack()
root0.mainloop()