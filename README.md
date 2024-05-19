
# Movie Collection API

Welcome to the Movie Collection API! This project empowers developers with a user-friendly and powerful way to access a vast amount of movie data. Whether you're building applications, websites, or simply have a passion for movies, this API provides a comprehensive resource to enrich your projects.


## Features

- Rich Movie Data: Access details like titles, descriptions, cast, crew, genres, release dates, and more.
- Efficient Search: Find movies quickly and easily using various filters and keywords.
- User-Friendly API Design: The RESTful API is well-documented and straightforward to integrate.
- Regular Updates: We strive to keep the data current and maintain a reliable API.


## Installation

To run the Movie Collection API locally, follow these steps:

1. Clone the repository:
```bash
  git clone https://github.com/your-username/movie-collection-api.git
```

2. Navigate to the project directory:
```bash
  cd movie-collection-api
```

3. Create and activate a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

4. Set up the database:
```bash
flask db upgrade
```

5. Run the application:
```bash
flask run
```

The API should now be running at http://localhost:5000/.


## Authors

- [@annsrutto](https://www.github.com/Annsrutto)


- [@daviskoech](https://www.github.com/davykoch)


## Usage/Examples

The Movie Collection API provides the following endpoints:

- **GET** /movies: Retrieve a list of all movies
- **POST** /movies: Create a new movie
- **GET** /movies/<id>: Retrieve a specific movie by ID
- **PUT** /movies/<id>: Update a movie by ID
- **DELETE** /movies/<id>: Delete a movie by ID
- **GET** /search: Search and filter movies by title, genre, or release date


<img width="500" alt="Movie-API-Code_Snippet" src="https://github.com/Annsrutto/movie_collection_API/assets/135266679/6b0efda4-73ca-41b1-96b2-d483f7c027be">



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

## Related Projects

Here are some related projects

- [The Movie Database](https://www.themoviedb.org/)
- [ Letterboxd ](https://letterboxd.com/)


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)
License. Please refer to the LICENSE file for details.


## Screenshots

<img width="830" alt="App screenshot" src="https://github.com/Annsrutto/movie_collection_API/assets/135266679/393ca09d-67ff-489b-a724-f307aa444d91">
