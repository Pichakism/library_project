from models.books import Book
from services.book_services_for_csv import add_book_in_csv, search_book_in_csv

print("\nHow can I help you?\n1 - Add a Book\n2 - Search a Book")
user_input = input("\nEnter number of your request: ")


if user_input == "1":
    add_book_in_csv()
elif user_input == "2":
    search_book_in_csv()