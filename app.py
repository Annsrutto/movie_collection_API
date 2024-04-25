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
    try:
        data = request.json
        title = data.get('title')
        release_date = data.get('release_date', None)
        director_id = data.get('director_id', None)
        genre = data.get('genre', None)

        if not title or not release_date or not director_id or not genre:
            return jsonify('error': 'Title, release_date, director_id and genre required')

        new_movie = Movie(title=title, release_date=release_date, director_id=director_id, genre=genre)
        
        new_movie.save()

        response_data = {
            'message' : 'movie added successfully'
            'movie' : new_movie.serialize()
        }
        return jsonify(response_data), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if '__name__' == '__main__':
    app.run(debug=True)
    