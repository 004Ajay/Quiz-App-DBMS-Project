    for widget in add_question_frame.winfo_children(): # To delete alredy exisiting widgets in content_frame. # Not working for some reason, try disabling the button.
        widget.destroy()