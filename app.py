#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from models import movie, director, genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
