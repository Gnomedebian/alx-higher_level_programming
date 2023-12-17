#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(host='localhost',
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM hbtn_0e_0_usa"
               "ORDER BY states.id ASC")
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print(col)
cursor.close()
db.close()
