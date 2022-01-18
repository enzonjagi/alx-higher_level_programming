#!/usr/bin/python3
'''State table model
a python file that contains the class definition of a State
and an instance Base = declarative_base()
'''


if __name__ == '__main__':
    import sqlalchemy
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.declarative import decalarative_base

    Base = declarative_base()

    class State(Base):
        '''State model
        Contains the definition of the State Table
        as seen below
        '''
        __tablename__ = 'states'

        id = Column(
            Integer, primary_key=True, nullable=False)
        name = Column(
            String(128), nullable=False)
