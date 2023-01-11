from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from db_connect import project_db


side_panel_bg = "#3F3F3F"
side_panel_font = "Montserrat, 15"
admin_panel_item_font= "Montserrat, 25"

mydb = project_db()
mycursor = mydb.cursor(buffered=True)

def admin_panel():
    root = tk.Tk()
    root.title("Admin")
    root.geometry("1920x1080")
    root.iconbitmap("images/Q.ico")

    def exit_window(e): root.destroy() # to exit window

    global admin_img # for protecting image from garbage collection (admin icon)

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


    ##################### ADMIN CONTROLS #####################
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

    def category_controls():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

        category_controls_label = tk.Label(content_frame, bg="white", text="Category Controls", font="Montserrat, 55")
        category_controls_label.pack(pady=30)

        category_controls_frame = tk.Frame(content_frame, bg="white")
        category_controls_frame.pack()

        add_category_button = tk.Button(category_controls_frame, bg="#F0F0F0", text="Add Category", padx=10, pady=5, font="Montserrat, 25",command=add_category)
        add_category_button.grid(row=3, column=0,padx=100, pady=50)
    
        delete_category_button = tk.Button(category_controls_frame, bg="#F0F0F0", text="Delete Category", padx=10, pady=5, font="Montserrat, 25",command=delete_category)
        delete_category_button.grid(row=3, column=3, padx=100, pady=50)     

    """
    # TO BE COMPLETED IF WE GET TIME

    def statistics():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()

    def user_reports():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame.
            widget.destroy()
    """


    ##################### CATEGORY CONTROLS SECTION #############################
    def add_category():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def add_cat():
            try:
                mycursor.execute(f'INSERT INTO CATEGORIES VALUES("{ent_cat_title.get()}", "{ent_cat_desc.get()}")')
                mydb.commit()
                mb.showinfo("Category Added", "Category added successfully")
                [widget.delete(0, 'end') for widget in add_cat_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mydb.rollback()
                mb.showinfo("Error", "Error adding category")

        category_controls()

        add_cat_frame = tk.LabelFrame(content_frame, text="Add Category", font=admin_panel_item_font, bg='White')
        add_cat_frame.pack(side="top")

        cat_label = tk.Label(add_cat_frame, text="Enter Category Name", font=side_panel_font, justify="left", bg='White')
        cat_label.grid(row=2, column=0, sticky="w", padx=60)
        ent_cat_title = tk.Entry(add_cat_frame, borderwidth=5, width=50)
        ent_cat_title.grid(row=2, column=1, sticky="w", padx=60)

        desc_label = tk.Label(add_cat_frame, text="Enter Category Description", font=side_panel_font, justify="left", bg='White')
        desc_label.grid(row=3, column=0, sticky="w", pady=25, padx=60)
        ent_cat_desc = tk.Entry(add_cat_frame, borderwidth=5, width=50)
        ent_cat_desc.place(x=275,y=120,height=75, width=310)

        cat_add_btn = tk.Button(add_cat_frame, text="Add Category", font="Montserrat, 25", command=add_cat)
        cat_add_btn.grid(row=5,column=1,padx=90, pady=80)

    def delete_category():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def del_cat():
            try:
                cat = ent_cat_title.get()
                
                mycursor.execute("SELECT CATEGORY_NAME FROM CATEGORIES")
                categories = [i[0].lower() for i in mycursor.fetchall()]
                if cat.lower() in categories:
                    mycursor.execute(f"DELETE FROM QUESTIONS WHERE CATE_NAME = '{ent_cat_title.get()}'")
                    mycursor.execute(f"DELETE FROM CATEGORIES WHERE CATEGORY_NAME = '{ent_cat_title.get()}'")
                    mydb.commit()
                    mb.showinfo("Category Deleted", "Category deleted successfully")
                    [widget.delete(0, 'end') for widget in del_cat_frame.winfo_children() if isinstance(widget, tk.Entry)]
                else:
                    mb.showinfo("Category not found", "No such category exist")
            except:
                mydb.rollback()
                mb.showinfo("Error", "Error deleting category")

        category_controls()

        del_cat_frame = tk.LabelFrame(content_frame, text="Delete Category", font=admin_panel_item_font, bg='White')
        del_cat_frame.pack(side="top")

        cat_label = tk.Label(del_cat_frame, text="Enter Category Name", font=side_panel_font, justify="left", bg='White')
        cat_label.grid(row=2, column=0, sticky="w", padx=60)
        ent_cat_title = tk.Entry(del_cat_frame, borderwidth=5, width=50)
        ent_cat_title.grid(row=2, column=1, sticky="w", padx=60)

        cat_add_btn = tk.Button(del_cat_frame, text="Delete Category", font="Montserrat, 25", command=del_cat)
        cat_add_btn.grid(row=5,column=1,padx=90, pady=80)

    ##################### QUESTION CONTROLS SECTION #############################
    def add_question():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def add_qn():
            try:
                mycursor.execute(f'INSERT INTO QUESTIONS VALUES(NULL,"{ent_qn_title.get()}","{opt_1_ent.get()}","{opt_2_ent.get()}","{opt_3_ent.get()}","{opt_4_ent.get()}","{crt_ans_ent.get()}","{qn_cate_ent.get()}");')
                mydb.commit()
                mb.showinfo("Question Added", "Question added successfully")
                [widget.delete(0, 'end') for widget in add_qn_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mydb.rollback()
                mb.showinfo("Error", "Error adding question")

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

        add_qn_btn = tk.Button(add_qn_frame, text="Add Question", font="Montserrat, 25", command=add_qn)
        add_qn_btn.grid(column=1, pady=30)


    def update_question():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def update_qn():
            """
            try:
                mycursor.execute(f'INSERT INTO QUESTIONS VALUES(NULL,"{ent_qn_title.get()}","{opt_1_ent.get()}","{opt_2_ent.get()}","{opt_3_ent.get()}","{opt_4_ent.get()}","{crt_ans_ent.get()}","{qn_cate_ent.get()}");')
                mydb.commit()
                mb.showinfo("Question Added", "Question added successfully")
                [widget.delete(0, 'end') for widget in update_qn_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mb.showinfo("Error", "Error updating question")
                mydb.rollback()
            """ 

        question_controls()

        update_qn_frame = tk.LabelFrame(content_frame, text="Update Question", font=admin_panel_item_font,bg='White')
        update_qn_frame.pack(side=TOP)

        qn_title_lbl = tk.Label(update_qn_frame, text="Edit Question title", font=side_panel_font, justify="left",bg='White')
        qn_title_lbl.grid(row=0, column=0, sticky="w", padx=40)

        ent_qn_title = tk.Entry(update_qn_frame, borderwidth=5, width=160)
        ent_qn_title.grid(row=1, column=0, columnspan=4, padx=60)

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

        update_qn_btn = tk.Button(update_qn_frame, text="Update Question", font="Montserrat, 25", command=update_qn)
        update_qn_btn.grid(column=1, pady=30)


    def delete_question():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def del_qn():
            try:
                mycursor.execute(f"SELECT Q_NO FROM QUESTIONS WHERE QUESTION = '{qn_menu.get()}'") # to get question number from question
                qn_no = mycursor.fetchall()[0][0] # to take question number from '[(33,)]' list & tuple
                mycursor.execute(f"DELETE FROM QUESTIONS WHERE Q_NO = {qn_no}") # deleting question using question number(primary key)
                mydb.commit()
                mb.showinfo("Question Deleted", "Question deleted successfully")
            except:
                mb.showinfo("Error", "Error deleting the question")
                mydb.rollback()    

        question_controls()

        del_qn_frame = tk.LabelFrame(content_frame,bg='White')
        del_qn_frame.pack(side=TOP,anchor=CENTER)

        def show_qns():
            mydb.reconnect() # To refresh the cursor buffer

            global qn_menu

            qn_menu = StringVar() # drop-down list of questions under selected category
            qn_menu.set("Select the question to delete")

            mycursor.execute(f"SELECT QUESTION FROM QUESTIONS WHERE CATE_NAME = '{cate_menu.get()}'")
            qns_lst = [i[0] for i in mycursor.fetchall()]

            qn_drop_down = OptionMenu(del_qn_frame, qn_menu, *qns_lst) # Create a dropdown menu for questions of selected category
            qn_drop_down.config(font=side_panel_font)
            qn_dd_list = root.nametowidget(qn_drop_down.menuname)  # Get menu widget.
            qn_dd_list.config(font=side_panel_font)
            qn_drop_down.grid(row=5,column=1,padx=20,pady=20)



        cate_menu = tk.StringVar() # drop-down list of categories
        cate_menu.set("Select Question Category")     

        mycursor.execute("SELECT DISTINCT CATE_NAME FROM QUESTIONS")
        categories = [i[0] for i in mycursor.fetchall()]

        cate_drop_down = tk.OptionMenu(del_qn_frame, cate_menu, *categories) # Create a dropdown menu
        cate_drop_down.config(font=side_panel_font,borderwidth=5, width=50) # tkf.Font(family='Montserrat', size=15))
        cate_dd_list = del_qn_frame.nametowidget(cate_drop_down.menuname)  # Get menu widget.
        cate_dd_list.config(font=side_panel_font) # tkf.Font(family='Montserrat', size=12))  # Set the dropdown menu's font
        cate_drop_down.grid(row=1,column=1,padx=20,pady=20)

        show_qn_btn = Button(del_qn_frame, text="Show Question",font=side_panel_font, command = show_qns) # add command function
        show_qn_btn.grid(row=3,column=1,padx=20,pady=20)

        del_button = tk.Button(del_qn_frame, text="Delete Question",font=side_panel_font, command=del_qn) # , command = delete_question) # add command function
        del_button.grid(row=7,column=1,padx=20,pady=20)

    ##################### USER CONTROLS SECTION #############################

    def add_user():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        def add_usr():
            try:
                mycursor.execute(f"INSERT INTO PLAYERS VALUES ('{ent_user_title.get()}', '{email_ent.get()}', '{pass_ent.get()}')") # to insert new user
                mydb.commit()
                mb.showinfo("User Added", "User added successfully")
                [widget.delete(0, 'end') for widget in add_user_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mb.showinfo("Error", "Error adding user")
                mydb.rollback()
        
        def clear(): [widget.delete(0, 'end') for widget in add_user_frame.winfo_children() if isinstance(widget, tk.Entry)]

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

        clear_btn = tk.Button(add_user_frame, text="Clear", font="Montserrat, 25", command=clear)
        clear_btn.grid(row=6,column=0,padx=20,pady=20)

        add_btn = tk.Button(add_user_frame, text="Add User", font="Montserrat, 25", command=add_usr)
        add_btn.grid(row=6,column=1,padx=20,pady=20)


    def update_user():
        for widget in content_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
            widget.destroy()

        """
        def update_usr():
            try:
                mycursor.execute(f"INSERT INTO PLAYERS VALUES ('{ent_user_title.get()}', '{email_ent.get()}', '{pass_ent.get()}')") # to insert new user
                mydb.commit()
                mb.showinfo("User Added", "User added successfully")
                [widget.delete(0, 'end') for widget in update_user_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mb.showinfo("Error", "Error adding user")
                mydb.rollback()
        """    

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

        def del_usr():
            try:
                mycursor.execute(f"DELETE FROM PLAYERS WHERE EMAIL = '{email_ent.get()}'") # to insert new user
                mydb.commit()
                mb.showinfo("User Deleted", "User deleted successfully")
                [widget.delete(0, 'end') for widget in delete_user_frame.winfo_children() if isinstance(widget, tk.Entry)]
            except:
                mb.showinfo("Error", "Error deleting user")
                mydb.rollback()    

        user_controls()

        delete_user_frame = tk.LabelFrame(content_frame, text="Delete User Profile", font=admin_panel_item_font, bg='White')
        delete_user_frame.pack(side="top")

        email_label = tk.Label(delete_user_frame, text="Enter Email", font=side_panel_font, bg='White')
        email_label.grid(row=1, column=0, sticky="w", pady=15, padx=60)
        email_ent = tk.Entry(delete_user_frame, borderwidth=5, width=50)
        email_ent.grid(row=1, column=1, sticky="w", padx=60)

        del_btn = tk.Button(delete_user_frame, text="Delete User", font="Montserrat, 25", command=del_usr)
        del_btn.grid(row=3,column=1,padx=90, pady=80)

    # admin_img = ImageTk.PhotoImage(Image.open("DBMS-Project/work files/Noyal/admin_white.png"))
    admin_img = ImageTk.PhotoImage(Image.open("images/admin_white.png")) # Admin image, used in side panel.
    
    # Side Pannel
    side_panel = tk.Frame(root, bg=side_panel_bg,)
    side_panel.pack(side="left", fill="y")

    # Admin main icon label
    admin_icon_label = tk.Label(side_panel, image=admin_img, bg=side_panel_bg)
    admin_icon_label.pack(pady=35)

    admin_dashboard_button = tk.Button(side_panel, text="Admin Dashboard", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=dashboard)
    admin_dashboard_button.pack(padx=50)

    category_controls_button = tk.Button(side_panel, text="Category Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=category_controls)
    category_controls_button.pack(padx=52)

    question_controls_button = tk.Button(side_panel, text="Question Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=question_controls)
    question_controls_button.pack(padx=60, pady=20)

    user_controls_button = tk.Button(side_panel, text="User Controls", font=side_panel_font, bg=side_panel_bg, foreground="white", relief="flat", activebackground=side_panel_bg, command=user_controls)
    user_controls_button.pack(padx=65)

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