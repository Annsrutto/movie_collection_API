
# Movie Collection API

Welcome to the Movie Collection API! This project empowers developers with a user-friendly and powerful way to access a vast amount of movie data. Whether you're building applications, websites, or simply have a passion for movies, this API provides a comprehensive resource to enrich your projects.


## Features

- Rich Movie Data: Access details like titles, descriptions, cast, crew, genres, release dates, and more.
- Efficient Search: Find movies quickly and easily using various filters and keywords.
- User-Friendly API Design: The RESTful API is well-documented and straightforward to integrate.
- Regular Updates: We strive to keep the data current and maintain a reliable API.


## API Reference

#### List all movies

```http
  GET /movies
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Add movie

```http
  POST /movies/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to add |

#### Update movies

```http
  PUT /movies/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to update |

#### Delete movies

```http
  DELETE /movies/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to delete |

## Authors

- [@annsrutto](https://www.github.com/Annsrutto)


- [@daviskoech](https://www.github.com/davykoch)


## Screenshots


<img width="830" alt="App screenshot" src="https://github.com/Annsrutto/movie_collection_API/assets/135266679/393ca09d-67ff-489b-a724-f307aa444d91">

## Usage/Examples

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

with app.app_context():
    db.create_all()

@app.route('/movies', methods=['GET'])
def get_all_movies():
    movies = Movie.query.all()
    movie_list = [movie.serialize() for movie in movies]
    return (movie_list)


## Contributing

We welcome contributions to this project! If you have improvements, bug fixes, or feature suggestions, feel free to create a pull request on this repository. Please follow these guidelines:

- Fork the repository.
- Create a new branch for your changes.
- Write clear and concise commit messages.
- Add unit tests for your contributions.
- Submit a pull request for review.

## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Python, Flask, MySQL

## Related

Here are some related projects

- [The Movie Database](https://www.themoviedb.org/)
- [ Letterboxd ](https://letterboxd.com/)


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)
License. Please refer to the LICENSE file for details.

