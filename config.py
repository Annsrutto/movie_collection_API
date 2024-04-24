#!/usr/bin/python3
"""this contains configuration for connecting to MySQL Database."""

DB_USERNAME = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_SERVER = 'localhost'  # Change to your MySQL server address
DB_NAME = 'your_db_name'

SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
