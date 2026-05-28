import csv
import datetime
from src.services.gtj import gregorian_to_jalali
from src.models.members import Member
from src.models.status import Member_Status
from src.services.service_factory import get_member_service

# Mapping menu input numbers to actual database column names
member_fields = {
    "1": "id",
    "2": "first_name",
    "3": "last_name",
    "4": "phone_number",
    "5": "member_status",
    "6": "join_date"
}

# -------------------------
# ADD MEMBER
# -------------------------
# Gets member info from user input
# creates Member object
# sends it to service layer for insert operation
def add_member(chosen_db):
    print("\n-----Add Member Menu-----")
    # id = input("\nEnter member ID: ")
    first_name = input("Enter member first name: ")
    last_name = input("Enter member last name: ")
    phone_number = input("Enter member phone number: ")
    member_status = int(input("\n1 - Available\n2 - Unavailable\nEnter member ststus: "))
    join_date = str(gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))

    member = Member(first_name, last_name, phone_number,Member_Status(member_status), join_date)
    
    service = get_member_service(chosen_db)
    print(service.insert_member(member))

# -------------------------
# SEARCH INPUT
# -------------------------
# Gets search input from user
# selects column and value
def user_input_for_member_search():
    while True:
        column = int(input(
            "\n-----Search Member Menu-----\n"
            "How do you want to search?\n"
            "1 - By ID\n"
            "2 - By First name\n"
            "3 - By Last name\n"
            "4 - By Phone number\n"
            "5 - By Member status\n"
            "6 - By Date of join\n"
            "0 - Back...\n\n"
            "Enter: "))
        if column == 0:
            return
        value = input("\nWhat is the desired value to search for? : ")
        if column not in range(1, 7):
            print("ERROR: Column is not valid!")
            continue
        else:
            return column, value

# -------------------------
# SEARCH MEMBER
# -------------------------
# Searches member data using service layer
# prints formatted output
def search_member(chosen_db):
    result = user_input_for_member_search()
    if result is None:
        return
    column, value = result

    service = get_member_service(chosen_db)
    data = service.select_member(member_fields[str(column)], value)
    print("\nYour data:")
    for i, row in enumerate(data, 1):
        print(f"\nMember Number {i}:")
        for k, v in row.items():
            print(f"{k} : {v}")

    return data, member_fields[str(column)], value
    

# -------------------------
# EDIT MEMBER
# -------------------------
# Selects record from search result
# gets updated values from user
# sends update request to service layer
def edit_member(chosen_db):
    result = search_member(chosen_db)
    if not result:
        return
    data, column, value = result
    service = get_member_service(chosen_db)

    user_input = int(input("\nEnter Member Number: "))
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

    print(service.update_member(column, value, updates))

# -------------------------
# REMOVE MEMBER
# -------------------------
# Deletes member based on selected column
# calls service layer delete method
def remove_member(chosen_db):
    while True:
        column = int(input(
            "\n1 - ID"
            "\n2 - First Name"
            "\n3 - Last Name"
            "\n4 - Phone Number"
            "\n5 - Member Status"
            "\n6 - Date of Join"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if column == 0:
            return
        value = input("\nWhat is the desired value to search for? : ")

        service = get_member_service(chosen_db)
        print(service.delete_member(member_fields[str(column)], value))

# -------------------------
# MAIN MENU
# -------------------------
# only handles user input and routing
def member_managment():
    while True:
        user_input = (input(
            "\n-----Member Managment Menu-----\n"
            "What you want to do?\n"
            "1 - Add a member\n"
            "2 - Search a member\n"
            "3 - Edit a Member\n"
            "4 - Remove a Member\n"
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
        database_chosen = input("\n\nEnter number of your request: ")
        if user_input == "1":
            add_member(database_chosen)
        elif user_input == "2":
            search_member(database_chosen)
        elif user_input == "3":
            edit_member(database_chosen)
        elif user_input == "4":
            remove_member(database_chosen)