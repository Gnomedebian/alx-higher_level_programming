#!/usr/bin/python3
'''script take 4 arguments'''

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
    query = "SELECT * FROM states WHERE BINARY \
        name LIKE %s ORDER BY id ASC"
    arg = (sys.argv[4],)
    cursor = db.cursor()
    cursor.execute(query, arg)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
