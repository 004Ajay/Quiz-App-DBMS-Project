# UPDATE PROFILE WINDOW THAT POPS-UP WHEN CLICKED ON SETTINGS ICON IN USER'S WELCOME PAGE

from tkinter import *
# from PIL import ImageTk

def settings_icon():
        root2=Toplevel()
        #root2=Tk()
        root2.title("Update User Profile")
        root2.geometry("350x400+1000+220")
        root2.focus_force()
        root2.grab_set()
        root2.config(bg='white')

        title1=Label(root2,text="Edit User Profile",font=("Montserrat",17),bg="white")
        title1.place(relx=0.5,rely=.15,anchor=CENTER)

        email_label=Label(root2,text="E-mail",font=("Montserrat",12),bg='white')
        email_label.place(relx=0.07,rely=.29)
        email_entry=Entry(root2, bg='white',font=('Montserrat',11))
        email_entry.place(relx=.34,rely=0.29,width=200,height=25)

        usernm_label=Label(root2,text="Username",font=("Montserrat",12),bg='white')
        usernm_label.place(relx=0.07,rely=0.39)
        usernm_entry=Entry(root2, bg='white',font=('Montserrat',11))
        usernm_entry.place(relx=.34,rely=0.39,width=200,height=25)

        biolbl=Label(root2,text="Biography",font=("Montserrat",12),bg='white')
        biolbl.place(relx=.07,rely=.52)
        newpw_entry=Entry(root2,show='*',bg='white',font=('Montserrat',11))
        newpw_entry.place(relx=.34,rely=.49,width=200,height=70)

        next_btn=Button(root2,text="Save Changes",font=('Montserrat', 12))
        next_btn.place(relx=0.5,rely=.8,anchor=CENTER, width=150, height=40)

#root2.mainloop()

if __name__=='__main__':
        settings_icon()
