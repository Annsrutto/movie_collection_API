#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

from flask import Flask, request, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError
from models.movie import Movie, db
from models.genre import Genre

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()


# the endpoint url and method for adding movies
@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    movie_list = [serialize_movie(movie) for movie in movies]
    return jsonify(movie_list)


@app.route('/')
def index():
    # Assuming you have some movies data to pass to the template
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)



@app.route('/movies', methods=['POST'])
def add_movies():
    try:
        data = request.json
        title = data.get('title')
        release_date = data.get('release_date', None)
        # director = data.get('director', None)
        genre = data.get('genre', None)

        required_fields = ['title', 'genre', 'release_date']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing data required'}), 400

        new_movie = Movie(title=title, release_date=release_date, genre=genre)

        new_movie.save()

        response_data = {
            'message': 'movie added successfully',
            'movie': new_movie.serialize()
        }
        return jsonify(response_data), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/search', methods=['GET'])
def search_movies():
    title = request.args.get('title')
    release_date = request.args.get('release_date')
    # director = request.args.get('director')
    genre = request.args.get('genre')

    query = Movie.query
    if title:
        query = query.filter(Movie.title.ilike(f'%{title}%'))
    # if director:
        # query = query.filter(Movie.director.ilike(f'%{director}%'))
    if genre:
        query = query.filter(Movie.genre.ilike(f'%{genre}%'))
    if release_date:
        query = query.filter(Movie.release_date == release_date)

    movies = query.all()

    if movies:
        movie_list = [serialize_movie(movie) for movie in movies]
        return jsonify({'movie': movie_list}), 200
    else:
        return jsonify({'message': 'No movie found matching search criteria'}), 200

# PUT /movies/<id> endpoint to update movie details
@app.route('/movies/<int:movie_id>', methods=['PUT'])
def update_movie(movie_id):
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400

        required_fields = ['title', 'genre', 'release_date']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing data required'}), 400

        movie = Movie.query.get(movie_id)
        if not movie:
            return jsonify({'error': 'Movie not found'}), 404

        movie.title = data['title']
        # movie.director = data['director']
        movie.genre = data['genre']
        movie.release_date = data['release_date']

        db.session.commit()

        response = make_response(jsonify({'message': 'Movie updated successfully'}), 200)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Location'] = f'/movies/{movie_id}'
        return response

    except DatabaseError:
        return jsonify({'error': 'Database error occurred'}), 500


@app.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    # Check if the movie with the provided ID exists
    movie = Movie.query.get(id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404

    try:
        # Soft delete the movie by marking it as deleted
        movie.deleted = True
        db.session.commit()
        return jsonify({'message': 'Movie deleted successfully'}), 204
    except Exception as e:
        # Handle database errors
        return jsonify({'message': 'Failed to delete movie', 'error': str(e)}), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
