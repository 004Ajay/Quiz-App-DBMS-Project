# WELCOME PAGE FOR USERS

from tkinter import *
import mysql.connector
from update_profile import *



#################  KEYBOARD SHORTCUTS   ######################

# def exit_window(e): root.destroy() # to exit window

##############################################################

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor(buffered=True)

root = Tk()
root.geometry("1920x1080")
root.title("welcome + username")
root.iconbitmap('assets/Q.ico')

bg = Label(root,bg="white") #background
bg.place(x=0,y=0,relwidth=1,relheight=1)

def welcome_user(username, emai):
    


    def logout():
        return()


    def settings():
        return()


    def qu():
        return()

    mycursor.execute("SELECT * FROM players")
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


root.mainloop()
    