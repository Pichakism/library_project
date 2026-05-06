class Book:
    def __init__(self, book_title, auther_name, publication_year, book_id, page_count, genre, book_status):
        self.book_title = book_title
        self.auther_name = auther_name
        self.publication_year = publication_year
        self.book_id = book_id
        self.page_count = page_count
        self.genre = genre
        self.book_status = book_status
    
    def add_book(self):
        ...