#!/usr/bin/python3
"""injection safe method to lists items within database hbtn_0e_0_usa 
    based off given argument"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host='localhost', port=3306,
                        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)