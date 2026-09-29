"""Run a small demonstration of the book collection API."""

import database
import books_api


def main():
    database.initialize_database()

    print("Adding sample authors and books...")
    author_one_id = books_api.add_author("Ursula K. Le Guin")
    author_two_id = books_api.add_author("George Orwell")

    book_one_id = books_api.add_book(
        "A Wizard of Earthsea", author_one_id, 1968, 5, True
    )
    books_api.add_book("The Left Hand of Darkness", author_one_id, 1969, 5, False)
    books_api.add_book("Nineteen Eighty-Four", author_two_id, 1949, 4, True)

    print("\nAll authors:")
    for author in books_api.get_all_authors():
        print(author)

    print("\nAll books:")
    for book in books_api.get_all_books():
        print(book)

    print("\nUpdating one book...")
    books_api.update_book(
        book_one_id, "A Wizard of Earthsea (updated)", author_one_id, 1968, 5, True
    )
    print("Updated book:", books_api.get_book(book_one_id))


if __name__ == "__main__":
    main()