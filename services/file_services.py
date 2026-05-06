import csv
import os
from models.books import Book

def save_book_csv(book):
    file_path = "./data/book_data.csv"
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "book_id",
                "book_title",
                "auther_name",
                "publication_year",
                "page_count",
                "genre",
                "book_status"
            ])

        writer.writerow([
            book.book_id,
            book.book_title,
            book.auther_name,
            book.publication_year,
            book.page_count,
            book.genre,
            book.book_status
        ])

        print(f"\nBook \"{book.book_title}\" save Successfully...")
    