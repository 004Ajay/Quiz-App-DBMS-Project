import mysql.connector
import tkinter as tk

# Connect to the database and execute the query
mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')

mycursor = mydb.cursor(buffered=True)
mycursor.execute("SELECT * FROM players")

# Retrieve the query results
results = mycursor.fetchall()

# Get the column names
column_names = [column[0] for column in mycursor.description]

# Create the Tkinter root and frame
root = tk.Tk()
root.geometry('1920x1080')
frame = tk.Frame(root)
frame.place(x=400, y= 350)
# Create a label for each column and place it in the frame
labels = []
for i, column_name in enumerate(column_names):
    label = tk.Label(frame, text=column_name)
    label.grid(row=0, column=i)
    labels.append(label)

# Create a label for each row and place it in the frame
for i, row in enumerate(results):
    for j, col in enumerate(row):
        label = tk.Label(frame, text=col)
        label.grid(row=i+1, column=j)
        labels.append(label)

# Place the frame on the root

# Run the Tkinter event loop
root.mainloop()