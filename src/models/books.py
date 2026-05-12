# Represents a Book entity in the system
# - Stores all metadata related to a book
# - Used for creating book objects before saving to CSV
class Book:
    def __init__(self, isbn, book_title, auther_name, publication_year, page_count, genre, book_status, physical_version, digital_version, count):
        self.isbn = isbn
        self.book_title = book_title
        self.auther_name = auther_name
        self.publication_year = publication_year
        self.page_count = page_count
        self.genre = genre
        self.book_status = book_status
        self.physical_version = physical_version
        self.digital_version = digital_version
        self.count = count
    
    # Returns a formatted string representation of a Book object
    # - Used for printing book details in a readable format
    def __str__(self):
        return(
            f"ISBN = {self.isbn}\n"
            f"Book title = {self.book_title}\n"
            f"Auther name = {self.auther_name}\n"
            f"Publication date = {self.publication_year}\n"
            f"Page number = {self.page_count}\n"
            f"Genre = {self.genre}\n"
            f"Status = {self.book_status}\n"
            f"Physical version = {self.physical_version}\n"
            f"Digital version = {self.digital_version}\n"
            f"Count = {self.on_lone}\n"
        )