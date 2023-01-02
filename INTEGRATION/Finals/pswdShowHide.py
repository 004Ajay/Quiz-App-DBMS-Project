##########################  Password Show/Hide Functionality  ##########################

from tkinter import *

def pswd_show(rt, spwd, img, x_axis, y_axis): # rt - root
    def show(): spwd.config(show="") # showing password
    def hide(): spwd.config(show="*") # hiding password
    pw_Show_Btn = Button(rt, image=img, bd=0, bg="White")
    pw_Show_Btn.place(x=x_axis, y=y_axis, width=35, height=25)
    pw_Show_Btn.bind("<ButtonPress>", lambda event:show())
    pw_Show_Btn.bind("<ButtonRelease>", lambda event:hide())