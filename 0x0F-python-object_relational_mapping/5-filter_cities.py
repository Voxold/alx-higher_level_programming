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

    query = f"""SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = '{argv[4]}' ORDER BY cities.id"""

    mycursor.execute(query)

    result = mycursor.fetchall()
    if result:
        for row in result[:-1]:
            for i in row:
                print(i, end=", ")
        print(result[-1][0])
    else:
        print()

    mycursor.close()
    mydb.close()
