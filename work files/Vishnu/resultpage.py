import tkinter as tk
from tkinter import *


root=Tk()
root.geometry('1920x1080')
root.config(bg='white')
root.title('Result')
rslt=Label(text='Result Of Software Quiz',font=('Montserrat',20,UNDERLINE,'bold'),bg='white')
rslt.place(relx=0.5,rely=0.1,anchor=CENTER)

usr=Label(text='Username:<username>',font=('Montserrat',16),bg='white')
usr.place(relx=0.32,rely=0.19)

tme=Label(text='Time Taken:<time_taken>',font=('Montserrat',16),bg='white')
tme.place(relx=0.53,rely=0.19)

dtl=Label(text='Detailed Report',font=('Montserrat',16,UNDERLINE),bg='white')
dtl.place(relx=0.32,rely=0.3)

totqn=Label(text='Total Questions Attended:',font=('Montserrat',16),bg='white')
totqn.place(relx=0.32,rely=0.37)

crtans=Label(text='Correctly Answered:',font=('Montserrat',16),bg='white')
crtans.place(relx=0.32,rely=0.41)

wrngans=Label(text='Wrongly Answered:',font=('Montserrat',16),bg='white')
wrngans.place(relx=0.32,rely=0.45)

lgot=Button(root,text='Log Out',font=('Montserrat', 15))
lgot.place(relx=0.22,rely=0.6,width=150,height=50)

cnt=Button(root,text='Continue',font=('Montserrat', 15))
cnt.place(relx=0.68,rely=0.6,width=150,height=50)


root.mainloop()