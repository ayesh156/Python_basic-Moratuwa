import mysql.connector

try:
    db = mysql.connector.connect(
        host='localhost',
        database='school',
        user='root',
        password=''
    )

    if db.is_connected():
        cursor = db.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("You're connected to database: %s" % record)

except Exception as e:
    print("Error while connecting to MySQL", e)

finally:
    if db.is_connected():
        db.close()
        cursor.close()
        print("MySQL connection is closeed")