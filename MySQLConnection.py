import mysql.connector as myDB

# Create the connection object
mydb = myDB.connect(host="localhost", user="root", passwd="1234", database="telusko")

# printing the connection object
print(mydb)

myCursor = mydb.cursor()
myCursor.execute("select * from student")

result = myCursor.fetchall()

for i in result:
    print(i)
