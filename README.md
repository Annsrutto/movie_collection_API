
# Movie Collection API

The Movie Collection API was developed as a project to showcase RESTful API development skills and to provide a backend solution for managing movie data. It can be integrated with various frontend applications or used as a standalone API for movie enthusiasts or professionals in the entertainment industry. This project empowers developers with a user-friendly and powerful way to access a vast amount of movie data. Whether you're building applications, websites, or simply have a passion for movies, this API provides a comprehensive resource to enrich your projects.


## Installation

To run the Movie Collection API locally, follow these steps:

1. Clone the repository:
```bash
  git clone https://github.com/your-username/movie_collection_api.git
```

2. Navigate to the project directory:
```bash
  cd movie_collection_api
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

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/anns-rutto-22397b217)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/davis-koech-22145a131)


## Usage

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


## Licensing

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)
License. Please refer to the LICENSE file for details.


## Screenshots

<img width="830" alt="App screenshot" src="https://github.com/Annsrutto/movie_collection_API/assets/135266679/393ca09d-67ff-489b-a724-f307aa444d91">
