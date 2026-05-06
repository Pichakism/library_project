import csv
import os
from models.books import Book

def save_book_in_csv(book):
    file_path = "./data/book_data.csv"
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
            book.book_status.name
        ])
        print(f"\nBook \"{book.book_title}\" saved Successfully...")
    
def search_book_with_isbn_in_csv(isbn):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["isbn"] == isbn:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_title_in_csv(title):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["book_title"] == title:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_auther_name_in_csv(auther_name):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["auther_name"] == auther_name:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_publication_year_in_csv(publication_year):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["publication_year"] == publication_year:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_page_count_in_csv(page_count):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["page_count"] == page_count:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_genre_in_csv(genre):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["genre"] == genre:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")

def search_book_with_book_status_in_csv(book_status):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        book_data = csv.DictReader(file)
        for book in book_data:
            if book["book_status"] == book_status:
                print("\nBook founded! :")
                print(f"ISBN = {book['isbn']}\nBook title = {book['book_title']}\nAuther name = {book['auther_name']}\nPublication date = {book['publication_year']}\nPage Number = {book['page_count']}\nGenre = {book['genre']}\nStatus = {book['book_status']}")
            else:
                print("Book not Founded...!")


def save_member_in_csv(member):
    file_path = "./data/member_data.csv"
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "id",
                "first_name",
                "last_name",
                "phone_number",
                "member_status",
                "date_of_join"
            ])
        writer.writerow([
            member.id,
            member.first_name,
            member.last_name,
            member.phone_number,
            member.member_status.name,
            member.date
        ])
        print(f"\nMember \"{member.first_name}{member.last_name}\" saved Successfully...")