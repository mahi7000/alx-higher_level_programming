#!/usr/bin/python3
""" contains class definition of a State """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State table """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
