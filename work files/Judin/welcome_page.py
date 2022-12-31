from tkinter import *

window = Tk()
window.geometry("1920x1080")
window.title("welcome")
window.iconbitmap('favicon.ico')


#background

bg = Label(window,bg="white")
bg.place(x=0,y=0,relwidth=1,relheight=1)



#texts

username = "<username>"
welcome = Label(text="Welcome "+username,font=('Arial',40,'bold'),bg="white")
welcome.place(x=500,y=60)

stat = Label(window,text="Statistics",font=('Arial',30,'bold'),bg="white")
stat.place(x=250,y=200)

play = Label(window,text="Play now",font=('Arial',30,'bold'),bg="white")
play.place(x=1150,y=191.5)

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

b_qu = Button(window,text="Question\ncategories>>",command=qu)
b_qu.place(relx=.78,rely=.33)



window.mainloop()
