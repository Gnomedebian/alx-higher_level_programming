#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py.
creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""


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
    new_State = State(name="California")
    new_State.cities = [City(name="San Francisco")]
    r = session.add(new_State)
    session.commit()
    session.close()
