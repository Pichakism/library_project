import csv
import os
import pandas as pd
from src.models.books import Book
from src.models.members import Member
from src.storages.csv_storage import CsvStorage

csv_book_file_path = "./data/book_data.csv"
csv_member_file_path = "./data/member_data.csv"

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

# Saves a new book record into CSV file
# - Creates file and header if not exists
# - Appends book data as a new row
def save_book_in_csv(book):
    storage = CsvStorage()
    storage.create_csv(book)
    print(f"\nBook \"{book.book_title}\" saved Successfully...")
    
# Searches books in book DataFrame based on selected column and value
# - Uses find_rows() for filtering
# - Prints matching results or not found message
def search_book_in_csv(search_col, search_val):
    storage = CsvStorage()
    book_df = storage.load_dataframe(csv_book_file_path)
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

# Edits a book record in DataFrame and CSV
# - Searches matching rows
# - Lets user choose row index
# - Collects updated fields from user
# - Calls edit_row() to apply changes
def edit_book_in_csv(search_col, search_val):
    storage = CsvStorage()
    book_df = storage.load_dataframe(csv_book_file_path)
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
    
    book_df = edit_row(book_df, selected_index, updates, csv_book_file_path)
    print(f'\nRow {selected_index} updated successfully.')
    return

# Removes a book record from DataFrame and CSV
# - Searches matching rows
# - User selects row index
# - Calls delete_row() to remove it
def remove_book_in_csv(search_col, search_val):
    storage = CsvStorage()
    book_df = storage.load_dataframe(csv_book_file_path)
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
    book_df = delete_row(book_df, selected_index, csv_book_file_path)
    print(f'\nRow {selected_index} removed successfully.')
    return

# Saves a new member record into CSV file
# - Creates file and header if not exists
# - Appends member data as a new row
def save_member_in_csv(member):
    storage = CsvStorage()
    storage.create_csv(member)
    print(f"\nMember \"{member.first_name} {member.last_name}\" saved Successfully...")

# Searches a member in CSV file by field and value
# - Reads CSV using DictReader
# - Matches exact field value
# - Prints found member(s)
def search_member_in_csv(search_col, search_val):
    storage = CsvStorage()
    member_df = storage.load_dataframe(csv_member_file_path)
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

# Edits a member record in DataFrame and CSV
# - Searches matching rows
# - Lets user select row index
# - Collects updated fields
# - Calls edit_row() to save changes
def edit_member_in_csv(search_col, search_val):
    storage = CsvStorage()
    member_df = storage.load_dataframe(csv_member_file_path)
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
    
    member_df = edit_row(member_df, selected_index, updates, csv_member_file_path)
    print(f'\nRow {selected_index} updated successfully.')
    return

# Removes a member record from DataFrame and CSV
# - Searches matching rows
# - User selects row index
# - Calls delete_row() to remove it
def remove_member_in_csv(search_col, search_val):
    storage = CsvStorage()
    member_df = storage.load_dataframe(csv_member_file_path)
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
    member_df = delete_row(member_df, selected_index, csv_member_file_path)
    print(f'\nRow {selected_index} removed successfully.')
    return