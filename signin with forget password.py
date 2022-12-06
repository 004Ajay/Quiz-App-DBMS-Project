import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import mysql.connector

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()
root.geometry("1920x1080")
"""
# can use this as final
# it will autmtcly gets screen size and will zoom the window to dim of screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}") # "1920x1080"
root.state('zoomed')
"""

#################  ICONS & IMAGES   ######################
root.iconbitmap("Q.ico") # app icon (top left corner)
pw_show = ImageTk.PhotoImage(file="show_pw.png") # to show/hide password
#bg1=ImageTk.PhotoImage(file=r"D:/t.jpg")  # change path of image as in your system
#bg_lbl=Label(root,image=bg1).place(x=0, y=-0, relwidth=1, relheight=1)

############   Password Show/Hide   ##########################

def pswdshow(spwd,a,b):
    def show(): spwd.config(show="") # for showing pswd of pswd in login page
    def hide(): spwd.config(show="*") # for hiding pswd of pswd in login page
    pw_ShowBtn = Button(root, image=pw_show, bd=0, bg="white")
    pw_ShowBtn.place(x=a, y=b, width=35, height=25)
    pw_ShowBtn.bind("<ButtonPress>", lambda event:show())
    pw_ShowBtn.bind("<ButtonRelease>", lambda event:hide())

def exit_window(e):
    root.destroy() # to exit window

#################   SIGN_UP PAGE   ############################

def register_page():
    root.title("Signup Page")
     

    def sign_up():
        name=new_name.get()
        pw1=new_pw.get()
        cpw=new_cpw.get()
        em=new_mail.get()
        mycursor.execute(f"SELECT * FROM USERS WHERE USRNM = '{name}' OR EMAIL= '{em}'")
        data=mycursor.fetchall()
        if em=="" or name=="" or pw1=="" or cpw=="":
            messagebox.showinfo("Add all info", "All fields are mandatory")
        elif len(data)!= 0:
            messagebox.showinfo("Player exist", "Player already exist")
        elif pw1 != cpw:
            messagebox.showinfo("Password Error", "Passwords doesn't match")
        else:
            inst='INSERT INTO USERS VALUES (%s,%s,%s)'
            val=(name,em,pw1)
            mycursor.execute(inst,val)
            mydb.commit()
            messagebox.showinfo("Success", "Player successfully added")
            login_page()
    
    frame=Frame(root,bg='white')
    frame.place(x=565,y=90,width=430, height=520)

    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50),bg='white')
    label_title.place(x=615, y=100)

    label_heading=Label(root,text='Create An Account',font=('Montserrat', 20),bg='white')
    label_heading.place(x=660,y=200)

    label_mail = Label(root, text="E-mail",font=('Montserrat',15),bg='white')
    label_mail.place(x=585, y=300)
    new_mail = Entry(root,font=('Montserrat',11),bg='white')
    new_mail.place(x=780, y=300, width=180, height=30)

    label_name = Label(root, text="Username",font=('Montserrat',15),bg='white')
    label_name.place(x=585, y=340)
    new_name = Entry(root,font=('Montserrat',11),bg='white')
    new_name.place(x=780, y=340, width=180, height=30)

    label_pw = Label(root, text="New Password",font=('Montserrat',15),bg='white')
    label_pw.place(x=585, y=380)
    new_pw = Entry(root, show='*',font=('Montserrat',13),bg='white')
    new_pw.place(x=780, y=380, width=180, height=30)
    pswdshow(new_pw,960,383)

    label_confirm_pw = Label(root, text="Confirm Password",font=('Montserrat',15),bg='white')
    label_confirm_pw.place(x=585, y=420)
    new_cpw = Entry(root, show='*',font=('Montserrat',13),bg='white')
    new_cpw.place(x=780, y=420, width=180, height=30)
    pswdshow(new_cpw,960,423)

    button_signup = Button(root, text="Sign Up",font=('Montserrat',17), command = sign_up)
    button_signup.place(x=676, y=480, width=200, height=50)

    account=Label(root,text='Already have an account?',font=('Montserrat',10),bg='white')
    account.place(x=655,y=575)

    loginbt=Button(root,text='Log in',font=('Montserrat',11, UNDERLINE),fg='blue',bd=0,cursor='hand2',bg='white',command=login_page)
    loginbt.place(x=830,y=568) # ,width=100,height=25)

#################   LOGIN_PAGE   ############################

def login_page():
    root.title("Log in page")
    def frgtpwd():
        root2=Toplevel()
        root2.title("Forget Password")
        root2.geometry("300x400+400+200")
        root2.focus_force()
        root2.grab_set()


        def urotp():
            mydb = mysql.connector.connect( # connecting to database
            host="localhost",user="root",passwd="1234",database="project",auth_plugin='mysql_native_password')
            mycursor = mydb.cursor()

            mycursor.execute(f"SELECT * FROM users WHERE (email = '{emailentry.get()}' AND usrnm= '{userentry.get()}')")
            if emailentry.get()==""or userentry.get()==""or newpwentry.get==""or newcpwentry.get()=="":
                messagebox.showinfo("Add all info", "All fields are mandatory")
            elif len(mycursor.fetchall())<1:
                messagebox.showinfo("invalid", "Invalid Email or Username ")
            elif newpwentry.get() != newcpwentry.get():
                messagebox.showinfo("Password Error", "Passwords doesn't match")
            else:
                query='update users set pswd=%s where email=%s'
                mycursor.execute(query,(newcpwentry.get(),emailentry.get()))
                mydb.commit()
                root2.destroy()
                messagebox.showinfo("Success", "successfully changed password")
                


        frame=Frame(root2,bg='white')
        frame.place(x=20,y=40,width=260, height=340)


        title1=Label(root2,text="RESET PASSWORD",font=("Montserrat",17,'bold'),bg="white")
        title1.place(x=45,y=50)

        emaillabel=Label(root2,text="Enter Email",font=("Montserrat",13),bg='white')
        emaillabel.place(x=25,y=120)
        emailentry=Entry(root2, bg='white',font=('Montserrat',13))
        emailentry.place(x=30,y=150,width=240,height=25)

        userlabel=Label(root2,text="Enter Username",font=("Montserrat",13),bg='white')
        userlabel.place(x=25,y=175)
        userentry=Entry(root2, bg='white',font=('Montserrat',13))
        userentry.place(x=30,y=200,width=240,height=25)

        newpwlabel=Label(root2,text="New Password",font=("Montserrat",13),bg='white')
        newpwlabel.place(x=25,y=225)
        newpwentry=Entry(root2, bg='white',font=('Montserrat',13))
        newpwentry.place(x=30,y=250,width=240,height=25)

        newcpwlabel=Label(root2,text="Confirm Password",font=("Montserrat",13),bg='white')
        newcpwlabel.place(x=25,y=275)
        newcpwentry=Entry(root2, bg='white',font=('Montserrat',13))
        newcpwentry.place(x=30,y=300,width=240,height=25)

        nextbtn=Button(root2,text="NEXT",font=('Montserrat'),bg="white",command=urotp)
        nextbtn.place(x=100,y=335)


    def verify_login():
        mycursor.execute(f"SELECT * FROM USERS WHERE (USRNM = '{usrnm_email.get()}' OR EMAIL = '{usrnm_email.get()}') AND PSWD = '{pw.get()}'")
        if len(mycursor.fetchall()) > 0:
            messagebox.showinfo("Success", "Login Successful") # should be changed to check, then proceed to current acc
        else:
            messagebox.showinfo("Info Error", "Invalid username or password")

    frame=Frame(root,bg='white')
    frame.place(x=565,y=95,width=430, height=520)

    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50), bg='white')
    label_title.place(x=615, y=100)
    label_title = Label(root, text="Log in\nto continue to Quiz App", font=('Montserrat', 12), bg='white')
    label_title.place(x=690, y=192)

    label_usrnm_email = Label(root, text="Username/Email", font=('Montserrat', 15), bg='white')
    label_usrnm_email.place(x=620, y=310)
    usrnm_email = Entry(root, bg='white',font=('Montserrat',13))
    usrnm_email.place(x=625, y=350, width=300, height=30)

    label_pw = Label(root, text="Password", font=('Montserrat', 15), bg='white')
    label_pw.place(x=620, y=395)
    
    pw = Entry(root, bg='white', show='*',font=('Montserrat',13)) ## ADD OPTIONAL PASSWORD VIEW
    pw.place(x=625, y=435, width=300, height=30)
    pswdshow(pw,930,435)


    button_login = Button(root, text="Log in", font=('Montserrat', 14), command=verify_login)
    button_login.place(x=703, y=486, width=150, height=40)

    label_new_user = Label(root, text="New player? ", font=('Montserrat', 12), bg='white')
    label_new_user.place(x=675, y=570)

    register_button = Button(root,text="Register here",font=('Montserrat',11,UNDERLINE)\
                      ,fg='blue',bd=0,cursor='hand2',bg='white',command=register_page) # bd is border
    register_button.place(x=777, y=567, width=125, height=35)
    frgt_button = Button(root,text="forgot password??",font=('Montserrat',11,UNDERLINE),fg='blue',bd=0,cursor='hand2',bg='white',command=frgtpwd) # bd is border
    frgt_button.place(x=625, y=457, width=125, height=35)#x=777


    
root.bind('<Escape>', exit_window)
login_page()
root.mainloop()