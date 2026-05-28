from src.repositories import postgreSql_repository
from src.storages.postgreSql_storage import PostgreSqlStorage


class PostgreSqlService:
    def __init__(self):
        self.storage = PostgreSqlStorage()

    def search_book(self, column, value):
        data_list = []
        i = 1
        sqLite_columns = [
            "id", "isbn", "book_title", "author_name",
            "publication_year", "page_count", "genre", "book_status",
            "physical_version", "digital_version", "count"]
        search_results = postgreSql_repository.BookRepository.search_book(self, column, value)
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
        user_input = int(input("\nEnter Book Number: "))
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

        print(postgreSql_repository.BookRepository.update_book(self, column, value, updates))

    def search_member(self, column, value):
        data_list = []
        i = 1
        sqLite_columns = ["id", "first name", "last name", "phone number", "status", "join date"]
        search_results = postgreSql_repository.MemberRepository().search_member(column, value)
        print("\nYour data:")
        for row in search_results:
            data = dict(zip(sqLite_columns, row))
            data_list.append(data)
            print(f"\nMember Number {i}:")
            i += 1
            for key, value in data.items():
                print(f"{key} : {value}")
        return data_list

    def update_member(self, data, column, value):
        user_input = int(input("\nEnter Member Numbe: "))
        if user_input < 1 or user_input > len(data):
            print("\nInvalid member number...!")
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

        print(postgreSql_repository.MemberRepository.update_member(self, column, value, updates))
