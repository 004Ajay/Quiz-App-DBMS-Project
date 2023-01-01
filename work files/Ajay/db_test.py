import mysql.connector
import random

mydb = mysql.connector.connect( # connecting to database
    host="localhost",
    user="root",
    passwd="1234",
    database="project",
    auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

cate = mycursor.execute("SELECT DISTINCT CATE FROM QUESTIONS")
cats = [i[0] for i in mycursor.fetchall()]
print(cats)

sel_cats = random.choice(cats)
print(sel_cats)

mydb.reconnect()

cate_qns = mycursor.execute(f"SELECT QN FROM QUESTIONS WHERE CATE = '{sel_cats}'")

caats = (i[0] for i in mycursor.fetchall())
print(*tuple(caats))