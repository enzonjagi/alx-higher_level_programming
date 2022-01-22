#!/usr/bin/python3
'''Queries the cities table in the DB'''


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker

    # check if arguments exist then work, if not, do nothing
    if sys.argv[3] is not None:
        uname = sys.argv[1]
        pwd = sys.argv[2]
        db = sys.argv[3]

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

        # Query Time: prints all City objects including state_id
        q = session.query(City, State).filter(
                           City.state_id == State.id
                           ).order_by(City.id).all()

        for x in q:
            print('{}: ({}) {}'.format(x[1].name, x[0].id, x[0].name))

        session.close()
        engine.dispose()
