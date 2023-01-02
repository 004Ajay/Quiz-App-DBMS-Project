qn_menu = tk.StringVar() # drop-down list of questions under selected category
    qn_menu.set("Select the question to delete")

    mycursor.execute(f"SELECT QUESTION FROM QUESTIONS WHERE CATE_NAME = '{cate_menu.get()}'")
    qns_lst = [i[0] for i in mycursor.fetchall()]

    qn_drop_down = tk.OptionMenu(root, qn_menu, *qns_lst) # Create a dropdown menu for questions of selected category
    qn_drop_down.config(font=side_panel_font)
    qn_dd_list = root.nametowidget(qn_drop_down.menuname)  # Get menu widget.
    qn_dd_list.config(font=side_panel_font)
    qn_drop_down.place(x=580, y=430, width=380, height=40)