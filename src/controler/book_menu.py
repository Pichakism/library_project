import csv
from src.models.books import Book
from src.models.status import *
# from src.services.csv_services import orchestration
from src.repositories.csv_repository import *


# Adds a new book to CSV
# - Takes user input for all book fields
# - Creates a Book object
# - Calls save_book() to persist it in CSV
def add_book(chosen_db):
    print("\n-----Add Book Menu-----")
    isbn = input("\nEnter book ISBN: ")
    book_title = input("Enter book title: ")
    auther_name = input("Enter auther name: ")
    publication_year = input("Enter publication year: ")
    page_count = input("Enter number of page: ")
    genre = input("Enter genre: ")
    book_status = int(input("\n1 - Available\n2 - Unavailable\n3 - On loan\n4 - Reserved\nEnter book ststus: "))
    physical_version = int(input("\n1 - Yes\n2 - No\nEnter Physical version Value: "))
    digital_version = int(input("\n1 - Yes\n2 - No\nEnter Digital version Value: "))

    book = Book(isbn,
            book_title,
            auther_name,
            publication_year,
            page_count,
            genre,
            Book_Status(book_status),
            Physical_version(physical_version),
            Digital_version(digital_version))
    if chosen_db == "1":
        save_book_in_csv(book)
    

# Searches books in CSV based on selected field
# - Shows search menu
# - Takes search column + value
# - Calls search_book() from services
def search_book(chosen_db):
    while True:
        search_fields = {
            "1": "isbn",
            "2": "book_title",
            "3": "auther_name",
            "4": "publication_year",
            "5": "page_count",
            "6": "genre",
            "7": "book_status",
            "8": "physical_version",
            "9": "digital_version"
        }
        user_input = input(
            "\n-----Search Book Menu-----\n"
            "How do you want to search?\n"
            "1 - By ISBN\n"
            "2 - By title\n"
            "3 - By auther name\n"
            "4 - By publication year\n"
            "5 - By page number\n"
            "6 - By genre\n"
            "7 - By status\n"
            "8 - Physical version\n"
            "9 - Digital version\n"
            "0 - Back...\n\n"
            "Enter: ")
        if user_input in search_fields:
            value = input("\nEnter search value: ")
            if chosen_db == "1":
                search_book(int(user_input), value)
        elif user_input == "0":
            return
        else:
            print("Invalid choice!")
    
# Edits an existing book record in CSV
# - Selects column to search
# - Gets search value
# - Calls edit_book() to update matched record
def edit_book(chosen_db):
    while True:
        search_column = int(input(
            "\n-----Edit Book Menu-----\n"
            "\n1 - ISBN"
            "\n2 - Book Title"
            "\n3 - Auter Name"
            "\n4 - Publication Year"
            "\n5 - Page Count"
            "\n6 - Genre"
            "\n7 - Book Status"
            "\n8 - Physical Version"
            "\n9 - Digital Version"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if search_column == 0:
            return
        search_value = input("\nWhat is the desired value to search for? : ")

        if search_column not in range(1, 9):
            print("ERROR: Column is not valid!")
            continue
        else:
            if chosen_db == "1":
                edit_book_in_csv(search_column, search_value)

# Removes a book from CSV
# - Selects column to search
# - Gets search value
# - Calls remove_book() to delete matched record
def remove_book(chosen_db):
    while True:
        search_column = int(input(
            "\n-----Edit Book Menu-----\n"
            "\n1 - ISBN"
            "\n2 - Book Title"
            "\n3 - Auter Name"
            "\n4 - Publication Year"
            "\n5 - Page Count"
            "\n6 - Genre"
            "\n7 - Book Status"
            "\n8 - Physical Version"
            "\n9 - Digital Version"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if search_column == 0:
            return
        search_value = input("\nWhat is the desired value to search for? : ")

        if search_column not in range(1, 9):
            print("ERROR: Column is not valid!")
            continue
        else:
            if chosen_db == "1":
                remove_book_in_csv(search_column, search_value)

# Main book management menu
# - Routes user to add, search, edit, or remove book functions
def book_managment():
    while True:
        user_input = (input(
            "\n-----Book Managment Menu-----\n"
            "What you want to do?\n"
            "1 - Add a Book\n"
            "2 - Search a Book\n"
            "3 - Edit a Book\n"
            "4 - Remove a Book\n"
            "0 - Back...\n\n"
            "Enter your request: "))
        if user_input == "0":
            return
        print(
            "\n---Choose Database---"
            "\nWhat Database do you want?\n"
            "1 - CSV\n"
            "2 - sqLite\n"
            )
        database_chosen = input("\n\nEnter number of your request: ")
        if user_input == "1":
            add_book(database_chosen)
        elif user_input == "2":
            search_book_in_csv(database_chosen)
        elif user_input == "3":
            edit_book(database_chosen)
        elif user_input == "4":
            remove_book(database_chosen)