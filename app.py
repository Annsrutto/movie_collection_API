#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from models import db, movie, director, genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# the endpoint url and method for adding movies
@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    movie_list = [{'id' : movie.id, 'title' : movie.title, 'genre' : movie.genre} for movie in movies]
    return jsonify(movie_list)

@app.route('/movies', methods=['POST'])
def add_movies():
    
