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
    user_input = input("\nHow do you want to search?\n1 - By ISBN\n2 - By title\n3 - By auther name\n4 - By publication year\n5 - By page number\n6 - By genre\n7 - By status\n\nEnter: ")
    if user_input == "1":
        isbn = input("\nEnter book ISBN: ")
        search_book_with_isbn_in_csv(isbn)
    elif user_input == "2":
        title = input("\nEnter book title: ")
        search_book_with_title_in_csv(title)
    elif user_input == "3":
        auther_name = input("\nEnter auther name: ")
        search_book_with_auther_name_in_csv(auther_name)
    elif user_input == "4":
        publication_year = input("\nEnter publication year: ")
        search_book_with_publication_year_in_csv(publication_year)
    elif user_input == "5":
        page_count = input("\nEnter page number: ")
        search_book_with_page_count_in_csv(page_count)
    elif user_input == "6":
        genre = input("\nEnter book genre: ")
        search_book_with_genre_in_csv(genre)
    elif user_input == "7":
        book_status = input("\nEnter book atatus: ")
        search_book_with_book_status_in_csv(book_status)
    else:
        print("Invalid Input...! Try Again")