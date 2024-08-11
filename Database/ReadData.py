from tkinter import E
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        database="school",
        user="root",
        password=""
    )

    if db.is_connected():
        cursor = db.cursor()
        sql = "SELECT * FROM employee WHERE age = 21"
        cursor.execute(sql)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print("\nPrint each row")
        for row in records:
            print("Firstname = ", row[0])
            print("Lastname = ", row[1])
            print("Age = ", row[2])
            print("Income = ", row[3], "\n")

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()
