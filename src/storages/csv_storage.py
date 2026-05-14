import os
import csv
import pandas as pd

csv_book_file_path = "./data/book_data.csv"
csv_member_file_path = "./data/member_data.csv"
csv_loan_file_path = "./data/loan.csv"
class CsvStorage:

    def __init__(self):
        # self.file_path = file_path
        ...

    def create_file(self, file_path, header):
        try:
            if not os.path.exists(file_path):
                with open(file_path, "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
            return True
        except Exception as e:
            print(e)
            return False
            
    def add_book_to_csv(self, file_path, book, id):
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                id,
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

    def add_member_to_csv(self, file_path, member, id):
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                id,
                member.first_name,
                member.last_name,
                member.phone_number,
                member.member_status,
                member.date
            ])

    def add_loan_to_csv(self, file_path, loan, id):
        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                id,
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

    
    def _get_last_id(self, file_path):
        with open(file_path, "r", newline="") as f:
            reader = list(csv.reader(f))
            if len(reader) <= 1:
                return 0
            return int(reader[-1][0])