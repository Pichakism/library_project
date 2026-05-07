import csv
import os
from models.books import Book
from models.members import Member

def save_book_in_csv(book):
    file_path = "./data/book_data.csv"
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as file:
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
                "digital_version"
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
            book.digital_version.name
        ])
        print(f"\nBook \"{book.book_title}\" saved Successfully...")
    
def search_book(field, value):
    file_path = "./data/book_data.csv"
    with open(file_path, "r") as file:
        books = csv.DictReader(file)
        found = False
        for book in books:
            if book[field] == str(value):
                book_obj = Book(**book)
                print("\nBook found!:")
                print(book_obj)
                found = True
        if not found:
            print("Book not found!")

def save_member_in_csv(member):
    file_path = "./data/member_data.csv"
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow([
                "id",
                "first_name",
                "last_name",
                "phone_number",
                "member_status",
                "date"
            ])
        writer.writerow([
            member.id,
            member.first_name,
            member.last_name,
            member.phone_number,
            member.member_status.name,
            member.date
        ])
        print(f"\nMember \"{member.first_name} {member.last_name}\" saved Successfully...")

def search_member(field, value):
    file_path = "./data/member_data.csv"
    with open(file_path, "r") as file:
        members = csv.DictReader(file)
        found = False
        for member in members:
            if member[field] == str(value):
                member_obj = Member(**member)
                print("\nMember found!:")
                print(member_obj)
                found = True
        if not found:
            print("Member not found!")