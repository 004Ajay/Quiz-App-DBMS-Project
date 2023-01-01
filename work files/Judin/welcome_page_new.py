from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("welcome"+username)
window.iconbitmap('favicon.ico')


#background

bg = Label(window,bg="white")
bg.place(x=0,y=0,relwidth=1,relheight=1)


#texts
date = "<date>"
join_date = "<join_date>"
username = "<username>"

welcome = Label(text="Welcome "+username,font=('Arial',40,'bold'),bg="white")
welcome.place(x=500,y=70)


table_label = Label()#label for the recent gameplays table....
table_label.place()

join = Label(text="Player since "+join_date,font=('Arial',19,'italic'),bg="white")
join.place(x=0,y=739)

last_played = Label(text="Last played on "+date,font=('Arial',25,'italic'),bg="white")
last_played.place(x=550,y=160)

stat = Label(window,text="Recent gameplays",font=('Arial',30,'italic'),bg="white")
stat.place(x=250,y=299)

play = Label(window,text="New game",font=('Arial',30,'italic'),bg="white")
play.place(x=1150,y=291.5)

#buttons 

def logout():
    return()

b_logout = Button(window,text ="Log out",font=('Arial',8),command=logout,height=1,width=7)
b_logout.place(relx=.919,rely=.0149)

def settings():
    return()

images = PhotoImage(file="set.png")
b_settings = Button(window,image=images,command=settings,height=25)
b_settings.place(relx=.955,rely=.008)


def qu():
    return()

b_qu = Button(window,text="Question\ncategories>>",height=3,width=13,command=qu)
b_qu.place(relx=.78,rely=.43)



window.mainloop()
