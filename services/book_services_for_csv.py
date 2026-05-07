import csv
from models.books import Book
from models.book_status import Book_Status
from services.csv_services import *

def add_book_in_csv():
    isbn = input("\nEnter book ISBN: ")
    book_title = input("Enter book title: ")
    auther_name = input("Enter auther name: ")
    publication_year = input("Enter publication year: ")
    page_count = input("Enter number of page: ")
    genre = input("Enter genre: ")
    book_status = int(input("\n1 - Available\n2 - Unavailable\n3 - On loan\n4 - Reserved\nEnter book ststus: "))

    save_book_in_csv(Book(isbn, book_title, auther_name, publication_year, page_count, genre, Book_Status(book_status)))

def search_book_in_csv():
    search_fields = {
        "1": "isbn",
        "2": "book_title",
        "3": "auther_name",
        "4": "publication_year",
        "5": "page_count",
        "6": "genre",
        "7": "book_status"
    }
    user_input = input("\nHow do you want to search?\n1 - By ISBN\n2 - By title\n3 - By auther name\n4 - By publication year\n5 - By page number\n6 - By genre\n7 - By status\n\nEnter: ")
    
    if user_input in search_fields:
        value = input("\nEnter search value: ")
        search_book(
            search_fields[user_input],
            value
        )
    else:
        print("Invalid choice!")
    