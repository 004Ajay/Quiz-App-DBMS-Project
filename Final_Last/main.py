# CURRENT STARTING FILE

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
from pswdShowHide import pswd_show # show/hide password
from forgot_pswd import * # from forgot password file
from db_connect import project_db # for accessing 'our project database'
from welcome_page import * # moving to welcome page
from admin import admin_panel

mydb = project_db()
mycursor = mydb.cursor(buffered=True)
"""
A buffered cursor stores the result set in the client's memory after executing a SELECT statement.
This can be more memory efficient than a non-buffered cursor, which stores the entire result set on the server
and retrieves it row by row as needed.
"""

root = Tk()
# root.geometry("1920x1080")

# can use this as final
# it will autmtcly gets screen size and will zoom the window to dim of screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}") # "1920x1080"
root.state('zoomed')


#################  KEYBOARD SHORTCUTS   ######################

def exit_window(e): root.destroy() # to exit window

#################  ICONS & IMAGES   ######################

root.iconbitmap("images/Q.ico") # app icon (top left corner)
eye_img = ImageTk.PhotoImage(master = root, file="images/show_pw.png") # to show/hide password
bg1=ImageTk.PhotoImage(master = root, file="images/main_bg.jpg")  # change path of image as in your system 
bg_lbl=Label(root, image=bg1).place(x=0, y=-0, relwidth=1, relheight=1)

#################   SIGN_UP PAGE   ############################
def framedes():
    global frame2
    login_page()

def register_page():
    global frame,frame2
    root.title("Signup Page")

    def signup_btn_shortkey(event): sign_up()
    def login_link_shortkey(event): login_page()
    frame.destroy()

    def sign_up():

        name=new_name.get()
        pw1=new_pw.get()
        cpw=new_cpw.get()
        em=new_mail.get()
        
        mycursor.execute(f"SELECT * FROM PLAYERS WHERE USERNAME = '{name}' OR EMAIL= '{em}'")
        if em=="" or name=="" or pw1=="" or cpw=="":
            mb.showinfo("Add all info", "All fields are mandatory")
        elif len(mycursor.fetchall())!= 0:
            mb.showinfo("Player exist", "Player already exist")
        elif pw1 != cpw:
            mb.showinfo("Password Error", "Passwords doesn't match")
        else:
            mycursor.execute(f"INSERT INTO PLAYERS VALUES ('{name}','{em}','{pw1}')")
            mydb.commit()
            mb.showinfo("Success", "Player successfully added")
            login_page() # redirects to login page after successful sign up
    
    frame2=Frame(root,bg='white')
    frame2.place(relx=.5,rely=.45,anchor=CENTER,width=430, height=520)

    label_title = Label(frame2, text="QUIZ APP", font=('Montserrat', 50),bg='white')
    label_title.place(relx=.5, rely=.1,anchor=CENTER)

    label_heading=Label(frame2,text='Create An Account',font=('Montserrat', 20),bg='white')
    label_heading.place(relx=.5,rely=.25,anchor=CENTER)

    label_mail = Label(frame2, text="E-mail",font=('Montserrat',15),bg='white')
    label_mail.place(relx=.05,rely=.4)
    new_mail = Entry(frame2,font=('Montserrat',11),bg='white')
    new_mail.place(relx=.5,rely=.4, width=180, height=30)

    label_name = Label(frame2, text="Username",font=('Montserrat',15),bg='white')
    label_name.place(relx=.05, rely=.48)
    new_name = Entry(frame2,font=('Montserrat',11),bg='white')
    new_name.place(relx=.5, rely=.48, width=180, height=30)

    label_pw = Label(frame2, text="New Password",font=('Montserrat',15),bg='white')
    label_pw.place(relx=.05, rely=.56)
    new_pw = Entry(frame2, show='*',font=('Montserrat',13),bg='white')
    new_pw.place(relx=.5,rely=.56, width=180, height=30)

    label_confirm_pw = Label(frame2, text="Confirm Password",font=('Montserrat',15),bg='white')
    label_confirm_pw.place(relx=.05, rely=.64)
    new_cpw = Entry(frame2, show='*',font=('Montserrat',13),bg='white')
    new_cpw.place(relx=.5, rely=.64, width=180, height=30)

    button_signup = Button(frame2, text="Sign Up",font=('Montserrat',17),command=sign_up)
    button_signup.place(relx=.5, rely=.8,anchor=CENTER, width=200, height=50)
    button_signup.bind("<Return>", signup_btn_shortkey) # short key for sign up button

    account=Label(frame2,text='Already have an account?',font=('Montserrat',10),bg='white')
    account.place(relx=.2,rely=.92)

    login_link=Button(frame2,text='Log in',font=('Montserrat',11, UNDERLINE),fg='blue',bd=0,cursor='hand2',bg='white',command=framedes)
    login_link.place(relx=.6,rely=.92) # ,width=100,height=25)
    login_link.bind("<Return>", login_link_shortkey) # short key for login link in sign up page

    pswd_show(frame2,new_pw,eye_img,395,295)  # moved to here for better TAB key travel
    pswd_show(frame2,new_cpw,eye_img,395,335)


#################   LOGIN_PAGE   ############################

def login_page():
    root.title("Log in page")

    def login_shortkey(event): verify_login()
    def frgt_pw_shortkey(event): FrgtPwWin()
    def reg_btn_shortkey(event): register_page()

    def verify_login():
        mydb.reconnect()
        mycursor.execute(f"SELECT * FROM PLAYERS WHERE (USERNAME = '{usrnm_email.get()}' OR EMAIL = '{usrnm_email.get()}') AND PASSWORD = '{pw.get()}'")
        #mycursor.execute(f"SELECT * FROM PLAYERS WHERE USERNAME = 'ajay' AND PASSWORD = 'sjc'") # FOR EASY LOGIN, REMOVE AT LAST
        data=mycursor.fetchall()
        global usrnm,emai
        if usrnm_email.get() == 'admin' and  pw.get() == 'pass':
            root.destroy() # destroy current window
            admin_panel() # logging in to admin panel
        elif len(data)> 0:
            usrnm=data[0][0]
            emai=data[0][1]
            root.destroy() # destroy current window
            welcome_user(usrnm, emai) # opening welcome page
        else:
            mb.showinfo("Info Error", "Invalid username or password")
    global frame
    frame=Frame(root,bg='white')
    frame.place(relx=.5,rely=.45,anchor=CENTER,width=430, height=520)

    label_title = Label(frame, text="QUIZ APP", font=('Montserrat', 50), bg='white')
    label_title.place(relx=.5,rely=0.16,anchor=CENTER)
    label_title = Label(frame, text="Log in\nto continue to Quiz App", font=('Montserrat', 12), bg='white')
    label_title.place(relx=.5, rely=.3,anchor=CENTER)

    label_usrnm_email = Label(frame, text="Username/Email", font=('Montserrat', 13), bg='white')
    label_usrnm_email.place(relx=.125, rely=.44)
    usrnm_email = Entry(frame, bg='white',font=('Montserrat',13))
    usrnm_email.place(relx=.14, rely=.495, width=300, height=30)

    label_pw = Label(frame, text="Password", font=('Montserrat', 13), bg='white')
    label_pw.place(relx=.125, rely=.567)
    
    pw = Entry(frame, bg='white', show='*',font=('Montserrat',13))
    pw.place(relx=.14, rely=.63, width=300, height=30)

    button_login = Button(frame, text="Log in", font=('Montserrat', 14), command=verify_login)
    button_login.place(relx=.5, rely=.79, width=140, height=40,anchor=CENTER)
    button_login.bind("<Return>", login_shortkey) # short key for login button
    pswd_show(frame,pw,eye_img,370,330) # moved to here for better TAB key travel

    frgt_button = Button(frame,text="forgot password?",font=('Montserrat',9,UNDERLINE)\
                      ,fg='blue',bd=0,cursor='hand2',bg='white',command=FrgtPwWin) # FrgtPwWin from forgot password
    frgt_button.place(relx=.125, rely=.696, width=120, height=20)#x=777
    frgt_button.bind("<Return>", frgt_pw_shortkey) # short key for forgot password button

    label_new_user = Label(frame, text="New player? ", font=('Montserrat', 12), bg='white')
    label_new_user.place(relx=.26, rely=.915)
    register_button = Button(frame,text="Register here",font=('Montserrat',11,UNDERLINE)\
                      ,fg='blue',bd=0,cursor='hand2',bg='white',command=register_page) # bd is border
    register_button.place(relx=.52, rely=.915, width=105, height=20)
    register_button.bind("<Return>", reg_btn_shortkey) # short key for register button

root.bind('<Escape>', exit_window)
login_page()
root.mainloop()