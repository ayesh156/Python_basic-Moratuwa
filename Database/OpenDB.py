import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    if db.is_connected():
        cursor = db.cursor()
        cursor.execute("select version()")
        data = cursor.fetchone()
        print("Database version: %s " % data)

except Exception as e:
    print("Error while connecting to MYSQL ", e)

finally:
    db.close()
    cursor.close()
