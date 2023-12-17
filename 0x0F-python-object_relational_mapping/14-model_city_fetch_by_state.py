#!/usr/bin/python3
"""
deletes all State objects with name containing
the letter a from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ), pool_pre_ping=True)
    session = Session(engine)
    row = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for C, i in row:
        print("{}: ({}) {}".format(i.name, C.id, C.name))
    session.commit()
    session.close()
