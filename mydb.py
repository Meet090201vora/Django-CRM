import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password@123Meet!'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All done!")