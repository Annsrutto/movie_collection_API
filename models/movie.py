#!/usr/bin/python3
"""This module contains the class models for the movie collection API."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Float, Text, ForeignKey

db = SQLAlchemy()


class Movie(db.Model):
    """Contains the class Movie which represents a movie."""
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date)
    rating = db.Column(db.Float)
    duration_minutes = db.Column(db.Integer)
    overview = db.Column(db.Text)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}')>"
