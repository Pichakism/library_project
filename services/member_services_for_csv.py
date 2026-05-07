import csv
import datetime
from services.gtj import gregorian_to_jalali
from models.members import Member
from models.member_status import Member_Status
from services.csv_services import *

def add_member_in_csv():
    id = input("\nEnter member ID: ")
    first_name = input("Enter member first name: ")
    last_name = input("Enter member last name: ")
    phone_number = input("Enter member phone number: ")
    member_status = int(input("\n1 - Available\n2 - Unavailable\nEnter member ststus: "))
    date = gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)

    save_member_in_csv(Member(id, first_name, last_name, phone_number,Member_Status(member_status), date))

def search_member_in_csv():
    search_fields = {
        "1": "id",
        "2": "first_name",
        "3": "last_name",
        "4": "phone_number",
        "5": "member_status",
        "6": "date"
    }
    user_input = input("\nHow do you want to search?\n1 - By ID\n2 - By First name\n3 - By Last name\n4 - By Phone number\n5 - By Member status\n6 - By Date of join\n\nEnter: ")
    
    if user_input in search_fields:
        value = input("\nEnter search value: ")
        search_member(
            search_fields[user_input],
            value
        )
    else:
        print("Invalid choice!")

def member_managment():
    user_input = (input("\nWhat you want to do?\n1 - Add member\n2 - Search member\n\nEnter your request: "))
    if user_input == "1":
        add_member_in_csv()
    elif user_input == "2":
        search_member_in_csv()

