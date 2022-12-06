import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()

# root.geometry("500x500")
root.geometry("1920x1080")
#root.configure(bg='bisque')
bg1=ImageTk.PhotoImage(file=r"D:/t.jpg")

bg_lbl=Label(root,image=bg1)
bg_lbl.place(x=0,y=-0,relwidth=1,relheight=1)

def register_page():
    root.title("Signup Page")
    def validations():
        name=new_name.get()
        pw1=new_pw.get()
        cpw=new_cpw.get()
        em=new_mail.get()
        if em=="":
            messagebox.showinfo("Mandatory", "Enter Your EMAIL!!")
        elif name=="":
            messagebox.showinfo("Mandatory", "Enter Your Username")
        elif pw1=="":
            messagebox.showinfo("Mandatory", "Enter Your Password!!")
        elif cpw=="":
            messagebox.showinfo("Mandatory", "Confirm Your Password!!")
        else:
            sign_up(name,em,pw1,cpw)



    def sign_up(name,em,pw1,cpw):
    
    
        mycursor.execute(f"SELECT * FROM users WHERE USRNM = '{name}' OR EMAIL= '{em}'")
        data=mycursor.fetchall()
        if len(data)!= 0:
            messagebox.showinfo("Exists", "user already exists!!!")
    
        elif pw1 != cpw:
            messagebox.showinfo("Invalid ", "Both Password Should Match")
        else:
            inst='INSERT INTO users VALUES (%s,%s,%s)'
            val=(name,em,pw1)
            mycursor.execute(inst,val)
            mydb.commit()
            messagebox.showinfo("Success", "Successfully added")
            login_page()
    






    frame=Frame(root,bg='white')
    frame.place(x=560,y=90,width=430, height=520)


    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50),bg='white')
    label_title.place(x=615, y=100)

    label_heading=Label(root,text='Create An Account',font=('Montserrat', 20),bg='white')
    label_heading.place(x=660,y=200)

    label_mail = Label(root, text="E-mail",font=('Montserrat',15),bg='white')
    label_mail.place(x=585, y=300)
    new_mail = Entry(root,font=('Montserrat',13),bg='white')
    new_mail.place(x=780, y=300, width=180, height=30)

    label_name = Label(root, text="Userame",font=('Montserrat',15),bg='white')
    label_name.place(x=585, y=340)
    new_name = Entry(root,font=('Montserrat',13),bg='white')
    new_name.place(x=780, y=340, width=180, height=30)

    label_pw = Label(root, text="New Password",font=('Montserrat',15),bg='white')
    label_pw.place(x=585, y=380)
    new_pw = Entry(root, show='*',font=('Montserrat',13),bg='white')
    new_pw.place(x=780, y=380, width=180, height=30)

    label_confirm_pw = Label(root, text="Confirm Password",font=('Montserrat',15),bg='white')
    label_confirm_pw.place(x=585, y=420)
    new_cpw = Entry(root, show='*',font=('Montserrat',13),bg='white')
    new_cpw.place(x=780, y=420, width=180, height=30)

    account=Label(root,text='Already Have An Account?',font=('Montserrat',10),bg='white')
    account.place(x=570,y=580)

    
    button_signup = Button(root, text="Sign Up",font=('Montserrat',17,'bold'), command = validations)
    button_signup.place(x=676, y=480, width=200, height=50)

    loginbt=Button(root,text='Log in',font=('Montserrat',14),fg='blue',bd=0,cursor='hand2',bg='white',command=login_page)
    loginbt.place(x=730,y=575,width=100,height=25)




def login_page():
    root.title("Log in page")
    def verify_login():
        mycursor.execute(f"SELECT * FROM users WHERE (USRNM = '{username.get()}' OR EMAIL = '{email.get()}') AND PSWD = '{pw.get()}'")
        if len(mycursor.fetchall()) > 0:
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showinfo("Failed", "Login Failed")

########################################## LOG IN THINGS ##################################################

    frame=Frame(root,bg='white')
    frame.place(x=560,y=90,width=430, height=520)

    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50), bg='white') # title added
    label_title.place(x=615, y=100)
    label_title = Label(root, text="Log in page", font=('Montserrat', 20), bg='white') # title added
    label_title.place(x=712, y=190)

    label_username = Label(root, text="Username", font=('Montserrat', 15), bg='white')
    label_username.place(x=620, y=310)
    username = Entry(root, bg='white',font=('Montserrat',13))
    username.place(x=750, y=315, width=180, height=30)

    label_email = Label(root, text="Email", font=('Montserrat', 15), bg='white')
    label_email.place(x=620, y=355)
    email = Entry(root, bg='white',font=('Montserrat',13))
    email.place(x=750, y=355, width=180, height=30)

    label_pw = Label(root, text="Password", font=('Montserrat', 15), bg='white')
    label_pw.place(x=620, y=395)
    pw = Entry(root, bg='white', show='*',font=('Montserrat',13)) ## ADD OPTIONAL PASSWORD VIEW
    pw.place(x=750, y=395, width=180, height=30)

    label_new_user = Label(root, text="New player? ", font=('Montserrat', 15), bg='white')
    label_new_user.place(x=660, y=570)

########################################## BUTTON THINGS ##################################################

    button_login = Button(root, text="Log in", font=('Montserrat', 14,'bold'), command=verify_login)
    button_login.place(x=703, y=445, width=150, height=40)

    button_register = Button(root, text="Register here", font=('Montserrat', 12), command=register_page)
    button_register.place(x=800, y=570, width=125, height=35)

login_page()

root.mainloop()