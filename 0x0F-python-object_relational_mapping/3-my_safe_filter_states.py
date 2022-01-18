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

    sub = ";"
    emoty = ""
    for x in filter_by:
        if x == sub:
            emoty = emoty[0:-1]
            break
        emoty += x
    # emoty = emoty[0:-1]
    # print(emoty)

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=passwd,
                         db=database)
    cur = db.cursor()
    cur.execute(
        ('SELECT * FROM states WHERE BINARY name = \'{}\' ORDER BY id ASC').
        format(emoty))
    result = cur.fetchall()

    cur.close()
    db.close()
    for x in result:
        print(x)
