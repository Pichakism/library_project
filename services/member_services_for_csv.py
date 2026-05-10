import csv
import datetime
from services.gtj import gregorian_to_jalali
from models.members import Member
from models.status import Member_Status
from services.csv_services import *

# Adds a new member to CSV
# - Gets member info from user input
# - Converts current Gregorian date to Jalali
# - Creates Member object
# - Calls save_member() to store data in CSV
def add_member_in_csv():
    print("\n-----Add Member Menu-----")
    id = input("\nEnter member ID: ")
    first_name = input("Enter member first name: ")
    last_name = input("Enter member last name: ")
    phone_number = input("Enter member phone number: ")
    member_status = int(input("\n1 - Available\n2 - Unavailable\nEnter member ststus: "))
    date = gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)

    save_member(Member(id, first_name, last_name, phone_number,Member_Status(member_status), date))

# Searches members in CSV based on selected field
# - Shows search menu
# - Maps user choice to column name
# - Calls search_member() with selected field and value
def search_member_in_csv():
    while True:
        search_fields = {
            "1": "id",
            "2": "first_name",
            "3": "last_name",
            "4": "phone_number",
            "5": "member_status",
            "6": "date"
        }
        user_input = input(
            "\n-----Search Member Menu-----\n"
            "How do you want to search?\n"
            "1 - By ID\n"
            "2 - By First name\n"
            "3 - By Last name\n"
            "4 - By Phone number\n"
            "5 - By Member status\n"
            "6 - By Date of join\n"
            "0 - Back...\n\n"
            "Enter: ")
        if user_input in search_fields:
            value = input("\nEnter search value: ")
            search_member(
                search_fields[user_input],
                value)
        elif user_input == "0":
            return
        else:
            print("Invalid choice!")

# Edits an existing member in CSV
# - Selects column to search
# - Gets value to locate member
# - Calls edit_member() to update record
def edit_member_in_csv():
    while True:
        search_column = int(input(
            "\n1 - ID"
            "\n2 - First Name"
            "\n3 - Last Name"
            "\n4 - Phone Number"
            "\n5 - Member Status"
            "\n6 - Date of Join"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if search_column == 0:
            return

        search_value = input("\nWhat is the desired value to search for? : ")

        if search_column not in range(1, 6):
            print("ERROR: Column is not valid!")
            continue
        else:
            edit_member(search_column, search_value)

# Removes a member from CSV
# - Selects column to search
# - Gets value to identify member
# - Calls remove_member() to delete record
def remove_member_in_csv():
    while True:
        search_column = int(input(
            "\n1 - ID"
            "\n2 - First Name"
            "\n3 - Last Name"
            "\n4 - Phone Number"
            "\n5 - Member Status"
            "\n6 - Date of Join"
            "\n0 - Back"
            "\n\nWhich column should we search based on? : "))
        if search_column == 0:
            return

        search_value = input("\nWhat is the desired value to search for? : ")

        if search_column not in range(1, 6):
            print("ERROR: Column is not valid!")
            continue
        else:
            remove_member(search_column, search_value)

# Main menu for member management
# - Routes user to add, search, edit, or remove member operations
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
        if user_input == "1":
            add_member_in_csv()
        elif user_input == "2":
            search_member_in_csv()
        elif user_input == "3":
            edit_member_in_csv()
        elif user_input == "4":
            remove_member_in_csv()
        elif user_input == "0":
            return

