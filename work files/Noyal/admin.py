import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Admin")
root.geometry("1920x1080")
root.iconbitmap("./Assets/Q.ico")

# Admin image
admin_img = ImageTk.PhotoImage(Image.open("D:/Programming/Python/Project/Assets/admin-settings.png"))

# Side Pannel
side_panel = tk.Frame(root, bg="black")
side_panel.pack(anchor="w", fill="y", expand="true")

# Admin main icon label
admin_icon_label = tk.Label(side_panel, image=admin_img)
admin_icon_label.pack(padx=50)

admin_icon_label2 = tk.Label(side_panel, text="HI")
admin_icon_label2.pack()

root.mainloop()