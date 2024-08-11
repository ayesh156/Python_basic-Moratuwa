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
        sql = """CREATE TABLE employee(
            firstname CHAR(20) NOT NULL,
            lastname CHAR(20),
            age int,
            income float)"""
        cursor.execute(sql)
        print("Table successfully created!")

except Exception as e:
    print("Error while connecting to MySQL ", e)

finally:
    db.close()
    cursor.close()