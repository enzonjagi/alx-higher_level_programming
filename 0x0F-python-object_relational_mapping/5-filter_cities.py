#!/usr/bin/python3
'''Getting all values from database.table order_by table.id
Should print the Cities of a state
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

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=passwd,
                         db=database)
    cur = db.cursor()
    cur.execute(
        'SELECT c.name FROM cities c INNER JOIN states s ' +
        'ON s.id = c.state_id WHERE ' +
        'BINARY s.name = %s' +
        'ORDER BY c.id ASC;', [emoty])
    result = cur.fetchall()

    cur.close()
    db.close()
    print(', '.join(map(lambda char: char[0], result)))
