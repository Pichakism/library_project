from src.storages.sqlite_storage import SqliteStorage

class BookRepository:
    def __init__(self):
        self.storage = SqliteStorage()

    # NOTE: book func...:
    def search_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name", "publication_year", "page_count", "genre", "book_status", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    SELECT *
                    FROM books
                    WHERE {column} LIKE ?
                """
        results = self.storage.fetch_all(query, (f"%{value}%",))
        print(results)


    def save_book(self, book):
        query = """
                    INSERT INTO books (
                        isbn,
                        title,
                        author_name,
                        publication_year,
                        page_count,
                        genre,
                        status,
                        count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """
        self.storage.execute_row(
            query,
            (
                book.isbn,
                book.book_title,
                book.auther_name,
                book.publication_year,
                book.page_count,
                book.genre,
                book.book_status.name,
                book.count
            )
        )
        print("\nData add successfully...\n")

    def update_book(self):
        ...

    def delete_book(self):
        ...

class MemberRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # NOTE: member func...:
    def search_member(self):
        ...

    def save_member(self):
        ...

    def update_member(self):
        ...

    def delete_member(self):
        ...

class LoanRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # NOTE: loan func...:
    def search_loan(self):
        ...

    def save_loan(self):
        ...
    
    def update_loan(self):
        ...

    def delete_loan(self):
        ...