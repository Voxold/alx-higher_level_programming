#!/usr/bin/python3
"""MySQLdb Module"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY ID ASC")

    result = mycursor.fetchall()
    for row in result:
        print(row)
    mycursor.close()
    mydb.close()
