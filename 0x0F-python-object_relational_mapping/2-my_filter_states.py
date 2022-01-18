#!/usr/bin/python3
'''Getting all values from database.table
where name provided as user input
order_by table.id
'''


if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    filter_by = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=passwd,
                         db=database)
    cur = db.cursor()
    cur.execute(
        'SELECT * FROM states WHERE name = {} ORDER BY id', format(filter_by))
    result = cur.fetchall()

    cur.close()
    db.close()
    for x in result:
        print(x)
