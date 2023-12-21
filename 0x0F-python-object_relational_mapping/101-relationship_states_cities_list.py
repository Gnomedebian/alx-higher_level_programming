#!/usr/bin/python3
"""lists State objects, City objects, contained in the database"""


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
    raw = session.query(State).all()
    for i in raw:
        print("{}: {}".format(i.id, i.name))
        for r in i.cities:
            print("    {}: {}".format(r.id, r.name))
    session.close()
