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

root.title("Admin Panel")
root.geometry("1920x1080")
#root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
# root.state('zoomed')
root.config(bg='white')


def exit_window(e):
    root.destroy()


label_title = Label(root, text="ADMIN PANEL", font=('Felix Titling', 30),bg='white')
label_title.place(x=615, y=30)


"""
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
"""
# account=Label(root,text='Already Have An Account?',font=('Montserrat',10),bg='white')
# account.place(x=570,y=580)



# question controls - - buttons

label_heading=Label(root,text='Question Controls',font=('Montserrat', 15),bg='white')
label_heading.place(x=1100,y=100)

button_AddQuestion = Button(root, text="Add Question",font=('Montserrat',12), command = "")
button_AddQuestion.place(x=1000, y=200, width=125, height=40)

button_DelQuestion = Button(root, text="Delete Question",font=('Montserrat',12), command = "")
button_DelQuestion.place(x=1270, y=200, width=155, height=40)

# user controls - buttons

label_heading=Label(root,text='User Controls',font=('Montserrat', 15),bg='white')
label_heading.place(x=200,y=100)

button_AddUser = Button(root, text="Add User",font=('Montserrat',12), command = "")
button_AddUser.place(x=100, y=200, width=100, height=40)

button_DelUser = Button(root, text="Delete User",font=('Montserrat',12), command = "")
button_DelUser.place(x=330, y=200, width=110, height=40)




# loginbt=Button(root,text='Log in',font=('Montserrat',14),fg='blue',bd=0,cursor='hand',bg='white',command="")
# loginbt.place(x=730,y=575,width=100,height=25)



"""
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
            messagebox.showinfo("Error", "ALL Fields Are Mandatory!!!")
        
        elif len(data)!= 0:
            messagebox.showinfo("Exists", "user already exists!!!")
    
        elif pw1 != cpw:
            messagebox.showinfo("Invalid ", "Both Password Should Match")
        else:
            inst='INSERT INTO USERS VALUES (%s,%s,%s)'
            val=(name,em,pw1)
            mycursor.execute(inst,val)
            mydb.commit()
            messagebox.showinfo("Success", "Successfully added")
            login_page()

    frame=Frame(root,bg='white')
    frame.place(x=560,y=90,width=430, height=520)


# ------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------------------------- #

def login_page():
    root.title("Log in page")
    def verify_login():
        mycursor.execute(f"SELECT * FROM USERS WHERE (USRNM = '{username.get()}' OR EMAIL = '{username.get()}') AND PSWD = '{pw.get()}'")
        if len(mycursor.fetchall()) > 0:
            messagebox.showinfo("Success", "Login Successful")
        else:
            messagebox.showinfo("Invalid", "Invalid Username OR Password")

########################################## LOG IN THINGS ##################################################

    frame=Frame(root,bg='white')
    frame.place(x=560,y=90,width=430, height=520)

    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50), bg='white') # title added
    label_title.place(x=615, y=100)
    label_title = Label(root, text="Log in\nto continue to Quiz App", font=('Montserrat', 12), bg='white') # title added
    label_title.place(x=690, y=192)
    # label_title = Label(root, text="Log in\nto continue to Quiz App", font=('Montserrat', 20), bg='white') # title added
    # label_title.place(x=712, y=190)

    label_username = Label(root, text="Username/Email", font=('Montserrat', 15), bg='white')
    label_username.place(x=620, y=310)
    username = Entry(root, bg='white',font=('Montserrat',13))
    username.place(x=625, y=350, width=300, height=30)

    #label_email = Label(root, text="Email", font=('Montserrat', 15), bg='white')
    #label_email.place(x=620, y=355)
    #email = Entry(root, bg='white',font=('Montserrat',13))
    #email.place(x=750, y=355, width=180, height=30)y=y+40

    label_pw = Label(root, text="Password", font=('Montserrat', 15), bg='white')
    label_pw.place(x=620, y=395)
    pw = Entry(root, bg='white', show='*',font=('Montserrat',13)) ## ADD OPTIONAL PASSWORD VIEW
    pw.place(x=625, y=435, width=300, height=30)

    label_new_user = Label(root, text="New player? ", font=('Montserrat', 15), bg='white')
    label_new_user.place(x=660, y=570)

########################################## BUTTON THINGS ##################################################

    button_login = Button(root, text="Log in", font=('Montserrat', 14,'bold'), command=verify_login)
    button_login.place(x=705, y=485, width=150, height=40)

    button_register = Button(root, text="Register here", font=('Montserrat', 12), bg='white', command=register_page)
    button_register.place(x=800, y=570, width=125, height=35)
    
    
    """

root.bind('<Escape>', exit_window)
root.mainloop()