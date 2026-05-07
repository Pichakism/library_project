from models.books import Book
from services.book_services_for_csv import book_managment
from services.member_services_for_csv import member_managment

print("\nHow can I help you?\n1 - Book managment\n2 - Member managment")
user_input = input("\nEnter number of your request: ")


if user_input == "1":
    book_managment()
elif user_input == "2":
    member_managment()
