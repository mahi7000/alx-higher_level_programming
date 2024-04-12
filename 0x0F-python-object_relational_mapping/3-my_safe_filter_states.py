#!/usr/bin/python3
""" displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument """
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    cursor.execute(query, (search,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
