import csv
from src.models.books import Book
from src.models.loan import Loan
from src.models.status import *
# from src.services.csv_services import orchestration
# from src.repositories import (sqlite_repository, mysql_repository, postgreSql_repository, sqlServer_repository, csv_repository)
# from src.services.book_service import BookService 
from src.services.service_factory import get_book_service
# from src.storages.sqlite_storage import SqliteStorage
# from src.storages.mysql_storage import MySqlStorage
# from src.storages.postgreSql_storage import PostgreSqlStorage
# from src.storages.sqlServer_storage import SqlServerStorage
# from src.services import sqlite_service, mysql_service, postgreSql_service, sqlServer_service


book_fields = {
    "1": "isbn",
    "2": "book_title",
    "3": "author_name",
    "4": "publication_year",
    "5": "page_count",
    "6": "genre",
    "7": "book_status",
    "8": "physical_version",
    "9": "digital_version",
    "10": "count"
}

# Adds a new book to CSV
# - Takes user input for all book fields
# - Creates a Book object
# - Calls save_book() to persist it in CSV
def add_book(chosen_db):
    print("\n-----Add Book Menu-----")
    isbn = input("\nEnter book ISBN: ")
    book_title = input("Enter book title: ")
    author_name = input("Enter auther name: ")
    publication_year = input("Enter publication year: ")
    page_count = input("Enter number of page: ")
    genre = input("Enter genre: ")
    book_status = int(input("\n1 - Available\n2 - Unavailable\n3 - On loan\n4 - Reserved\nEnter book ststus: "))
    physical_version = int(input("\n1 - Yes\n2 - No\nEnter Physical version Value: "))
    digital_version = int(input("\n1 - Yes\n2 - No\nEnter Digital version Value: "))
    count = int(input("Enter count of book: "))

    book = Book(isbn,
            book_title,
            author_name,
            publication_year,
            page_count,
            genre,
            Book_Status(book_status),
            Physical_version(physical_version),
            Digital_version(digital_version),
            count)
    if chosen_db == "1":
        add = csv_repository.BookRepository()
        print(add.save_book_in_csv(book))
    service = get_book_service(chosen_db)
    print(service.insert_book(book))
    
def user_input_for_search():
    while True:
        column = int(input(
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
            "10 - count\n"
            "0 - Back...\n\n"
            "Enter: "))
        if column == 0:
            return
        value = input("\nWhat is the desired value to search for? : ")
        if column not in range(1, 11):
            print("ERROR: Column is not valid!")
            continue
        else:
            return column, value

# Searches books in CSV based on selected field
# - Shows search menu
# - Takes search column + value
# - Calls search_book() from services
def search_book(chosen_db):
    result = user_input_for_search()
    if result is None:
        return
    column, value = result
    
    if chosen_db == "1":
        from src.repositories.csv_repository import BookRepository # ---------------------------------
        data = BookRepository().search_book_in_csv(book_fields[str(column)], value) # ---------------------------------
        for i, row in enumerate(data, 1): # ---------------------------------
            print(f"\nBook {i}: {row}") # ---------------------------------

        return None

    service = get_book_service(chosen_db)
    data = service.select_book(book_fields[str(column)], value)
    print("\nYour data:")
    for i, row in enumerate(data, 1):
        print(f"\nBook Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")

    return data, book_fields[str(column)], value
    
# Edits an existing book record in CSV
# - Selects column to search
# - Gets search value
# - Calls edit_book() to update matched record
def edit_book(chosen_db):
    result = search_book(chosen_db)
    if not result:
        return
    data, column, value = result
    service = get_book_service(chosen_db)

    user_input = int(input("\nEnter Book Number: "))
    if user_input < 1 or user_input > len(data):
        print("Invalid number!")
        return

    selected = data[user_input - 1]

    updates = {}
    print("\nEnter new values (Enter to skip):")

    for k, v in selected.items():
        new_val = input(f"{k} ({v}): ")
        if new_val.strip():
            updates[k] = new_val

    if not updates:
        print("No changes")
        return

    print(service.update_book(column, value, updates))

# Removes a book from CSV
# - Selects column to search
# - Gets search value
# - Calls remove_book() to delete matched record
def remove_book(chosen_db):
    while True:
        column = int(input(
            "\n-----Delete Book Menu-----\n"
            "\n1 - ISBN"
            "\n2 - Book Title"
            "\n3 - Auter Name"
            "\n4 - Publication Year"
            "\n5 - Page Count"
            "\n6 - Genre"
            "\n7 - Book Status"
            "\n8 - Physical Version"
            "\n9 - Digital Version"
            "\n10 - Count"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if column == 0:
            return
        value = input("\nWhat is the desired value to search for? : ")

        if chosen_db == "1":
            from src.repositories.csv_repository import BookRepository
            print(BookRepository().remove_book_in_csv(column, value))
            continue

        service = get_book_service(chosen_db)
        print(service.delete_book(book_fields[str(column)], value))

"""def add_loan(chosen_db):
    print("\n-----Add Member Menu-----")
    id = input("\nEnter loan ID: ")
    book_isbn = input("Enter book ISBN: ")
    member_id = input("Enter member ID: ")
    date = gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)

    loan = Loan(id, book_isbn, member_id, date)
    save_loan_in_csv(loan)"""

def loan_book(chosen_db):
    """print("\n-----Loan Book Menu-----")

    book_column = int(input("Book column: "))
    book_value = input("Book value: ")

    member_column = int(input("Member column: "))
    member_value = input("Member value: ")

    _, service = get_book_service(chosen_db)

    print(service.loan_book(
        (book_fields[str(book_column)], book_value),
        ("member_field", member_value)
    ))"""
    while True:
        search_column_for_book = int(input(
            "\n-----Loan Book Menu-----\n"
            "\n1 - ISBN"
            "\n2 - Book Title"
            "\n3 - Auter Name"
            "\n4 - Publication Year"
            "\n5 - Page Count"
            "\n6 - Genre"
            "\n7 - Book Status"
            "\n8 - Physical Version"
            "\n9 - Digital Version"
            "\n10 - Count"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if search_column_for_book == 0:
            return
        search_value_for_book = input("\nWhat is the desired value to search for? : ")

        search_column_for_member = int(input(
            "\n1 - ID"
            "\n2 - First Name"
            "\n3 - Last Name"
            "\n4 - Phone Number"
            "\n5 - Member Status"
            "\n6 - Date of Join"
            "\n\nWhich column should we search based on? : "))
        search_value_for_member = input("\nWhat is the desired value to search for? : ")

        if search_column_for_book not in range(1, 10) and search_column_for_member not in range(1, 6):
            print("ERROR: Column is not valid!")
            continue
        else:
            if chosen_db == "1":
                add = csv_repository.LoanRepository()
                add.loan_book_in_csv(
                    search_column_for_book,
                    search_value_for_book,
                    search_column_for_member,
                    search_value_for_member
                    )
            elif chosen_db == "2":
                ... # TODO:         
            elif chosen_db == "3":
                ... # TODO:         

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
            "5 - Loan a Book\n"
            "0 - Back...\n\n"
            "Enter your request: "))
        if user_input == "0":
            return
        print(
            "\n---Choose Database---"
            "\nWhat Database do you want?\n"
            "1 - CSV\n"
            "2 - sqLite\n"
            "3 - mySql\n"
            "4 - postgreSql\n"
            "5 - SQL Server\n"
            )
        database_chosen = input("\nEnter number of your request: ")
        if user_input == "1":
            add_book(database_chosen)
        elif user_input == "2":
            search_book(database_chosen)
        elif user_input == "3":
            edit_book(database_chosen)
        elif user_input == "4":
            remove_book(database_chosen)
        elif user_input == "5":
            loan_book(database_chosen)