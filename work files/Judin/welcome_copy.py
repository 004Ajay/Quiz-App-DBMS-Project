from tkinter import *

root = Tk()
root.geometry("1920x1080")
root.title("welcome + username")
root.iconbitmap('Q.ico')


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


welcome = Label(text=f"Welcome username", font=('Montserrat',33,'bold'),bg="white")
welcome.place(relx=0.5,rely=0.15, anchor=CENTER)

last_played = Label(text=f"Last played on 27/11/2022", font=('Montserrat',20),bg="white")
last_played.place(relx=0.5,rely=0.27, anchor=CENTER)

stat = Label(root,text="Recent gameplays", font=('Montserrat',20),bg="white")
stat.place(x=250,y=299)

# new_game = Label(root,text="New game", font=('Montserrat',30),bg="white")
# new_game.place(x=1150,y=291.5)

table_label = Label()#label for the recent gameplays table....
table_label.place()

join_date = Label(text="Player since: join_date", font=('Montserrat',30),bg="white")
join_date.place(x=0,y=739)

# buttons
b_logout = Button(root,text ="Log out",font=('Montserrat',12),command=logout)
b_logout.place(relx=.9,rely=0.148,height=30,width=80)

images = PhotoImage(file="settings.png")
b_settings = Button(root,image=images,height=25,command=settings)
b_settings.place(relx=.95,rely=.0149)

b_qu = Button(root,text="New Game",command=qu)
b_qu.place(x=900, y=450, width=100, height=30)

root.bind('<Escape>', exit_window)
root.mainloop()