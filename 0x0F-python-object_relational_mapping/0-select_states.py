#!/usr/bin/python3
'''Getting all values from database.table
order_by table.id
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=passwd,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    result = cur.fetchall()

    for x in result:
        print(x)
