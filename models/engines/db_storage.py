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
    
    def search_movies(self, title=None, release_date=None, director=None, genre=None):
        query =  session.query(Movie)
        if title:
            query = query.filter(Movie.title.ilike(f'%{title}%'))
        if director:
            query = query.filter(Movie.director.ilike(f'%{director}%'))
        if genre:
            query = query.filter(Movie.genre.ilike(f'%{genre}%'))
        if release_date:
            query = query.filter(Movie.release_date == release_date)
        return query.all()

    def update_movies(self, movie):
        session.merge(movie)
        session.commit()

    def delete_movies(self, movie):
        session.delete(movie)
        session.commit()
