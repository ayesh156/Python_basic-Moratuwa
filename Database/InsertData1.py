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
        sql = """INSERT INTO employee(first_name,last_name,age,sex,income)
        values('Ayesh','Chathuranga',21,'M',2000)"""
        cursor.execute(sql)
        print("record successfully inserted")
        db.commit()
        print(cursor.rowcount," record inserted")

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    if db.is_connected():
        db.close()
        cursor.close()