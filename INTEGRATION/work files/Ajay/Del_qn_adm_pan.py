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
    print(cate_menu.get(), qn_menu.get()) # to get selected item from drop down list

def del_qn():
    pass

label_title = Label(root, text="Question Categories", font=('Montserrat', 35),bg='white') # center title
label_title.place(x=520, y=130)

label_heading=Label(root,text='Click the drop down to select category',font=('Montserrat', 12),bg='white') # Short Description
label_heading.place(x=615,y=200)

cate_menu = StringVar() # drop-down list of categories
cate_menu.set("Select Question Category") 

cate = mycursor.execute("SELECT DISTINCT CATE FROM QUESTIONS")
categories = [i[0] for i in mycursor.fetchall()]

cate_drop_down = OptionMenu(root, cate_menu, *categories) # Create a dropdown menu
cate_drop_down.config(font=tkf.Font(family='Montserrat', size=15))
cate_dd_list = root.nametowidget(cate_drop_down.menuname)  # Get menu widget.
cate_dd_list.config(font=tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
cate_drop_down.place(x=580, y=330, width=380, height=40)

mydb.reconnect() # To refresh the cursor buffer

qn_menu = StringVar() # drop-down list of questions under selected category
qn_menu.set("Select the question to delete")

sel_cate_qns = mycursor.execute(f"SELECT QN FROM QUESTIONS WHERE CATE = '{cate_menu.get()}'")
qns_lst = [i[0] for i in mycursor.fetchall()]

qn_drop_down = OptionMenu(root, qn_menu, *qns_lst) # Create a dropdown menu for questions of selected category
qn_drop_down.config(font=tkf.Font(family='Montserrat', size=15))
qn_dd_list = root.nametowidget(qn_drop_down.menuname)  # Get menu widget.
qn_dd_list.config(font=tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
qn_drop_down.place(x=580, y=430, width=380, height=40)

continue_button = Button(root, text="Delete Question",font=('Montserrat',12), command = del_qn) # add command function
continue_button.place(x=680, y=550, width=170, height=40)

# back_button = Button(root, text="back",font=('Montserrat',12), command = "") # add command function
# back_button.place(x=430, y=650, width=110, height=40)

root.bind('<Escape>', exit_window)
root.mainloop()