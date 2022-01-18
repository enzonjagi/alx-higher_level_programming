#!/usr/bin/python3
'''contains the state class definition'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import decalarative_base

Base = declarative_base()


class State(Base):
    '''State class Contains the definition of the State Table'''
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, nullable=False,
        autoincrement=True, unique=True)
    name = Column(
        String(128), nullable=False)
