import mysql.connector

try:
    db = mysql.connector.connect(
        host = 'localhost',
        database = 'school',
        user = 'root',
        password = ''
    )

    if db.is_connected():
        cursor = db.cursor()
        sql = """INSERT INTO employee(first_name,last_name,age,sex,income)
        values(%s,%s,%s,%s,%s)"""
        val = ("Ayesh", "Chathuranga", 21, "M", 4000)
        cursor.execute(sql,val)
        print(cursor.rowcount, "record successfully inserted")
        db.commit()

except Exception as e:
    print("Error while conneting to MySQL ", e)

finally:
    if db.is_connected():
        db.close()
        cursor.close()