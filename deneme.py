import mysql.connector
connection = mysql.connector.connect(user = "root", database = "Bank", password = "Batman10")
cursor = connection.cursor()

testQuery = ("SELECT * FROM Users")

testQuery2=("select name, Deadline from Assignments where subject=\"Math\";")
cursor.execute("SET SQL_SAFE_UPDATES = 0;")
cursor.execute(testQuery)
for item in cursor:
    print(item)

cursor.close()
connection.close()