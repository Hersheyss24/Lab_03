# Book Collection

A small Python 3 project that stores authors and books in SQLite. It uses only
the Python standard library.

## Project files

- `database.py` creates `book_collection.db` and the tables, and enables foreign-key checks.
- `books_api.py` provides functions to add, read, and update authors and books.
- `client.py` demonstrates the API with two authors and three books, then updates one book.
- `book_collection_dd.txt` is the supplied data dictionary.
- `book_collection.db` is generated when the database is initialized.
- `copilot_transcription.txt` contains a hypothetical, seven-prompt build conversation.
- `reflection.md` contains a draft reflection about that hypothetical workflow.

## Database schema

- `author`: `Author_id` is the integer primary key; `Name` is required text.
- `book`: `Book_id` is the integer primary key; `Title` is required text; `Author_id` references `author`; `Year` is an integer; `Rating` must be between 1 and 5; `Read_it_or_not` stores a boolean value (`0` or `1`).

## Run the project

Open this project folder in VS Code. In the terminal, run these commands in order:

```text
python3 database.py
python3 client.py
```

The first command initializes the database. The client also initializes it if
needed, then adds sample records, displays them, and prints the updated book.
Running the client again adds another set of records; it does not clear the
existing data.

## Example output

On a fresh database, the client output includes:

```text
Adding sample authors and books...

All authors:
{'Author_id': 1, 'Name': 'Ursula K. Le Guin'}
{'Author_id': 2, 'Name': 'George Orwell'}

All books:
{'Book_id': 1, 'Title': 'A Wizard of Earthsea', 'Author_id': 1, 'Year': 1968, 'Rating': 5, 'Read_it_or_not': 1}
{'Book_id': 2, 'Title': 'The Left Hand of Darkness', 'Author_id': 1, 'Year': 1969, 'Rating': 5, 'Read_it_or_not': 0}
{'Book_id': 3, 'Title': 'Nineteen Eighty-Four', 'Author_id': 2, 'Year': 1949, 'Rating': 4, 'Read_it_or_not': 1}

Updating one book...
Updated book: {'Book_id': 1, 'Title': 'A Wizard of Earthsea (updated)', 'Author_id': 1, 'Year': 1968, 'Rating': 5, 'Read_it_or_not': 1}
```

IDs may differ if the database already contains records. Boolean values appear
as `1` and `0` in SQLite output.

## Check SQLite directly

This query uses Python's `sqlite3` module directly, without calling the API:

```text
python3 -c "import sqlite3; c=sqlite3.connect('book_collection.db'); print('authors:', c.execute('SELECT * FROM author').fetchall()); print('books:', c.execute('SELECT * FROM book').fetchall()); c.close()"
```