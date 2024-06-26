#!/usr/bin/python3
"""This module contains the class models for the movie collection API."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

db = SQLAlchemy()


class Genre(db.Model):
    """Genre model represents a genre of movies."""
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    movies = relationship('Movie', backref='genre')
