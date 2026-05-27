from src.repositories import sqlite_repository
from src.storages.sqlite_storage import SqliteStorage


class SqLiteService:
    def __init__(self):
        self.storage = SqliteStorage()

    def search_book(self, column, value):
        data_list = []
        i = 1
        sqLite_columns = [
            "id", "isbn", "title", "author_name",
            "publication year", "page count", "genre", "book status", "count"]
        search_results = sqlite_repository.BookRepository().search_book(column, value)
        print("\nYour data:")
        for row in search_results:
            data = dict(zip(sqLite_columns, row))
            data_list.append(data)
            print(f"\nBook Number {i}:")
            i += 1
            for key, value in data.items():
                print(f"{key} : {value}")
        return data_list

    def update_book(self, data, column, value):
        user_input = int(input("\nEnter Book Numbe: "))
        if user_input < 1 or user_input > len(data):
            print("\nInvalid book number...!")
            return
        selected_item = data[user_input - 1]

        print("\nEnter new values (Press Enter to skip):")

        updates = {}

        for key in selected_item.keys():
            current_value = selected_item[key]
            new_value = input(f"{key} (current: {current_value}): ")
            if new_value.strip() != "":
                updates[key] = new_value

        if not updates:
            print("No changes.")
            return

        print(sqlite_repository.BookRepository.update_book(self, column, value, updates))
