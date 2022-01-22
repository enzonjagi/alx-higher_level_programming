#!/usr/bin/python3
'''Script that lists all State objects from hbtn_0e_6_usa'''


if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
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

        # Add a State(name='Louisiana') to the db
        louisiana = State(name='Louisiana')
        session.add(louisiana)
        session.commit()
        # print(louisiana.id)

        # Print louisiana's id
        for state in session.query(State).filter(State.id == 2):
            if state:
                state.name = 'New Mexico'
                session.commit()
