from tkinter import *
import mysql.connector
#from update_profile import *

root = Tk()
root.geometry("1920x1080")
root.title("welcome + username")
root.iconbitmap('Q.ico')

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor(buffered=True)


#background
bg = Label(root,bg="white")
bg.place(x=0,y=0,relwidth=1,relheight=1)

#################  KEYBOARD SHORTCUTS   ######################

def exit_window(e): root.destroy() # to exit window

##############################################################

def logout():
    return()


def settings():
    return()


def qu():
    return()

mycursor.execute("SELECT * FROM PLAYERS")
res = mycursor.fetchall()
# print(res)


"""mycursor.execute("SELECT * FROM PLAYERS")
i=0 
for student in mycursor: 
    for j in range(len(student)):
        print(student[j],end='')
    i=i+1
    print()# line break at the end of one row"""

welcome = Label(text=f"Welcome username", font=('Montserrat',33,'bold'),bg="white")
welcome.place(relx=0.5,rely=0.15, anchor=CENTER)

last_played = Label(text=f"Last played on 27/11/2022", font=('Montserrat',20),bg="white")
last_played.place(relx=0.5,rely=0.27, anchor=CENTER)

stat = Label(root,text="Recent gameplays", font=('Montserrat',20),bg="white")
stat.place(x=380,y=310)

# new_game = Label(root,text="New game", font=('Montserrat',30),bg="white")
# new_game.place(x=1150,y=291.5)

# table_label = Label(root, bg='red')#label for the recent gameplays table....
# table_label.place(x=240, y=360, width=500, height=300)

join_date = Label(text="Player since: 17/11/2022", font=('Montserrat',15),bg="white")
join_date.place(x=20,y=719)

# buttons
b_logout = Button(root,text ="Log out",font=('Montserrat',12),command=logout)
b_logout.place(relx=.89,rely=0.016,height=30,width=80)

b_settings = Button(root,image=PhotoImage(file="settings.png"),height=25)#, command= settings_icons)
b_settings.place(relx=.95,rely=.0149)

b_qu = Button(root,text="New Game",font=('Montserrat',15), command=qu)
b_qu.place(x=1000, y=400, width=160, height=50)

"""
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
"""


root.bind('<Escape>', exit_window)
root.mainloop()