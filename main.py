from models.books import Book
from services.book_services_for_csv import book_managment
from services.member_services_for_csv import member_managment

def starter():
    while True:
        print(
            "\n---Starter Menu---"
            "\nHow can I help you?\n"
            "1 - Book managment\n"
            "2 - Member managment\n"
            "0 - Exit..."
            )
        user_input = input("\n\nEnter number of your request: ")

        if user_input == "1":
            book_managment()
        elif user_input == "2":
            member_managment()
        elif user_input == "0":
            print("\n***Bye Bye...!***\n")
            break


starter()