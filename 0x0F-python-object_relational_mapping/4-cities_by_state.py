#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import re
from sys import argv

if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
    )
    mycursor = mydb.cursor()

    query = """SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id"""

    mycursor.execute(query)

    result = mycursor.fetchall()
    for row in result:
        print(row)

    mycursor.close()
    mydb.close()
