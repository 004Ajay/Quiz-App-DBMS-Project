from tkinter import *
import mysql.connector
import tkinter.font as tkf # for setting font size for drop_down list

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root = Tk()

root.title("Admin Panel")
root.geometry("1920x1080")
#root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
# root.state('zoomed')
root.config(bg='white')


def exit_window(e):
    root.destroy()

def conti():
    print(menu.get()) # to get 

label_title = Label(root, text="Question Categories", font=('Montserrat', 35),bg='white') # center title
label_title.place(x=520, y=130)

label_heading=Label(root,text='Click the drop down to select category',font=('Montserrat', 12),bg='white') # Short Description
label_heading.place(x=615,y=200)

menu = StringVar() # drop-down list text
menu.set("Select a category") 

cate = ['Science', 'Computer', 'GK', 'Vehicles', 'Nature',
'Medicines', 'Mobile', 'Programming', 'Hardware', 'Software',
'Cricket', 'Football', 'News', 'Business', 'Slogans'] # change this to getting data from db like...

drop_down = OptionMenu(root, menu, *cate) # Create a dropdown menu
drop_down.config(font=tkf.Font(family='Montserrat', size=15)) # Montserrat
dd_list = root.nametowidget(drop_down.menuname)  # Get menu widget.
dd_list.config(font=tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
drop_down.place(x=580, y=260, width=380, height=40)


continue_button = Button(root, text="continue",font=('Montserrat',12), command = conti) # add command function
continue_button.place(x=1005, y=650, width=125, height=40)

back_button = Button(root, text="back",font=('Montserrat',12), command = "") # add command function
back_button.place(x=430, y=650, width=110, height=40)

root.bind('<Escape>', exit_window)
root.mainloop()