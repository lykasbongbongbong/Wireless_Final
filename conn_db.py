#!/usr/bin/python3
import pymysql
db = pymysql.connect(host = "localhost",port = 3306, user = "andy", password = "123456", db="class")
cursor = db.cursor()
cursor.execute("SELECT * FROM `students`")
data = cursor.fetchall()
print(data)
db.close()



