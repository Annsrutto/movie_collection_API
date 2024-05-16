import requests
from app import app
from datetime import datetime
from models.movie import Movie, db

TMDB_API_KEY = '928a86fa32cd492578b2921001b702a1'
TMDB_ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MjhhODZmYTMyY2Q0OTI1NzhiMjkyMTAwMWI3MDJhMSIsInN1YiI6IjY2MTljZGY3OGMzMTU5MDE5M2MwZTBjYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJ'

def fetch_movies_from_tmdb():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&access_token={TMDB_ACCESS_TOKEN}"
    response = requests.get(url)
    data = response.json()
    movies = data.get('results', [])
    return movies

def populate_database():
    movies = fetch_movies_from_tmdb()

    for movie_data in movies:
        title = movie_data['title']
        # release_date = datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date() if movie_data['release_date'] else None

        new_movie = Movie(title=title)
        db.session.add(new_movie)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        populate_database()