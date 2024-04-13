#!/usr/bin/python3
""" lists all cities of a state """
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

    query = """
    SELECT cities.name
    FROM cities
    LEFT JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (search,))

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    conn.close()
