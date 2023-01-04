# CATEGORY SELECTION AND GAMEPLAY

from tkinter import *
import tkinter.font as tkf # for setting font size for drop_down list
from tkinter import messagebox as mb
from db_connect import project_db

mydb = project_db()
mycursor = mydb.cursor(buffered=True)

global i,data,r1,r2,r3,r4,s,cnt1,rep,cat

def win(username, emai):
    root = Tk()
    root.title("Gameplay")
    root.geometry("1920x1080")
    root.config(bg='white')

    def exit_window(e): root.destroy()

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
        user=[] # to retrive user selection
        ans=[]  # to retrive correct answer from database
        l1=Label()
        global qnn
        qnn=0
        radiovar=StringVar()
        radiovar.set(None)
    
    
    ###########  TO DESTROY BUTTONS  ##################
        def des():
            r1.destroy()
            r2.destroy()
            r3.destroy()
            r4.destroy()
            s.destroy()
            cnt1.destroy()
            # exit_btn.destroy()

    ###########  IF 'EXIT' BUTTON IS CLICKED DURING GAMEPLAY  ##################    
        # def exit_to_result():
            # rep.destroy()
            # des()
            # calc_mark()
            # crt_ans = user_ans
            # wrong_ans = 
            # result(crt_ans, wrong_ans, score)
            # pass
            
    #############  CODE TO APPEND USER ANSWER TO VARIABLE 'USER' #################
    
        def selected():
            if radiovar.get()==NONE:
                mb.showinfo('Mandatory','choose an option')
            else:
                rep.destroy()
                des()
                global user_ans
                user_ans = radiovar.get()
                user.append(user_ans)
                mycursor.execute(f'insert into quiz_activity(player_email,date_played,category,question,user_answer,correct_answer) values(\'{emai}\',curdate(),\'{data[qnn-1][7]}\',\'{data[qnn-1][1]}\',\'{user_ans}\',\'{data[qnn-1][6]}\');')
                mydb.commit()
                mydb.reconnect()
                if qnn==tot_qns: # change no of questions here
                    des()
                    result()
                    # calc_mark()
                else:
                    qn()
                
    
    #########  TO RETRIVE QUESTION DATA FROM DATABASE   ###############
    
        def ques():
            global data
            mycursor.execute(f'SELECT * FROM QUESTIONS WHERE CATE_NAME=\'{cat}\' ORDER BY RAND()')
            data=mycursor.fetchall()
            global tot_qns
            tot_qns = len(data)
            qn()
    
    
    ########## TO CALCULATE SCORE AND DISPLAY   #################

        def exit_now():
            root.destroy()
            import welcome_page 
            welcome_page.welcome_user(username, emai)
        """def calc_mark():
            global crt_ans, wrong_ans, score 

            crt_ans = wrong_ans = score = 0
            for j in range(0, tot_qns): # change no of questions here
                if user[j]==ans[j]:
                    score += 10
                    crt_ans += 1
                else:
                    score -= 10
                    wrong_ans += 1
            
            if score < 0: # if score goes negative
                score = 0

               
            result(crt_ans, wrong_ans, score)    """

        def result():
            root.title('Result')
            crt_ans = wrong_ans = score = 0
            for j in range(0,tot_qns): # change no of questions here
                if user[j]==ans[j]:
                    score += 10
                    crt_ans += 1
                else:
                    wrong_ans += 1
            
            if score < 0: # if score goes negative
                score = 0

            rslt=Label(root,text=f'Result of {cat} Quiz',font=('Montserrat',20,UNDERLINE,'bold'),bg='white')
            rslt.place(relx=0.5,rely=0.1,anchor=CENTER)
    
            usr=Label(root,text= f'Username: {username}',font=('Montserrat',16),bg='white') # change username to get from db 
            usr.place(relx=0.5,rely=0.17,anchor=CENTER)

            score=Label(root, text= f'Score: {score}', font=('Montserrat',16), bg='white') # change username to get from db 
            score.place(relx=0.5,rely=0.23,anchor=CENTER)
    
            dtl=Label(root,text='Detailed Report',font=('Montserrat',16,UNDERLINE),bg='white')
            dtl.place(relx=0.5,rely=0.3,anchor=CENTER)
    
            totqn=Label(root,text='Total Questions Attended:',font=('Montserrat',16),bg='white')
            totqn.place(relx=0.49,rely=0.37,anchor=CENTER)
    
            totqnlb=Label(root,text=qnn,bg='white',font=('Montserrat', 16))
            totqnlb.place(relx=0.6,rely=0.37, anchor=CENTER)
    
            crtans=Label(root,text='Correctly Answered:',font=('Montserrat',16),bg='white')
            crtans.place(relx=0.43,rely=0.4)
    
            crtanslb=Label(root,text=crt_ans,bg='white',font=('Montserrat', 16))
            crtanslb.place(relx=0.59,rely=0.4)
    
            wrngans=Label(root,text='Wrongly Answered:',font=('Montserrat',16),bg='white')
            wrngans.place(relx=0.43,rely=0.44)
    
            wrnganslb=Label(root,text=wrong_ans,bg='white',font=('Montserrat', 16))
            wrnganslb.place(relx=0.58,rely=0.442)
    
            lgot=Button(root,text='Log Out',font=('Montserrat', 15))
            lgot.place(relx=0.22,rely=0.6,width=150,height=50)
    
            cnt=Button(root,text='Continue',font=('Montserrat', 15),command=exit_now)
            cnt.place(relx=0.68,rely=0.6,width=150,height=50)
    
    ############## USER   ############
    
        def qn():
            global i, data, qnn, r1, r2, r3, r4, s, cnt1, exit_btn, rep
            i=0
            if qnn<tot_qns: # change no of questions here
                radiovar.set(NONE)
                ans.append(data[qnn][6])
    
                s=Label(root,text=f'{qnn+1}. '+data[qnn][1],bg='white',font=('Montserrat', 18))
                s.place(relx=0.5,rely=0.2,anchor=CENTER)
                
                r1 = Radiobutton(root,text=data[qnn][2],variable=radiovar,value=data[qnn][2],bg='white',font=('Montserrat', 15))
                r1.place(relx=0.46,rely=0.3)
    
                r2 = Radiobutton(root,text=data[qnn][3],variable=radiovar,value=data[qnn][3],bg='white',font=('Montserrat', 15))
                r2.place(relx=0.46,rely=0.34)
    
                r3 = Radiobutton(root,text=data[qnn][4],variable=radiovar,value=data[qnn][4],bg='white',font=('Montserrat', 15))
                r3.place(relx=0.46,rely=0.38)
    
                r4 = Radiobutton(root,text=data[qnn][5],variable=radiovar,value=data[qnn][5],bg='white',font=('Montserrat', 15))
                r4.place(relx=0.46,rely=0.42)
                qnn+=1
    
                rep=Button(root,text='Report',font=('Montserrat', 15,UNDERLINE),bg='white',fg='blue',bd=0,cursor='hand2')
                rep.place(relx=0.22,rely=0.8,width=150,height=50)
    
                # exit_btn=Button(root,text='Exit',font=('Montserrat', 15),command=exit_to_result)
                # exit_btn.place(relx=0.46,rely=0.8,width=140,height=40)
    
                cnt1=Button(root,text='Continue',font=('Montserrat', 15),command=selected)
                cnt1.place(relx=0.68,rely=0.8,width=150,height=40)

                # scr_label = Label(root, )
        drpg()

    label_title = Label(root, text="Question Categories", font=('Montserrat', 35),bg='white') # Center Title
    label_title.place(relx=.5, rely=.15,anchor=CENTER)

    label_heading=Label(root,text='Click the drop down to select category',font=('Montserrat', 12),bg='white') # Short Description
    label_heading.place(relx=.5, rely=.21,anchor=CENTER)

    menu = StringVar() # drop-down list text
    menu.set("Select a category") 

    # cate = mycursor.execute("SELECT DISTINCT CATE FROM QUESTIONS")
    # categories = [i[0] for i in cate] #mycursor.fetchall()]

    mycursor.execute("SELECT DISTINCT CATE_NAME FROM QUESTIONS")
    categories = [i[0] for i in mycursor.fetchall()]

    drop_down = OptionMenu(root, menu, *categories) # Create a dropdown menu
    drop_down.config(font=tkf.Font(family='Montserrat', size=15)) # Montserrat
    dd_list = root.nametowidget(drop_down.menuname)  # Get menu widget.
    dd_list.config(font=tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
    drop_down.place(relx=.5, rely=.3,anchor=CENTER, width=380, height=40)


    continue_button = Button(root, text="continue",font=('Montserrat',12), command = gameplay) # add command function
    continue_button.place(relx=0.68,rely=0.8, width=125, height=40)

    back_button = Button(root, text="back",font=('Montserrat',12), command = "") # add command function
    back_button.place(relx=0.22,rely=0.8, width=110, height=40)

    root.bind('<Escape>', exit_window)