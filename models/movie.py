#!/usr/bin/python3
"""This module contains the class models for the movie collection API."""

from datetime import datetime
from sqlalchelmy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, Float, Text, ForeignKey

class Movie(db.Models):
    """Contains the class Movie."""
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_date = db.Column(db.Date)
    rating = db.Column(db.Float)
    duration_minutes = db.Column(db.Integer)
    overview = db.Column(db.Text)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
