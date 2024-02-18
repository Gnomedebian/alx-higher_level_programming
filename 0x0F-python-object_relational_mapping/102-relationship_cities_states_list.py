#!/usr/bin/python3
"""lists all City objects from database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            ), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    raw = session.query(City).all()
    for i in raw:
        print("{}: {} -> {}".format(i.id, i.name, i.state.name))
    session.close()
