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
        sql = "UPDATE employee SET income=8000 WHERE lastname='Lakshan'"
        cursor.execute(sql)
        print(cursor.rowcount, "record successfully updated!")
        db.commit()

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()