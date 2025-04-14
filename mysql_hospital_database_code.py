import mysql.connector
Mydb=mysql.connector.connect(host="localhost",user="root",passwd="Bharat@123")
mycursor=Mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS hospital")
