from src.models.books import Book
from src.storages.sqlite_storage import SqliteStorage
from src.storages.mysql_storage import MySqlStorage
from src.controler.book_menu import book_managment
from src.controler.member_menu import member_managment
from src.repositories.sqlite_repository import *
from src.bootstrap import Bootstrap


bootstrap = Bootstrap(MySqlStorage())
storage = bootstrap.run()
print("Application started...")

# Main entry point of the program
# - Shows the starter menu to the user
# - Routes user to Book or Member management modules
# - Keeps program running until user chooses Exit
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

# Program execution starts here
# - Calls starter() to launch main menu
starter()