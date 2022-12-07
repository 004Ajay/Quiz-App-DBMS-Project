##########################  Forgot Password Functionality  ##########################

from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk
from pswdShowHide import pswd_show # show/hide password
from db_connect import project_db # for accessing 'our project database'

mydb = project_db()
mycursor = mydb.cursor(buffered=True)

def FrgtPwWin():
    root2=Toplevel()
    root2.title("Reset Password")
    root2.geometry("350x400+1000+220")
    root2.iconbitmap('pswd.ico')
    root2.focus_force()
    root2.grab_set()
    global eye_imge 
    eye_imge = ImageTk.PhotoImage(file="show_pw.png") # image for show/hide password

    def check_entries():
        mycursor.execute(f"SELECT * FROM PLAYERS WHERE (email = '{email_entry.get()}' AND usrnm= '{usernm_entry.get()}')")
        if email_entry.get()==""or usernm_entry.get()==""or newpw_entry.get==""or newcpw_entry.get()=="":
            mb.showinfo("Add all info", "All fields are mandatory")
        elif len(mycursor.fetchall())<1:
            mb.showinfo("Entry Invalid", "Invalid Email or Username ")
        elif newpw_entry.get() != newcpw_entry.get():
            mb.showinfo("Password Error", "Passwords doesn't match")
        else:
            mycursor.execute(f"update PLAYERS set pswd='{newcpw_entry.get()}' where email='{email_entry.get()}'")
            mydb.commit()
            root2.destroy()
            mb.showinfo("Success", "Password changed successfully")

    frame=Frame(root2,bg='white')
    frame.place(x=35,y=20,width=280, height=360)

    title1=Label(root2,text="CHANGE PASSWORD",font=("Montserrat",17),bg="white")
    title1.place(x=50,y=40)

    email_label=Label(root2,text="Enter Email",font=("Montserrat",12),bg='white')
    email_label.place(x=65,y=100)
    email_entry=Entry(root2, bg='white',font=('Montserrat',11))
    email_entry.place(x=68,y=125,width=200,height=25)

    usernm_label=Label(root2,text="Enter Username",font=("Montserrat",12),bg='white')
    usernm_label.place(x=65,y=150)
    usernm_entry=Entry(root2, bg='white',font=('Montserrat',11))
    usernm_entry.place(x=68,y=175,width=200,height=25)

    newpw_label=Label(root2,text="New Password",font=("Montserrat",12),bg='white')
    newpw_label.place(x=65,y=200)
    newpw_entry=Entry(root2,show='*',bg='white',font=('Montserrat',11))
    newpw_entry.place(x=68,y=225,width=200,height=25)
    pswd_show(root2, newpw_entry, eye_imge, 270, 225)

    newcpw_label=Label(root2,text="Confirm Password",font=("Montserrat",12),bg='white')
    newcpw_label.place(x=65,y=250)
    newcpw_entry=Entry(root2,show='*',bg='white',font=('Montserrat',11))
    newcpw_entry.place(x=68,y=275,width=200,height=25)
    pswd_show(root2, newcpw_entry, eye_imge, 270, 275)

    next_btn=Button(root2,text="confirm",font=('Montserrat', 12),bg="white",command=check_entries)
    next_btn.place(x=130,y=325, width=70, height=40)

if __name__ == '__main__':
    FrgtPwWin()