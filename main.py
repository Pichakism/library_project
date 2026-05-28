from src.models.books import Book
from src.storages.sqlite_storage import SqliteStorage
from src.storages.mysql_storage import MySqlStorage
from src.storages.postgreSql_storage import PostgreSqlStorage
from src.storages.sqlServer_storage import SqlServerStorage
from src.storages.sqlite_storage import SqliteStorage
from src.controler.book_controler import book_managment
from src.controler.member_controler import member_managment
from src.repositories.sqlite_repository import *
from src.bootstrap import Bootstrap

# Main entry point of the program
# - Initializes databases
# - Shows starter menu
# - Routes user to selected management module
def starter():
    bootstrap = Bootstrap(MySqlStorage(), PostgreSqlStorage(), SqliteStorage(), SqlServerStorage())
    bootstrap.run()
    print("\nApplication started...")
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