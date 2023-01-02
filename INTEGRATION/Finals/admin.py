from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
# import tkinter.font as tkf # for setting font size for drop_down list
from db_connect import project_db


side_panel_bg = "#3F3F3F"
side_panel_font = "Montserrat, 15"
admin_panel_item_font= "Montserrat, 25"

mydb = project_db()
mycursor = mydb.cursor(buffered=True)

root = tk.Tk()
root.title("Admin")
root.geometry("1920x1080")
# root.iconbitmap("DBMS-Project/work files/Noyal/Q.ico")
root.iconbitmap("Q.ico")

#################  KEYBOARD SHORTCUTS   ######################

def exit_window(e): root.destroy() # to exit window

##############################################################

# BUTTON FUNCTION

def dashboard():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
        widget.destroy()

    admin_panel_label = tk.Label(content_frame, text="Admin Panel", font="Montserrat, 45", bg="white")
    admin_panel_label.pack(pady=30)

    admin_panel_items_frame = tk.Label(content_frame, bg="white")
    admin_panel_items_frame.pack()

    mycursor.execute("SELECT COUNT(DISTINCT(EMAIL)) FROM PLAYERS")
    tot_users = mycursor.fetchall()[0][0] # selecting req value from output: [(5,)]
    mycursor.execute('SELECT COUNT(DISTINCT(CATEGORY_NAME)) FROM CATEGORIES')
    tot_cate = mycursor.fetchall()[0][0]
    mycursor.execute('SELECT COUNT(DISTINCT(Q_NO)) FROM QUESTIONS')
    tot_qns = mycursor.fetchall()[0][0]

    total_user_label = tk.Label(admin_panel_items_frame, text=f"Total Users\n\n{tot_users}", font=admin_panel_item_font, bg="#9747FF", padx=30, pady=20)
    total_user_label.grid(row=0, column=0, padx=50, pady=100)

    total_categories_label = tk.Label(admin_panel_items_frame, text=f"Total Categories\n\n{tot_cate}", font=admin_panel_item_font, bg="#60F93E", padx=30, pady=20)
    total_categories_label.grid(row=0, column=1, padx=50)

    total_question_label = tk.Label(admin_panel_items_frame, text=f"Total Questions\n\n{tot_qns}", font=admin_panel_item_font, bg="#6BFFFF", padx=30, pady=20)
    total_question_label.grid(row=0, column=2, padx=50)

    # Notification Frame
    notification_frame = tk.LabelFrame(admin_panel_items_frame, bg="#F0F0F0")#,width=100, height=250)
    notification_frame.grid(row=1, column=2)

    notification_label = tk.Label(notification_frame, text="Notifications", padx=10, font="Montserrat, 25",width=10, height=3)
    notification_label.pack()

    # notif = mycursor.execute('select * from report') # enable after table creation
    notification_label = tk.Label(notification_frame, text="No new reports", padx=30, font="Montserrat, 25")
    notification_label.pack(pady=20)

    # FOR SHOWING SQL INSIDE TKINTER WINDOW

    mycursor.execute("SELECT * FROM players")
    results = mycursor.fetchall() # Retrieve the query results
    column_names = [column[0] for column in mycursor.description] # Get the column names

    frame = Frame(admin_panel_items_frame, bg='white')
    frame.place(x=350, y=460, anchor="center") # to change position of table

    # Create a label for each column and place it in the frame
    labels = []
    for i, column_name in enumerate(column_names):
        label = tk.Label(frame, text=column_name,font=('Montserrat', 15), bg='white')
        label.grid(row=0, column=i)
        labels.append(label)

    # Create a label for each row and place it in the frame
    for i, row in enumerate(results):
        for j, col in enumerate(row):
            label = tk.Label(frame, text=col,font=('Montserrat', 12), bg='white')
            label.grid(row=i+1, column=j)
            labels.append(label)

def des():
    cate_drop_down.destroy()
    show_qn_btn.destroy()
    del_button.destroy() 
    qn_drop_down.destroy()



def question_controls():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
        widget.destroy()

    question_controls_label = tk.Label(content_frame, bg="white", text="Question Controls", font="Montserrat, 55")
    question_controls_label.pack(pady=30)

    question_controls_frame = tk.Frame(content_frame, bg="white")
    question_controls_frame.pack()

    add_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Add Question", padx=10, pady=5, font="Montserrat, 25", command=add_question)
    add_question_button.grid(row=0, column=0)

    update_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Update Question", padx=10, pady=5, font="Montserrat, 25", command=update_question)
    update_question_button.grid(row=0, column=1, padx=200, pady=50)

    delete_question_button = tk.Button(question_controls_frame, bg="#F0F0F0", text="Delete Question", padx=10, pady=5, font="Montserrat, 25", command=delete_question)
    delete_question_button.grid(row=0, column=2)



def user_controls():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
        widget.destroy()

    user_controls_label = tk.Label(content_frame, bg="white", text="User Controls", font="Montserrat, 55")
    user_controls_label.pack(pady=30)

    user_controls_frame = tk.Frame(content_frame, bg="white")
    user_controls_frame.pack()

    add_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Add User", padx=10, pady=5, font="Montserrat, 25", command=add_user)
    add_user_button.grid(row=0, column=0)

    update_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Update User", padx=10, pady=5, font="Montserrat, 25", command=update_user)
    update_user_button.grid(row=0, column=1, padx=200, pady=50)

    delete_user_button = tk.Button(user_controls_frame, bg="#F0F0F0", text="Delete User", padx=10, pady=5, font="Montserrat, 25", command=delete_user)
    delete_user_button.grid(row=0, column=2)


"""
# TO BE COMPLETED IF WE GET TIME

def statistics():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
        widget.destroy()

def user_reports():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
        widget.destroy()
"""



##################### QUESTION CONTROLS SECTION #############################

def add_question():

    des()

    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    question_controls()

    add_qn_frame = tk.LabelFrame(content_frame, text="Add Question", font=admin_panel_item_font, bg='White')
    add_qn_frame.pack(side="top")

    question_title_label = tk.Label(add_qn_frame, text="Enter question title", font=side_panel_font, justify="left",bg='white')
    question_title_label.grid(row=0, column=0, sticky="w", padx=60)

    ent_qn_title = tk.Entry(add_qn_frame, borderwidth=5, width=160)
    ent_qn_title.grid(row=1, column=0, columnspan=3, padx=60)

    opt_1_lbl = tk.Label(add_qn_frame, text="Option 1", font=side_panel_font,bg='white')
    opt_1_lbl.grid(row=2, column=0, sticky="w", pady=15, padx=60)
    opt_1_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    opt_1_ent.grid(row=3, column=0, sticky="w", padx=60)
    opt_2_lbl = tk.Label(add_qn_frame, text="Option 2", font=side_panel_font,bg='white')
    opt_2_lbl.grid(row=2, column=2, sticky="w", padx=60)
    opt_2_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    opt_2_ent.grid(row=3, column=2, sticky="w", pady=15, padx=60)
    opt_3_lbl = tk.Label(add_qn_frame, text="Option 3", font=side_panel_font,bg='white')
    opt_3_lbl.grid(row=4, column=0, sticky="w", padx=60)
    opt_3_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    opt_3_ent.grid(row=5, column=0, sticky="w", pady=15, padx=60)
    opt_4_lbl = tk.Label(add_qn_frame, text="Option 4", font=side_panel_font,bg='white')
    opt_4_lbl.grid(row=4, column=2, sticky="w", padx=60)
    opt_4_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    opt_4_ent.grid(row=5, column=2, sticky="w", padx=60)

    crt_ans_lbl = tk.Label(add_qn_frame, text="Correct Answer", font=side_panel_font,bg='white')
    crt_ans_lbl.grid(row=6, column=0, sticky="w", padx=60)
    crt_ans_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    crt_ans_ent.grid(row=7, column=0, sticky="w", pady=15, padx=60)
    
    qn_cate_lbl = tk.Label(add_qn_frame, text="Question Category", font=side_panel_font,bg='white')
    qn_cate_lbl.grid(row=6, column=2, sticky="w", padx=60)
    qn_cate_ent = tk.Entry(add_qn_frame, borderwidth=5, width=50)
    qn_cate_ent.grid(row=7, column=2, sticky="w", padx=60)

    add_qn_btn = tk.Button(add_qn_frame, text="Add Question", font="Montserrat, 25")
    add_qn_btn.grid(column=1, pady=30)


def update_question():
    des()
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    question_controls()

    update_qn_frame = tk.LabelFrame(content_frame, text="Update Question", font=admin_panel_item_font,bg='White')
    update_qn_frame.pack()

    qn_title_lbl = tk.Label(update_qn_frame, text="Edit Question title", font=side_panel_font, justify="left",bg='White')
    qn_title_lbl.grid(row=0, column=0, sticky="w", padx=40)

    entry_question_title = tk.Entry(update_qn_frame, borderwidth=5, width=160)
    entry_question_title.grid(row=1, column=0, columnspan=4, padx=60)

    opt_1_lbl = tk.Label(update_qn_frame, text="Edit Option 1", font=side_panel_font,bg='White')
    opt_1_lbl.grid(row=2, column=0, sticky="w", pady=15, padx=60)
    opt_1_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    opt_1_ent.grid(row=3, column=0, sticky="w", padx=60)
    opt_2_lbl = tk.Label(update_qn_frame, text="Edit Option 2", font=side_panel_font,bg='white')
    opt_2_lbl.grid(row=2, column=2, sticky="w", padx=60)
    opt_2_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    opt_2_ent.grid(row=3, column=2, sticky="w", pady=15, padx=60)
    opt_3_lbl = tk.Label(update_qn_frame, text="Edit Option 3", font=side_panel_font,bg='white')
    opt_3_lbl.grid(row=4, column=0, sticky="w", padx=60)
    opt_3_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    opt_3_ent.grid(row=5, column=0, sticky="w", pady=15, padx=60)
    opt_4_lbl = tk.Label(update_qn_frame, text="Edit Option 4", font=side_panel_font,bg='white')
    opt_4_lbl.grid(row=4, column=2, sticky="w", padx=60)
    opt_4_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    opt_4_ent.grid(row=5, column=2, sticky="w", padx=60)

    crt_ans_lbl = tk.Label(update_qn_frame, text="Edit Correct Answer", font=side_panel_font,bg='white')
    crt_ans_lbl.grid(row=6, column=0, sticky="w", padx=60)
    crt_ans_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    crt_ans_ent.grid(row=7, column=0, sticky="w", pady=15, padx=60)
    
    qn_cate_lbl = tk.Label(update_qn_frame, text="Edit Question Category", font=side_panel_font,bg='white')
    qn_cate_lbl.grid(row=6, column=2, sticky="w", padx=60)
    qn_cate_ent = tk.Entry(update_qn_frame, borderwidth=5, width=50)
    qn_cate_ent.grid(row=7, column=2, sticky="w", padx=60)

    add_qn_btn = tk.Button(update_qn_frame, text="Update Question", font="Montserrat, 25")
    add_qn_btn.grid(column=1, pady=30)


def delete_question():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    question_controls()

    global cate_drop_down, show_qn_btn, del_button

    del_qn_frame = tk.Frame(content_frame)
    del_qn_frame.pack()

    def show_qns():
        global qn_drop_down
        mydb.reconnect() # To refresh the cursor buffer

        qn_menu = StringVar() # drop-down list of questions under selected category
        qn_menu.set("Select the question to delete")

        mycursor.execute(f"SELECT QUESTION FROM QUESTIONS WHERE CATE_NAME = '{cate_menu.get()}'")
        qns_lst = [i[0] for i in mycursor.fetchall()]

        qn_drop_down = OptionMenu(root, qn_menu, *qns_lst) # Create a dropdown menu for questions of selected category
        qn_drop_down.config(font=side_panel_font)
        qn_dd_list = root.nametowidget(qn_drop_down.menuname)  # Get menu widget.
        qn_dd_list.config(font=side_panel_font)
        qn_drop_down.place(x=450, y=530, width=850, height=40)


    cate_menu = tk.StringVar() # drop-down list of categories
    cate_menu.set("Select Question Category")     

    mycursor.execute("SELECT DISTINCT CATE_NAME FROM QUESTIONS")
    categories = [i[0] for i in mycursor.fetchall()]

    cate_drop_down = tk.OptionMenu(root, cate_menu, *categories) # Create a dropdown menu
    cate_drop_down.config(font=side_panel_font) # tkf.Font(family='Montserrat', size=15))
    cate_dd_list = root.nametowidget(cate_drop_down.menuname)  # Get menu widget.
    cate_dd_list.config(font=side_panel_font) # tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
    cate_drop_down.place(x=680, y=350, width=400, height=40)

    show_qn_btn = Button(root, text="Show Question",font=side_panel_font, command = show_qns) # add command function
    show_qn_btn.place(x=800, y=430, width=170, height=40)

    del_button = tk.Button(root, text="Delete Question",font=side_panel_font) # , command = delete_question) # add command function
    del_button.place(x=800, y=610, width=170, height=40)


##################### USER CONTROLS SECTION #############################

def add_user():
    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    user_controls()

    add_user_frame = tk.LabelFrame(content_frame, text="Add User Profile", font=admin_panel_item_font, bg='White')
    add_user_frame.pack(side="top")

    username_label = tk.Label(add_user_frame, text="Enter Username", font=side_panel_font, justify="left", bg='White')
    username_label.grid(row=1, column=0, sticky="w", padx=60)
    ent_user_title = tk.Entry(add_user_frame, borderwidth=5, width=50)
    ent_user_title.grid(row=2, column=0, sticky="w", padx=60)

    email_label = tk.Label(add_user_frame, text="Enter Email", font=side_panel_font, bg='White')
    email_label.grid(row=1, column=1, sticky="w", pady=15, padx=60)
    email_ent = tk.Entry(add_user_frame, borderwidth=5, width=50)
    email_ent.grid(row=2, column=1, sticky="w", padx=60)
    
    pass_label = tk.Label(add_user_frame, text="Enter Password", font=side_panel_font, bg='White')
    pass_label.grid(row=3, column=0, sticky="w", pady=15, padx=60)
    pass_ent = tk.Entry(add_user_frame, borderwidth=5, width=50)
    pass_ent.grid(row=4, column=0, sticky="w", padx=60)

    conf_pass_label = tk.Label(add_user_frame, text="Confirm Password", font=side_panel_font, bg='White')
    conf_pass_label.grid(row=3, column=1, sticky="w", pady=15, padx=60)
    conf_pass_ent = tk.Entry(add_user_frame, borderwidth=5, width=50)
    conf_pass_ent.grid(row=4, column=1, sticky="w", padx=60)

    clear_btn = tk.Button(add_user_frame, text="Clear", font="Montserrat, 25")
    clear_btn.grid(row=6,column=0,padx=20,pady=20)

    add_btn = tk.Button(add_user_frame, text="Add User", font="Montserrat, 25")
    add_btn.grid(row=6,column=1,padx=20,pady=20)


def update_user():

    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    user_controls()

    update_user_frame = tk.LabelFrame(content_frame, text="Update User Profile", font=admin_panel_item_font, bg='White')
    update_user_frame.pack(side="top")

    email_label = tk.Label(update_user_frame, text="E-mail", font=side_panel_font, bg='White')
    email_label.grid(row=1, column=0, sticky="w", pady=15, padx=60)
    email_ent = tk.Entry(update_user_frame, borderwidth=5, width=50)
    email_ent.grid(row=1, column=1, sticky="w", padx=60)

    username_label = tk.Label(update_user_frame, text="Username", font=side_panel_font, justify="left", bg='White')
    username_label.grid(row=2, column=0, sticky="w", padx=60)
    ent_user_title = tk.Entry(update_user_frame, borderwidth=5, width=50)
    ent_user_title.grid(row=2, column=1, sticky="w", padx=60)

    bio_label = tk.Label(update_user_frame, text="Biography", font=side_panel_font, justify="left", bg='White')
    bio_label.grid(row=3, column=0, sticky="w", pady=25, padx=60)
    ent_bio = tk.Entry(update_user_frame, borderwidth=5, width=50)
    ent_bio.place(x=275,y=120,height=75, width=310)

    change_btn = tk.Button(update_user_frame, text="Save Changes", font="Montserrat, 25")
    change_btn.grid(row=5,column=1,padx=90, pady=80)

def delete_user():

    for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()

    user_controls()

    delete_user_frame = tk.LabelFrame(content_frame, text="Delete User Profile", font=admin_panel_item_font, bg='White')
    delete_user_frame.pack(side="top")

    email_label = tk.Label(delete_user_frame, text="Enter Email", font=side_panel_font, bg='White')
    email_label.grid(row=1, column=0, sticky="w", pady=15, padx=60)
    email_ent = tk.Entry(delete_user_frame, borderwidth=5, width=50)
    email_ent.grid(row=1, column=1, sticky="w", padx=60)

    change_btn = tk.Button(delete_user_frame, text="Delete User", font="Montserrat, 25")
    change_btn.grid(row=3,column=1,padx=90, pady=80)











# admin_img = ImageTk.PhotoImage(Image.open("DBMS-Project/work files/Noyal/admin_white.png"))
admin_img = ImageTk.PhotoImage(Image.open("admin_white.png")) # Admin image, used in side panel.


# Side Pannel
side_panel = tk.Frame(root, bg=side_panel_bg,)
side_panel.pack(side="left", fill="y")

# Admin main icon label
admin_icon_label = tk.Label(side_panel, image=admin_img, bg=side_panel_bg)
admin_icon_label.pack(pady=35)

admin_dashboard_button = tk.Button(side_panel, text="Admin Dashboard", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=dashboard)
admin_dashboard_button.pack(padx=50)

question_controls_button = tk.Button(side_panel, text="Question Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=question_controls)
question_controls_button.pack(padx=50, pady=20)

user_controls_button = tk.Button(side_panel, text="User Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=user_controls)
user_controls_button.pack(padx=50)

"""
# WE CAN DO THIS IF WE GET TIME

user_reports_button = tk.Button(side_panel, text="User Reports", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg) # , command=user_reports)
user_reports_button.pack(padx=50, pady=20)

statistics_button = tk.Button(side_panel, text="Statistics", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg)# , command=statistics)
statistics_button.pack(padx=50, pady=20)
"""

# Content Frame
content_frame = tk.Frame(root, bg="white")
content_frame.pack(fill="both", expand="true")

dashboard()

root.bind('<Escape>', exit_window)
root.mainloop()