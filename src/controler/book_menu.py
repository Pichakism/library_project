import csv
from src.models.books import Book
from src.models.loan import Loan
from src.models.status import *
# from src.services.csv_services import orchestration
from src.repositories.csv_repository import *
from src.repositories import sqlite_repository
from src.repositories import csv_repository
from src.repositories import mysql_repository
from src.repositories import postgreSql_repository
from src.repositories import sqlServer_repository
from src.services import sqlite_service, mysql_service, postgreSql_service, sqlServer_service


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
    auther_name = input("Enter auther name: ")
    publication_year = input("Enter publication year: ")
    page_count = input("Enter number of page: ")
    genre = input("Enter genre: ")
    book_status = int(input("\n1 - Available\n2 - Unavailable\n3 - On loan\n4 - Reserved\nEnter book ststus: "))
    physical_version = int(input("\n1 - Yes\n2 - No\nEnter Physical version Value: "))
    digital_version = int(input("\n1 - Yes\n2 - No\nEnter Digital version Value: "))
    count = int(input("Enter count of book: "))

    book = Book(isbn,
            book_title,
            auther_name,
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
    elif chosen_db == "2":
        add = sqlite_repository.BookRepository()
        print(add.save_book(book))
    elif chosen_db == "3":
        add = mysql_repository.BookRepository()
        print(add.save_book(book))
    elif chosen_db == "4":
        add = postgreSql_repository.BookRepository()
        print(add.save_book(book))
    elif chosen_db == "5":
        add = sqlServer_repository.BookRepository()
        print(add.save_book(book))
    
def user_input_for_search_or_update():
    while True:
        search_column = int(input(
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
        if search_column == 0:
            return
        search_value = input("\nWhat is the desired value to search for? : ")
        if search_column not in range(1, 11):
            print("ERROR: Column is not valid!")
            continue
        else:
            return search_column, search_value

# Searches books in CSV based on selected field
# - Shows search menu
# - Takes search column + value
# - Calls search_book() from services
def search_book(chosen_db):
    result = user_input_for_search_or_update()
    if result is None:
        return
    column, values = result
    if chosen_db == "1":
        search = csv_repository.BookRepository()
        search.search_book_in_csv(book_fields[str(column)], values)
    elif chosen_db == "2":
        search = sqlite_service.SqLiteService()
        return search.search_book(book_fields[str(column)], values), book_fields[str(column)], values
    elif chosen_db == "3":
        search = mysql_service.MySqlService()
        return search.search_book(book_fields[str(column)], values), book_fields[str(column)], values
    elif chosen_db == "4":
        search = postgreSql_service.PostgreSqlService()
        return search.search_book(book_fields[str(column)], values), book_fields[str(column)], values
    elif chosen_db == "5":
        search = sqlServer_service.SqlServerService()
        return search.search_book(book_fields[str(column)], values), book_fields[str(column)], values
    
# Edits an existing book record in CSV
# - Selects column to search
# - Gets search value
# - Calls edit_book() to update matched record
def edit_book(chosen_db):
    if chosen_db == "1":
        edit = csv_repository.BookRepository()
        edit.search_book_in_csv(book_fields[str(column)], values)
    elif chosen_db == "2":
        data, column, value = search_book(chosen_db)
        if not data:
            print("No books found!")
            return
        sqlite_service.SqLiteService().update_book(data, column, value)
    elif chosen_db == "3":
        data, column, value = search_book(chosen_db)
        if not data:
            print("No books found!")
            return
        mysql_service.MySqlService().update_book(data, column, value)
    elif chosen_db == "4":
        data, column, value = search_book(chosen_db)
        if not data:
            print("No books found!")
            return
        postgreSql_service.PostgreSqlService().update_book(data, column, value)
    elif chosen_db == "5":
        data, column, value = search_book(chosen_db)
        if not data:
            print("No books found!")
            return
        sqlServer_service.SqlServerService.update_book(data, column, value)

# Removes a book from CSV
# - Selects column to search
# - Gets search value
# - Calls remove_book() to delete matched record
def remove_book(chosen_db):
    while True:
        search_column = int(input(
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
        if search_column == 0:
            return
        search_value = input("\nWhat is the desired value to search for? : ")

        if search_column not in range(1, 10):
            print("ERROR: Column is not valid!")
            continue
        else:
            if chosen_db == "1":
                delete = csv_repository.BookRepository()
                delete.remove_book_in_csv(search_column, search_value)
            elif chosen_db == "2":
                delete = sqlite_repository.BookRepository()
                delete.delete_book(book_fields[str(search_column)], search_value)
            elif chosen_db == "3":
                delete = mysql_repository.BookRepository()
                delete.delete_book(book_fields[str(search_column)], search_value)
            elif chosen_db == "4":
                delete = postgreSql_repository.BookRepository()
                delete.delete_book(book_fields[str(search_column)], search_value)
            elif chosen_db == "5":
                delete = sqlServer_repository.BookRepository()
                delete.delete_book(book_fields[str(search_column)], search_value)

"""def add_loan(chosen_db):
    print("\n-----Add Member Menu-----")
    id = input("\nEnter loan ID: ")
    book_isbn = input("Enter book ISBN: ")
    member_id = input("Enter member ID: ")
    date = gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)

    loan = Loan(id, book_isbn, member_id, date)
    save_loan_in_csv(loan)"""

def loan_book(chosen_db):
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