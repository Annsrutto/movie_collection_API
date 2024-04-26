#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

from flask import Flask
from config import SQLALCHEMY_DATABASE_URI
from models import movie, director, genre

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# the endpoint url and method for adding movies
@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    movie_list = [serialize_movie(movie) for movie in movies]
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
            return jsonify({'error' : 'Title, release_date, director_id and genre required'})

        new_movie = Movie(title=title, release_date=release_date, director_id=director_id, genre=genre)
        
        new_movie.save()

        response_data = {
            'message' : 'movie added successfully',
            'movie' : new_movie.serialize()
        }
        return jsonify(response_data), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/search', methods=['GET'])
def search_movies():
    title = request.args.get('title')
    release_date = request.args.get('release_date')
    director = request.args.get('director')
    genre = request.args.get('genre')

    query = Movie.query
    if title:
        query = query.filter(Movie.title.ilike(f'%{title}%'))
    if director:
        query = query.filter(Movie.director.ilike(f'%{director}%'))
    if genre:
        query = query.filter(Movie.genre.ilike(f'%{genre}%'))
    if release_date:
        query = query.filter(Movie.release_date == release_date)
    
    movies = query.all()

    if movies:
        movie_list = [serialize_movie(movie) for movie in movies]
        return jsonify({'movie': movie_list}), 200
    else:
        return jsonify({'message':'No movie found matching search criteria'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    