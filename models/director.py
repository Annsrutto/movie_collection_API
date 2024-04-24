#!/usr/bin/python3
"""This module contains the class models for the movie collection API."""

from datetime import datetime
from sqlalchelmy.orm import relationship
from sqlalchemy import Column, Integer, String
from models import db


class Director(db.Model):
    """Director model represents the director of movies.""""
    __tablename__ = 'directors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    movies = relationship('Movie', backref='director')
