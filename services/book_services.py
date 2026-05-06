import csv
from models.books import Book
from services.file_services import save_book_csv



def add_book():
    book_id = input("\nEnter book ID: ")
    book_title = input("Enter book title: ")
    auther_name = input("Enter auther name: ")
    publication_year = input("Enter publication year: ")
    page_count = input("Enter number of page: ")
    genre = input("Enter genre: ")
    book_status = input("Enter book ststus: ")

    save_book_csv(Book(book_id, book_title, auther_name, publication_year, page_count, genre, book_status))

