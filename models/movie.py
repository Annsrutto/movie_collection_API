#!/usr/bin/python3
"""This module contains the class models for the movie collection API."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship, validates
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey

db = SQLAlchemy()


class Movie(db.Model):
    """Contains the class Movie which represents a movie."""
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)
    # director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    
    # director = relationship("Director", back_populates="movies")
    

    def __init__(self, title, release_date=None):
        self.id = None
        self.title = title
        # self.release_date = release_date
        # self.director = director
        # self.genre_id = genre_id

    def set_id(self, id):
        self.id = id

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    
    def serialize(movie):
        return {
            'id' : movie.id,
            'title' : movie.title,
            # 'release_date' : str(self.release_date),
           # 'director': self.director.serialize() if self.director else None,
            # 'genre' : self.genre
        }

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Title is required")
        return title

    @validates('release_date')
    def validate_release_date(self, key, release_date):
        try:
            datetime.strptime(release_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid format")
        return release_date

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}')>"
