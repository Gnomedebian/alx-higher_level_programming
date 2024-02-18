#!/usr/bin/python3
'''file that contains the class definition of a State and an instance Base'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    state class

    attributes:
    id: id, primary_key
    name: string representing the name of the state
    '''
    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
