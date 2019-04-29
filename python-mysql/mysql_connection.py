import pymysql.cursors
import pandas as pd

# Connect to the database.
connection = pymysql.connect(host='labticvi2019.cevummruy0nm.us-east-2.rds.amazonaws.com',
                             user='laboratorio',
                             password='labtic2019',
                             db='employees',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:

    with connection.cursor() as cursor:

        # SQL
        sql = "SELECT * FROM employees"

        # Execute query.
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        df = pd.DataFrame(cursor)
        print(df)

        for row in cursor:
            print(row)

finally:
    # Close connection.
    connection.close()