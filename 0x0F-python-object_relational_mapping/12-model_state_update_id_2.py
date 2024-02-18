#!/usr/bin/python3
"""
changes the name of a State object
from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ), pool_pre_ping=True)
    session = Session(engine)
    row = session.query(State).filter_by(id=2).first()
    row.name = "New Mexico"
    row = session.add(row)
    session.commit()
    session.close()
