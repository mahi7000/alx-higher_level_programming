#!/usr/bin/python3
""" prints all cities """
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(
            City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
