"""Create and connect to the book collection SQLite database."""

import sqlite3
from contextlib import closing
from pathlib import Path


DATABASE_PATH = Path(__file__).with_name("book_collection.db")


def get_connection():
    """Open a database connection with foreign-key checks enabled."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    """Create the author and book tables if they do not already exist."""
    with closing(get_connection()) as connection:
        with connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS author (
                    Author_id INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS book (
                    Book_id INTEGER PRIMARY KEY,
                    Title TEXT NOT NULL,
                    Author_id INTEGER,
                    Year INTEGER,
                    Rating INTEGER CHECK (Rating BETWEEN 1 AND 5),
                    Read_it_or_not BOOLEAN,
                    FOREIGN KEY (Author_id) REFERENCES author (Author_id)
                )
                """
            )


if __name__ == "__main__":
    initialize_database()
    print(f"Database initialized: {DATABASE_PATH}")