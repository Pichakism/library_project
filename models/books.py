import csv  
class Book:
    def __init__(self, isbn, book_title, auther_name, publication_year, page_count, genre, book_status):
        self.isbn = isbn
        self.book_title = book_title
        self.auther_name = auther_name
        self.publication_year = publication_year
        self.page_count = page_count
        self.genre = genre
        self.book_status = book_status
    