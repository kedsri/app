import mysql.connector

mydb = mysql.connector.connect(
host = "localhost",
user = "yourusername",
password = "your_password"
)

print(mydb)