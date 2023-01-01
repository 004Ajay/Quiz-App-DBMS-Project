from tkinter import *
import mysql.connector


mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor(buffered=True)

mycursor.execute("select * from players")
res = mycursor.fetchall()
# print(res)

zero = [i[0] for i in res]
one = [i[1] for i in res]
two = [i[2] for i in res]
print(zero)
print(one)
print(two)




# my_conn = mydb.cursor()
# ####### end of connection ####
# my_conn.execute("SELECT * FROM PLAYERS")
# print(my_conn.fetchall())