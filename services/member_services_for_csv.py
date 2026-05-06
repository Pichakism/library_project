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

def member_managment():
    user_input = (input("\nWhat you want to do?\n1 - Add member\n\nEnter your request: "))
    if user_input == "1":
        add_member_in_csv()