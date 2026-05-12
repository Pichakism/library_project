import os
import csv
import pandas as pd

csv_book_file_path = "./data/book_data.csv"
csv_member_file_path = "./data/member_data.csv"
csv_loan_file_path = "./data/loan.csv"
class CsvStorage:

    def create_book_csv(self, book):
        file_exists = os.path.exists(csv_book_file_path)
        with open(csv_book_file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
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
                ])
            writer.writerow([
                book.isbn,
                book.book_title,
                book.auther_name,
                book.publication_year,
                book.page_count,
                book.genre,
                book.book_status.name,
                book.physical_version.name,
                book.digital_version.name,
                book.count,
            ])

    def create_member_csv(self, member):
        file_exists = os.path.exists(csv_member_file_path)
        with open(csv_member_file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    "id","first_name","last_name","phone_number","member_status","date"
                ])
            writer.writerow([
                member.id,
                member.first_name,
                member.last_name,
                member.phone_number,
                member.member_status,
                member.date

            ])

    def create_loan_csv(self, loan):
        file_exists = os.path.exists(csv_loan_file_path)
        with open(csv_loan_file_path, "a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow([
                    "id", "book_isbn", "member_id", "date"
                ])
            writer.writerow([
                loan.id,
                loan.book_isbn,
                loan.member_id,
                loan.date

            ])
            
    def load_dataframe(self, file_path):
        try:
            return pd.read_csv(file_path)
        except FileNotFoundError as e:
            print(e)
            return FileNotFoundError
        
    # Saves entire DataFrame to CSV file
    # - Overwrites existing file
    def save_dataframe(self, dataframe, file_path):
        dataframe.to_csv(file_path, index=False)