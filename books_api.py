"""Simple create, read, and update functions for authors and books."""

from contextlib import closing

from database import get_connection


def _row_as_dict(row):
    return dict(row) if row is not None else None


def add_author(name):
    """Add an author and return the new author's ID."""
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                "INSERT INTO author (Name) VALUES (?)", (name,)
            )
            return cursor.lastrowid


def get_author(author_id):
    """Return one author as a dictionary, or None if the ID is not found."""
    with closing(get_connection()) as connection:
        row = connection.execute(
            "SELECT Author_id, Name FROM author WHERE Author_id = ?",
            (author_id,),
        ).fetchone()
        return _row_as_dict(row)


def get_all_authors():
    """Return all authors as a list of dictionaries."""
    with closing(get_connection()) as connection:
        rows = connection.execute(
            "SELECT Author_id, Name FROM author ORDER BY Author_id"
        ).fetchall()
        return [dict(row) for row in rows]


def update_author(author_id, name):
    """Update an author; return True if an author with that ID exists."""
    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                "UPDATE author SET Name = ? WHERE Author_id = ?",
                (name, author_id),
            )
            return cursor.rowcount > 0


def add_book(title, author_id, year, rating, read_it_or_not):
    """Add a book and return its ID. Ratings outside 1 through 5 are rejected."""
    if rating is not None and not 1 <= rating <= 5:
        raise ValueError("Rating must be between 1 and 5")

    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                INSERT INTO book (Title, Author_id, Year, Rating, Read_it_or_not)
                VALUES (?, ?, ?, ?, ?)
                """,
                (title, author_id, year, rating, read_it_or_not),
            )
            return cursor.lastrowid


def get_book(book_id):
    """Return one book as a dictionary, or None if the ID is not found."""
    with closing(get_connection()) as connection:
        row = connection.execute(
            """
            SELECT Book_id, Title, Author_id, Year, Rating, Read_it_or_not
            FROM book WHERE Book_id = ?
            """,
            (book_id,),
        ).fetchone()
        return _row_as_dict(row)


def get_all_books():
    """Return all books as a list of dictionaries."""
    with closing(get_connection()) as connection:
        rows = connection.execute(
            """
            SELECT Book_id, Title, Author_id, Year, Rating, Read_it_or_not
            FROM book ORDER BY Book_id
            """
        ).fetchall()
        return [dict(row) for row in rows]


def update_book(book_id, title, author_id, year, rating, read_it_or_not):
    """Update a book; return True if a book with that ID exists."""
    if rating is not None and not 1 <= rating <= 5:
        raise ValueError("Rating must be between 1 and 5")

    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.execute(
                """
                UPDATE book
                SET Title = ?, Author_id = ?, Year = ?, Rating = ?,
                    Read_it_or_not = ?
                WHERE Book_id = ?
                """,
                (title, author_id, year, rating, read_it_or_not, book_id),
            )
            return cursor.rowcount > 0