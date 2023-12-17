#!/usr/bin/python3
'''it takes in the name of a state as an argument and lists
all cities of that state'''

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    query = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = %s ORDER BY cities.id"
    arg = (sys.argv[4], )
    cursor = db.cursor()
    cursor.execute(query, arg)
    rows = cursor.fetchall()
    r = ""
    for row in rows:
        r += row[0] + ", "
    print(r[0:-2:])
    cursor.close()
    db.close()
