from models.books import Book
from services.book_services import add_book

print("\nHow can I help to you?\n1 - Add book")
user_input = input("\nEnter number of your request: ")


if user_input == "1":
    add_book()
