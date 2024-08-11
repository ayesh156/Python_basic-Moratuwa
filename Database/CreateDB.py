import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if db.is_connected():
        cursor = db.cursor()
        sql = "CREATE DATABASE school"
        cursor.execute(sql)
        print("Database successfully created!")

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()


