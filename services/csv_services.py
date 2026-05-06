import csv
import os
from models.books import Book

file_path = "./data/book_data.csv"

def save_book_in_csv(book):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "isbn",
                "book_title",
                "auther_name",
                "publication_year",
                "page_count",
                "genre",
                "book_status"
            ])
        writer.writerow([
            book.isbn,
            book.book_title,
            book.auther_name,
            book.publication_year,
            book.page_count,
            book.genre,
            book.book_status
        ])
        print(f"\nBook \"{book.book_title}\" saved Successfully...")
    
def search_book_with_isbn_in_csv(isbn):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["isbn"] == isbn:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_title_in_csv(title):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["book_title"] == title:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_auther_name_in_csv(auther_name):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["auther_name"] == auther_name:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_publication_year_in_csv(publication_year):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["publication_year"] == publication_year:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_page_count_in_csv(page_count):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["page_count"] == page_count:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_genre_in_csv(genre):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["genre"] == genre:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_book_status_in_csv(book_status):
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["book_status"] == book_status:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")