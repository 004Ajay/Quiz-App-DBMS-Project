# CURRENT STARTING FILE

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
from pswdShowHide import pswd_show # show/hide password
from forgot_pswd import * # from forgot password file
from db_connect import project_db # for accessing 'our project database'
# from update_profile import *
# from wel_cpy import *
# from cat_sel_gmply_copy import *
# from catsel_test import *
from welcome_test import * # moving to welcome page

mydb = project_db()
mycursor = mydb.cursor(buffered=True)
"""
A buffered cursor stores the result set in the client's memory after executing a SELECT statement.
This can be more memory efficient than a non-buffered cursor, which stores the entire result set on the server
and retrieves it row by row as needed.
"""

root = Tk()
root.geometry("1920x1080")
"""
# can use this as final
# it will autmtcly gets screen size and will zoom the window to dim of screen
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}") # "1920x1080"
root.state('zoomed')
"""

#################  KEYBOARD SHORTCUTS   ######################

def exit_window(e): root.destroy() # to exit window

#################  ICONS & IMAGES   ######################

root.iconbitmap("assets/Q.ico") # app icon (top left corner)
eye_img = ImageTk.PhotoImage(master = root, file="assets/show_pw.png") # to show/hide password
bg1=ImageTk.PhotoImage(master = root, file="assets/main_bg.jpg")  # change path of image as in your system 
bg_lbl=Label(root, image=bg1).place(x=0, y=-0, relwidth=1, relheight=1)



"""
def welcome_user(username, emai):
        bg = Label(root,bg="white") #background
        bg.place(x=0,y=0,relwidth=1,relheight=1)


        def logout():
            pass


        def settings():
            return()


        def qu():
            gameplay()

        welcome = Label(text=f"Welcome {username}", font=('Montserrat',33,'bold'),bg="white")
        welcome.place(relx=0.5,rely=0.15, anchor=CENTER)

        last_played = Label(text=f"Last played on 27/11/2022", font=('Montserrat',20),bg="white")
        last_played.place(relx=0.5,rely=0.27, anchor=CENTER)

        stat = Label(root,text="Recent gameplays", font=('Montserrat',20),bg="white")
        stat.place(x=380,y=310)

        join_date = Label(text="Player since: 17/11/2022", font=('Montserrat',15),bg="white")
        join_date.place(x=20,y=719)

        # buttons
        b_logout = Button(root,text ="Log out",font=('Montserrat',12),command=logout)
        b_logout.place(relx=.89,rely=0.016,height=30,width=80)

        im = PhotoImage(file="settings.png") 
        b_settings = Button(root,image=im,height=25, command= settings_icon)
        b_settings.place(relx=.95,rely=.0149)

        b_qu = Button(root,text="New Game",font=('Montserrat',15), command=qu)
        b_qu.place(x=1000, y=400, width=160, height=50)


        mycursor.execute("SELECT * FROM PLAYERS")
        results = mycursor.fetchall() # Retrieve the query results
        column_names = [column[0] for column in mycursor.description] # Get the column names


        frame = Frame(root, bg='white')
        frame.place(x=510, y=440, anchor=CENTER) # to change position of table

        # Create a label for each column and place it in the frame
        labels = []
        for i, column_name in enumerate(column_names):
            label = Label(frame, text=column_name, bg='white')
            label.grid(row=0, column=i)
            labels.append(label)

        # Create a label for each row and place it in the frame
        for i, row in enumerate(results):
            for j, col in enumerate(row):
                label = Label(frame, text=col, bg='white')
                label.grid(row=i+1, column=j)
                labels.append(label)
"""

#################   SIGN_UP PAGE   ############################

def register_page():
    root.title("Signup Page")

    def sign_up():
        name=new_name.get()
        pw1=new_pw.get()
        cpw=new_cpw.get()
        em=new_mail.get()
        mycursor.execute(f"SELECT * FROM PLAYERS WHERE USRNM = '{name}' OR EMAIL= '{em}'")
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
    pswd_show(root,new_pw,eye_img,960,383)

    label_confirm_pw = Label(root, text="Confirm Password",font=('Montserrat',15),bg='white')
    label_confirm_pw.place(x=585, y=420)
    new_cpw = Entry(root, show='*',font=('Montserrat',13),bg='white')
    new_cpw.place(x=780, y=420, width=180, height=30)
    pswd_show(root,new_cpw,eye_img,960,423)

    button_signup = Button(root, text="Sign Up",font=('Montserrat',17),command=sign_up)
    button_signup.place(x=676, y=480, width=200, height=50)

    account=Label(root,text='Already have an account?',font=('Montserrat',10),bg='white')
    account.place(x=655,y=575)

    login_btn=Button(root,text='Log in',font=('Montserrat',11, UNDERLINE),fg='blue',bd=0,cursor='hand2',bg='white',command=login_page)
    login_btn.place(x=830,y=568) # ,width=100,height=25)
    

#################   LOGIN_PAGE   ############################

def login_page():
    root.title("Log in page")

    def verify_login():
        mydb.reconnect()
        mycursor.execute(f"SELECT * FROM PLAYERS WHERE (USERNAME = '{usrnm_email.get()}' OR EMAIL = '{usrnm_email.get()}') AND PASSWORD = '{pw.get()}'")
        #mycursor.execute(f"SELECT * FROM PLAYERS WHERE USERNAME = 'ajay' AND PASSWORD = 'sjc'") # FOR EASY LOGIN, REMOVE AT LAST
        data=mycursor.fetchall()
        global usrnm,emai
        if usrnm_email.get() == 'Admin' and  pw.get() == 'pass':
            # admin_panel()
            print("log to admin")
        elif len(data)> 0:
            usrnm=data[0][0]
            emai=data[0][1]
            root.destroy() # destroy current window
            welcome_user(usrnm, emai) # opening welcome page
        else:
            mb.showinfo("Info Error", "Invalid username or password")

    frame=Frame(root,bg='white')
    frame.place(x=565,y=95,width=430, height=520)

    label_title = Label(root, text="QUIZ APP", font=('Montserrat', 50), bg='white')
    label_title.place(x=615, y=100)
    label_title = Label(root, text="Log in\nto continue to Quiz App", font=('Montserrat', 12), bg='white')
    label_title.place(x=690, y=192)

    label_usrnm_email = Label(root, text="Username/Email", font=('Montserrat', 13), bg='white')
    label_usrnm_email.place(x=620, y=315)
    usrnm_email = Entry(root, bg='white',font=('Montserrat',13))
    usrnm_email.place(x=625, y=350, width=300, height=30)

    label_pw = Label(root, text="Password", font=('Montserrat', 15), bg='white')
    label_pw.place(x=620, y=390)
    
    pw = Entry(root, bg='white', show='*',font=('Montserrat',13))
    pw.place(x=625, y=423, width=300, height=30)
    pswd_show(root,pw,eye_img,930,425)

    frgt_button = Button(root,text="forgot password?",font=('Montserrat',9,UNDERLINE)\
                      ,fg='blue',bd=0,cursor='hand2',bg='white',command=FrgtPwWin) # FrgtPwWin from forgot password
    frgt_button.place(x=618, y=455, width=120, height=20)#x=777

    button_login = Button(root, text="Log in", font=('Montserrat', 14), command=verify_login)
    button_login.place(x=703, y=486, width=140, height=40)
    
    label_new_user = Label(root, text="New player? ", font=('Montserrat', 12), bg='white')
    label_new_user.place(x=675, y=570)
    register_button = Button(root,text="Register here",font=('Montserrat',11,UNDERLINE)\
                      ,fg='blue',bd=0,cursor='hand2',bg='white',command=register_page) # bd is border
    register_button.place(x=777, y=567, width=125, height=35)

root.bind('<Escape>', exit_window)
login_page()
root.mainloop()