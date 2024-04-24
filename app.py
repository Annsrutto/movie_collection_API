#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import Column, Integer, String, Date, Float, Text, ForeignKey


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

class Movie(db.Model):
    """Contains the class Movie which represents a movie."""
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    rating = db.Column(db.Float)
    duration_minutes = db.Column(db.Integer)
    overview = db.Column(db.Text)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))


class Genre(db.Model):
    """Genre model represents a genre of movies."""
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    movies = relationship('Movie', backref='genre')


class Director(db.Model):
    """Director model represents the director of movies."""
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    movies = relationship('Movie', backref='director')


if '__name__' == '__main__':
    app.run(debug=True)
