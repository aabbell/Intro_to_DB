import mysql.connector
import errorcode

try:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "abel",
    password = "trust2332",
    database = ""
)

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except:
    mysql.connector.Error as err:
    print(f"Error:{err}")

finally:
    if 'cursor' in locals():
        cursor.close()
