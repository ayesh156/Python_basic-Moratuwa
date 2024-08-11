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
        sql = """INSERT INTO employee(firstname,lastname,age,income)
        values(%s,%s,%s,%s)"""
        val = [("Ayesh", "Chathuranga", 21, 4000),
        ("Thisara", "Lakshan", 21, 5000),
        ("Eshara", "Ranaveera", 21, 5000)]
        cursor.executemany(sql,val)
        print(cursor.rowcount, "record successfully created")
        db.commit()

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()