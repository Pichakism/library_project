from src.services.service_factory import get_loan_service, get_book_service, get_member_service
from src.controler.book_controler import user_input_for_book_search, book_fields
from src.controler.member_controler import user_input_for_member_search, member_fields
from src.models.loan import Loan
from src.services.gtj import gregorian_to_jalali
import datetime


loan_fields = {
    "1": "id",
    "2": "member_id",
    "3": "book_id",
    "4": "date"
}

# -------------------------
# LOAN BOOK
# -------------------------
# Handles book borrowing process between book + member search
def add_loan(chosen_db):
    book_result = user_input_for_book_search()
    member_result = user_input_for_member_search()
    if book_result is None:
        return
    book_column, book_value = book_result
    if member_result is None:
        return
    member_column, member_value = member_result

    book_service = get_book_service(chosen_db)
    member_service = get_member_service(chosen_db)

    book_data = book_service.select_book(book_fields[str(book_column)], book_value)
    member_data = member_service.select_member(member_fields[str(member_column)], member_value)

    print("\nYour book data:")
    for i, row in enumerate(book_data, 1):
        print(f"\nBook Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")
    print("\nYour member data:")
    for i, row in enumerate(member_data, 1):
        print(f"\nMember Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")

    user_book_input = int(input("\nEnter Book Number: "))
    if user_book_input < 1 or user_book_input > len(book_data):
        print("Invalid number!")
        return
    user_member_input = int(input("\nEnter Member Number: "))
    if user_member_input < 1 or user_member_input > len(member_data):
        print("Invalid number!")
        return

    book_id = book_data[user_book_input - 1]["id"]
    member_id = member_data[user_member_input - 1]["id"]
    loan = Loan(book_id, member_id,
                str(gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)))

    service = get_loan_service(chosen_db)
    print(service.insert_loan(loan))


def user_input_for_search():
    while True:
        column = int(input(
            "\n-----Search Book Menu-----\n"
            "How do you want to search?\n"
            "\n1 - ID"
            "\n2 - Member ID"
            "\n3 - Book ID"
            "\n4 - Date"
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

def search_loan(chosen_db):
    result = user_input_for_search()
    if result is None:
        return
    column, value = result

    service = get_loan_service(chosen_db)
    data = service.select_loan(loan_fields[str(column)], value)
    print("\nYour data:")
    for i, row in enumerate(data, 1):
        print(f"\nLoan Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")

    return data, loan_fields[str(column)], value

def edit_loan(chosen_db):
    result = search_loan(chosen_db)
    if not result:
        return
    data, column, value = result
    service = get_loan_service(chosen_db)

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

    print(service.update_loan(column, value, updates))

def remove_loan(chosen_db):
    while True:
        column = int(input(
            "\n-----Delete Book Menu-----\n"
            "\n1 - ID"
            "\n2 - Member ID"
            "\n3 - Book ID"
            "\n4 - Date"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if column == 0:
            return
        value = input("\nWhat is the desired value to search for? : ")

        service = get_loan_service(chosen_db)
        print(service.delete_loan(loan_fields[str(column)], value))

def loan_managment():
    while True:
        user_input = (input(
            "\n-----Book Managment Menu-----\n"
            "What you want to do?\n"
            "1 - Add a Loan\n"
            "2 - Search a Loan\n"
            "3 - Edit a Loan\n"
            "4 - Remove a Loan\n"
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
            add_loan(database_chosen)
        elif user_input == "2":
            search_loan(database_chosen)
        elif user_input == "3":
            edit_loan(database_chosen)
        elif user_input == "4":
            remove_loan(database_chosen)