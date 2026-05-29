import csv
from src.models.books import Book
from src.models.status import *

# Service factory is responsible for returning the correct service
# based on selected database (SQLite, MySQL, PostgreSQL, SQL Server)
from src.services.service_factory import get_book_service

# Mapping menu input numbers to actual database column names
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

# -------------------------
# ADD BOOK
# -------------------------
# Gets book info from user input,
# creates Book object,
# sends it to service layer for insertion
def add_book():
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

    # Domain object creation
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

    # Controller only communicates with service layer
    service = get_book_service()
    print(service.insert_book(book))
    
# -------------------------
# SEARCH INPUT
# -------------------------
# Handles search menu input and validation
def user_input_for_book_search():
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

# -------------------------
# SEARCH BOOK
# -------------------------
# Delegates search operation to service layer
# and prints formatted output
def search_book():
    result = user_input_for_book_search()
    if result is None:
        return
    column, value = result

    service = get_book_service()
    data = service.select_book(book_fields[str(column)], value)
    print("\nYour data:")
    for i, row in enumerate(data, 1):
        print(f"\nBook Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")

    return data, book_fields[str(column)], value
    
# -------------------------
# EDIT BOOK
# -------------------------
# Selects record from search result,
# collects update fields,
# sends update request to service layer
def edit_book():
    result = search_book()
    if not result:
        return
    data, column, value = result
    service = get_book_service()

    user_input = int(input("\nEnter Book Number: "))
    if user_input < 1 or user_input > len(data):
        print("Invalid number!")
        return

    selected = data[user_input - 1]

    updates = {}
    print("\nEnter new values (Enter to skip):")

    for k, v in selected.items():
        if k == "id":
            continue
        new_val = input(f"{k} ({v}): ")
        if new_val.strip():
            updates[k] = new_val

    if not updates:
        print("No changes")
        return

    print(service.update_book(column, value, updates))

# -------------------------
# REMOVE BOOK
# -------------------------
# Deletes book based on selected search criteria
def remove_book():
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

        service = get_book_service()
        print(service.delete_book(book_fields[str(column)], value))

# -------------------------
# MAIN MENU
# -------------------------
# Only responsible for user interaction and routing
def book_managment():
    while True:
        user_input = (input(
            "\n-----Book Managment Menu-----\n"
            "What you want to do?\n"
            "1 - Add a Book\n"
            "2 - Search a Book\n"
            "3 - Edit a Book\n"
            "4 - Remove a Book\n"
            # "5 - Loan a Book\n"
            "0 - Back...\n\n"
            "Enter your request: "))
        if user_input == "0":
            return
        # print(
        #     "\n---Choose Database---"
        #     "\nWhat Database do you want?\n"
        #     "1 - CSV\n"
        #     "2 - sqLite\n"
        #     "3 - mySql\n"
        #     "4 - postgreSql\n"
        #     "5 - SQL Server\n"
        #     )
        # database_chosen = input("\nEnter number of your request: ")
        if user_input == "1":
            add_book()
        elif user_input == "2":
            search_book()
        elif user_input == "3":
            edit_book()
        elif user_input == "4":
            remove_book()