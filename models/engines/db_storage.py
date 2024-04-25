#!/usr/bin/python3
"""This is the database storage class for Movie Collection API"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:///movies.db')

Session = sessionmaker(bind=engine)
session = Session()

class DatabaseHandler:
    def add_movies(self, movie)
    try:
        session.add(movie)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise e
    
