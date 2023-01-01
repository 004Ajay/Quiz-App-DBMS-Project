from tkinter import *
#import mysql.connector
import tkinter.font as tkf # for setting font size for drop_down list

from tkinter import messagebox as mb
from PIL import ImageTk
import mysql.connector

root = Tk()

root.title("Admin Panel")
root.geometry("1920x1080")
#root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
# root.state('zoomed')
root.config(bg='white')

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)
global i,data,scibtn,r1,r2,r3,r4,s,cnt1,rep,cat
def gameplay():
    def drpg():
        global cat
        cat=menu.get()
        ques()
    label_title.destroy()
    drop_down.destroy()
    label_heading.destroy()
    continue_button.destroy()
    back_button.destroy()
    user=[] #to retrive user selection
    ans=[]  #to retrive correct answer from database
    l1=Label()
    global qnn
    qnn=0
    radiovar=StringVar()
    radiovar.set(None)
    ###########  FOR DESTROY BUTTONS  ##################
    def des():
        r1.destroy()
        r2.destroy()
        r3.destroy()
        r4.destroy()
        s.destroy()
        cnt1.destroy()
        
        

    #############  CODE TO APPEND USER ANSWER TO VARIABLE 'USER' #################

    def selected():
        if radiovar.get()==NONE:
            mb.showinfo('Mandatory','choose an option')
        else:
            rep.destroy()
            des()
            z=radiovar.get()
            user.append(z)
            if qnn==3:
                des()
                result()
            else:
            
                qn()
                



    #########  TO RETRIVE QUESTION DATA FROM DATABASE   ###############

    def ques():
        global data,scibtn
        #scibtn.destroy()
        mycursor.execute(f'select * from questions where CATE=\'{cat}\' order by rand()')
        data=mycursor.fetchall()
        qn()


    ########## TO CALCULATE SCORE AND DISPLAY   #################

    def result():
        root.title('Result')
        #score=0
        crt_ans=0
        wrong_ans=0
        for j in range(0,3):
            if user[j]==ans[j]:
                #score+=5
                crt_ans+=1
            else:
                wrong_ans+=1
        
        rslt=Label(root,text='Result Of Software Quiz',font=('Montserrat',20,UNDERLINE,'bold'),bg='white')
        rslt.place(relx=0.5,rely=0.1,anchor=CENTER)

        usr=Label(root,text='Username:<username>',font=('Montserrat',16),bg='white')
        usr.place(relx=0.32,rely=0.19)

        tme=Label(root,text='Time Taken:<time_taken>',font=('Montserrat',16),bg='white')
        tme.place(relx=0.53,rely=0.19)

        dtl=Label(root,text='Detailed Report',font=('Montserrat',16,UNDERLINE),bg='white')
        dtl.place(relx=0.32,rely=0.3)

        totqn=Label(root,text='Total Questions Attended:',font=('Montserrat',16),bg='white')
        totqn.place(relx=0.32,rely=0.37)

        totqnlb=Label(root,text=qnn,bg='white',font=('Montserrat', 16))
        totqnlb.place(relx=0.484,rely=0.37)

        crtans=Label(root,text='Correctly Answered:',font=('Montserrat',16),bg='white')
        crtans.place(relx=0.32,rely=0.41)

        crtanslb=Label(root,text=crt_ans,bg='white',font=('Montserrat', 16))
        crtanslb.place(relx=0.45,rely=0.41)

        wrngans=Label(root,text='Wrongly Answered:',font=('Montserrat',16),bg='white')
        wrngans.place(relx=0.32,rely=0.45)

        wrnganslb=Label(root,text=wrong_ans,bg='white',font=('Montserrat', 16))
        wrnganslb.place(relx=0.444,rely=0.45)

        lgot=Button(root,text='Log Out',font=('Montserrat', 15))
        lgot.place(relx=0.22,rely=0.6,width=150,height=50)

        cnt=Button(root,text='Continue',font=('Montserrat', 15),command=exit)
        cnt.place(relx=0.68,rely=0.6,width=150,height=50)


    ############## USER   ############


    def qn():
        global i,data,qnn,scibtn,r1,r2,r3,r4,s,cnt1,rep
    
        i=0
        if qnn<3:
            radiovar.set(NONE)
            ans.append(data[qnn][6])

            s=Label(root,text=data[qnn][1],bg='white',font=('Montserrat', 18))
            s.place(relx=0.5,rely=0.2,anchor=CENTER)
            

            r1 = Radiobutton(root,text=data[qnn][2],variable=radiovar,value=data[qnn][2],bg='white',font=('Montserrat', 15))
            r1.place(relx=0.48,rely=0.3)

            r2 = Radiobutton(root,text=data[qnn][3],variable=radiovar,value=data[qnn][3],bg='white',font=('Montserrat', 15))
            r2.place(relx=0.48,rely=0.34)

            r3 = Radiobutton(root,text=data[qnn][4],variable=radiovar,value=data[qnn][4],bg='white',font=('Montserrat', 15))
            r3.place(relx=0.48,rely=0.38)

            r4 = Radiobutton(root,text=data[qnn][5],variable=radiovar,value=data[qnn][5],bg='white',font=('Montserrat', 15))
            r4.place(relx=0.48,rely=0.42)
            qnn+=1

            rep=Button(root,text='Report',font=('Montserrat', 15,UNDERLINE),bg='white',fg='blue',bd=0,cursor='hand2')
            rep.place(relx=0.22,rely=0.8,width=150,height=50)


            cnt1=Button(root,text='Continue',font=('Montserrat', 15),command=selected)
            cnt1.place(relx=0.68,rely=0.8,width=150,height=50)
        
    #scibtn=Button(root,text="Science",font=('Montserrat', 18,'bold'),bg="white",command=ques)
    #scibtn.place(relx=0.5,rely=0.5,anchor=CENTER,width=100,height=50)
    drpg()
    #ques()



def exit_window(e):
    root.destroy()

def conti():
    print(menu.get()) # to get selected item from drop down list

label_title = Label(root, text="Question Categories", font=('Montserrat', 35),bg='white') # center title
label_title.place(relx=.5, rely=.15,anchor=CENTER)

label_heading=Label(root,text='Click the drop down to select category',font=('Montserrat', 12),bg='white') # Short Description
label_heading.place(relx=.5, rely=.2,anchor=CENTER)

menu = StringVar() # drop-down list text
menu.set("Select a category") 

cate = ['Computer',
        'Automobiles',
        'Business',
        'General Knowledge',
        'Nature'] # change this to getting data from db like...

drop_down = OptionMenu(root, menu, *cate) # Create a dropdown menu
drop_down.config(font=tkf.Font(family='Montserrat', size=15)) # Montserrat
dd_list = root.nametowidget(drop_down.menuname)  # Get menu widget.
dd_list.config(font=tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
drop_down.place(relx=.5, rely=.3,anchor=CENTER, width=380, height=40)


continue_button = Button(root, text="continue",font=('Montserrat',12), command = gameplay) # add command function
continue_button.place(relx=0.68,rely=0.8, width=125, height=40)

back_button = Button(root, text="back",font=('Montserrat',12), command = "") # add command function
back_button.place(relx=0.22,rely=0.8, width=110, height=40)

root.bind('<Escape>', exit_window)
root.mainloop()


'Computer Science',
'Automobiles',
'Business',
'General Knowledge',
'Nature'
