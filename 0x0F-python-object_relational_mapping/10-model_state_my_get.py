#!/usr/bin/python3
'''Script that lists all State objects from hbtn_0e_6_usa'''


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    # check if arguments exist then work, if not, do nothing
    if sys.argv[4] is not None:
        uname = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]
        search = sys.argv[4]

        # get rid of SQL injection
        clean = ""
        for char in search:
            if char == ' ':
                clean = clean[0:-1]
            clean += char
        # create the connection to the database
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.
            format(uname, pwd, db),
            connect_args=dict(host="localhost", port=3306)
        )
        Base.metadata.create_all(engine)

        # create a session and bind it to engine
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query db.table to get the states details
        se = session.query(State).filter(State.name.like(clean)).first()
        if se:
            print('{}'.format(se.id))
        else:
            print('Not found')
