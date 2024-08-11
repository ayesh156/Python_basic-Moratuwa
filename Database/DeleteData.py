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
        sql = "DELETE FROM employee WHERE income=8000"
        cursor.execute(sql)
        print(cursor.rowcount, "record successfully deleted!")
        db.commit()

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()


