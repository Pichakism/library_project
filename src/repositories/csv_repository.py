import csv
import os
import datetime
from src.services.gtj import gregorian_to_jalali
import pandas as pd
from src.models.books import Book
from src.models.members import Member
from src.models.loan import Loan
from src.storages.csv_storage import CsvStorage


# Finds rows in a DataFrame based on a column and search value
# - Uses case-insensitive partial matching (contains)
def find_rows(dataframe, column_name, search_value):
    matching_rows = dataframe[dataframe[column_name].astype(str).str.contains(search_value, case=False, na=False)]
    return matching_rows

# Edits a specific row in a DataFrame
# - Applies updates to selected columns
# - Converts numeric columns if needed
# - Saves updated DataFrame to CSV
def edit_row(dataframe, row_index, updates, file_path):
    storage = CsvStorage()
    for col, new_val in updates.items():
        col_dtype = dataframe[col].dtype
        if pd.api.types.is_numeric_dtype(col_dtype):
            dataframe[col] = dataframe[col].astype(object)
        dataframe.loc[row_index, col] = str(new_val)
    return storage.save_dataframe(dataframe, file_path)

# Deletes a row from DataFrame by index
# - Resets index after deletion
# - Saves updated DataFrame to CSV
def delete_row(dataframe, row_index, file_path):
    storage = CsvStorage()
    dataframe = dataframe.drop(index=row_index)
    dataframe = dataframe.reset_index(drop=True)
    return storage.save_dataframe(dataframe, file_path)

class BookRepository:
    def __init__(self, file_path="./data/book_data.csv"):
        self.storage = CsvStorage()
        self.file_path = file_path
        self.header = [
                        "id",
                        "isbn",
                        "book_title",
                        "auther_name",
                        "publication_year",
                        "page_count",
                        "genre",
                        "book_status",
                        "physical_version",
                        "digital_version",
                        "count"
                    ]

    # Saves a new book record into CSV file
    # - Creates file and header if not exists
    # - Appends book data as a new row
    def save_book_in_csv(self, book):
        file_exists = self.storage.create_file(self.file_path,self.header)
        if file_exists:
            new_id = self.storage._get_last_id(self.file_path) + 1
            self.storage.add_book_to_csv(self.file_path, book, new_id)
            print(f"\nBook \"{book.book_title}\" saved Successfully...")
        else:
            print("\nFile Not Found...!")

    # Searches books in book DataFrame based on selected column and value
    # - Uses find_rows() for filtering
    # - Prints matching results or not found message
    def search_book_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path,self.header)
        if file_exists:
            book_df = self.storage.load_dataframe(self.file_path)
            member_search_col = book_df.columns[search_col - 1]
            matching_rows = find_rows(book_df, member_search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
        else:
            print("\nFile Not Found...!")

    # Removes a book record from DataFrame and CSV
    # - Searches matching rows
    # - User selects row index
    # - Calls delete_row() to remove it
    def remove_book_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path,self.header)
        if file_exists:
            book_df = self.storage.load_dataframe(self.file_path)
            search_col = book_df.columns[search_col - 1]
            matching_rows = find_rows(book_df, search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
            try:
                selected_index = int(input("\nWhich row index do you want to remove? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index not in matching_rows.index:
                print("\nInvalid row index...!")
                return
            book_df = delete_row(book_df, selected_index, self.file_path)
            print(f'\nRow {selected_index} removed successfully.')
            return
        else:
            print("\nFile Not Found...!")

    # Edits a book record in DataFrame and CSV
    # - Searches matching rows
    # - Lets user choose row index
    # - Collects updated fields from user
    # - Calls edit_row() to apply changes
    def edit_book_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path,self.header)
        if file_exists:
            book_df = self.storage.load_dataframe(self.file_path)
            search_col = book_df.columns[search_col - 1]
            matching_rows = find_rows(book_df, search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
            try:
                selected_index = int(input("\nWhich row index do you want to edit? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index not in matching_rows.index:
                print("\nInvalid row index...!")
                return
            selected_row = book_df.loc[[selected_index]]
            updates = {}
            print(
                "\nEnter a new value: "
                "(Press Enter to skip)"
            )
            for col in book_df.columns:
                current_value = selected_row.iloc[0][col]
                new_value = input(
                    f"{col} "
                    f"(current: {current_value}): "
                )
                if new_value:
                    updates[col] = new_value
            
            if not updates:
                print("No changes.")
                return
            
            book_df = edit_row(book_df, selected_index, updates, self.file_path)
            print(f'\nRow {selected_index} updated successfully.')
            return

class MemberRepository:
    def __init__(self, file_path="./data/member_data.csv"):
        self.storage = CsvStorage()
        self.file_path = file_path
        self.header = ["id","first_name","last_name","phone_number","member_status","date"]

    # Saves a new member record into CSV file
    # - Creates file and header if not exists
    # - Appends member data as a new row
    def save_member_in_csv(self, member):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            new_id = self.storage._get_last_id(self.file_path) + 1
            self.storage.add_member_to_csv(self.file_path, member, new_id)
            print(f"\nMember \"{member.first_name} {member.last_name}\" saved Successfully...")
        else:
            print("\nFile Not Found...!")

    # Searches a member in CSV file by field and value
    # - Reads CSV using DictReader
    # - Matches exact field value
    # - Prints found member(s)
    def search_member_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            member_df = self.storage.load_dataframe(self.file_path)
            member_search_col = member_df.columns[search_col - 1]
            matching_rows = find_rows(member_df, member_search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
        else:
            print("\nFile Not Found...!")

    # Removes a member record from DataFrame and CSV
    # - Searches matching rows
    # - User selects row index
    # - Calls delete_row() to remove it
    def remove_member_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            member_df = self.storage.load_dataframe(self.file_path)
            search_col = member_df.columns[search_col - 1]
            matching_rows = find_rows(member_df, search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
            try:
                selected_index = int(input("\nWhich row index do you want to remove? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index not in matching_rows.index:
                print("\nInvalid row index...!")
                return
            member_df = delete_row(member_df, selected_index, self.file_path)
            print(f'\nRow {selected_index} removed successfully.')
            return
        else:
            print("\nFile Not Found...!")

    # Edits a member record in DataFrame and CSV
    # - Searches matching rows
    # - Lets user select row index
    # - Collects updated fields
    # - Calls edit_row() to save changes
    def edit_member_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            member_df = self.storage.load_dataframe(self.file_path)
            search_col = member_df.columns[search_col - 1]
            matching_rows = find_rows(member_df, search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
            try:
                selected_index = int(input("\nWhich row index do you want to edit? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index not in matching_rows.index:
                print("\nInvalid row index...!")
                return
            selected_row = member_df.loc[[selected_index]]
            updates = {}
            print(
                "\nEnter a new value: "
                "(Press Enter to skip)"
            )
            for col in member_df.columns:
                current_value = selected_row.iloc[0][col]
                new_value = input(
                    f"{col} "
                    f"(current: {current_value}): "
                )
                if new_value:
                    updates[col] = new_value
            
            if not updates:
                print("No changes.")
                return
            
            member_df = edit_row(member_df, selected_index, updates, self.file_path)
            print(f'\nRow {selected_index} updated successfully.')
            return
        else:
            print("\nFile Not Found...!")

class LoanRepository:
    def __init__(self, file_path="./data/loan.csv"):
        self.storage = CsvStorage()
        self.file_path = file_path
        self.header = ["id", "book_isbn", "member_id", "date"]

    """def save_loan_in_csv(self, loan):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            self.storage.add_loan_to_csv(loan)
            print(f"\nBook \"{loan.book_isbn} for {loan.member_id}\" saved Successfully...")
        else:
            print("\nFile Not Found...!")"""

    def loan_book_in_csv(self, search_column_for_book, search_value_for_book, search_column_for_member, search_value_for_member):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            new_id = self.storage._get_last_id(self.file_path) + 1
            book_df = self.storage.load_dataframe(str(BookRepository().file_path))
            member_search_col = book_df.columns[search_column_for_book]
            matching_rows_1 = find_rows(book_df, member_search_col, search_value_for_book)
            if matching_rows_1.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows{member_search_col} with value: \"{search_value_for_book}\" found.")
                print("*" * 40)
                return
            matching_rows_1_reset = matching_rows_1.reset_index(drop=True, inplace=True)
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows_1)
            print("*" * 120)
            member_df = self.storage.load_dataframe(str(MemberRepository().file_path))
            search_col = member_df.columns[search_column_for_member - 1]
            matching_rows_2 = find_rows(member_df, search_col, search_value_for_member)
            if matching_rows_2.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_value_for_member}\" found.")
                print("*" * 40)
                return
            matching_rows_2_reset = matching_rows_2.reset_index(drop=True, inplace=True)
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows_2)
            print("*" * 120)

            try:
                selected_index_1 = int(input("\nWhich row index in book do you want? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            try:
                selected_index_2 = int(input("\nWhich row index in member do you want? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index_1 not in matching_rows_1.index or selected_index_2 not in matching_rows_2.index:
                print("\nInvalid row index...!")
                return
            # print(matching_rows_1.iloc[selected_index_1, 0], matching_rows_2.iloc[selected_index_2, 0])
            loan = Loan(matching_rows_1.iloc[selected_index_1, 1],
                        matching_rows_2.iloc[selected_index_2, 0],
                        gregorian_to_jalali(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day))
            self.storage.add_loan_to_csv(self.file_path, loan, new_id)
            print(f'\nRow {selected_index_1} append successfully.')
            return
        else:
            print("\nFile Not Found...!")
    
    # TODO :                                                                                    
    def remove_loan_in_csv(self, search_col, search_val):
        file_exists = self.storage.create_file(self.file_path, self.header)
        if file_exists:
            member_df = self.storage.load_dataframe(self.file_path)
            search_col = member_df.columns[search_col - 1]
            matching_rows = find_rows(member_df, search_col, search_val)
            if matching_rows.empty:
                print("\n")
                print("*" * 40)
                print(f"No rows with value: \"{search_val}\" found.")
                print("*" * 40)
                return
            print("\n")
            print("*" * 120)
            print("Rows found:\n\n", matching_rows)
            print("*" * 120)
            try:
                selected_index = int(input("\nWhich row index do you want to remove? : "))
            except ValueError:
                print("\nInvalid value!!!")
                return
            if selected_index not in matching_rows.index:
                print("\nInvalid row index...!")
                return
            member_df = delete_row(member_df, selected_index, self.file_path)
            print(f'\nRow {selected_index} removed successfully.')
            return
        else:
            print("\nFile Not Found...!")
