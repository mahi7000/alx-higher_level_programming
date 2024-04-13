#!/usr/bin/python3
""" create a city table """
from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """City table"""
    __tablename__ = "cities"

    id = Column(Integer, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
