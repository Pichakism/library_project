from src.storages.mysql_storage import MySqlStorage

class BookRepositort:
    def __init__(self):
        self.storage = MySqlStorage()

    def search_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name", "publication_year", "page_count", "genre", "book_status", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        
        query = f"""
                    SELECT *
                    FROM books
                    WHERE {column} LIKE %s
                """
        
        results = self.storage.fetch_all(query, (f"%{value}%",))
        print(results)

    def save_book(self, book):
        query = """
                    INSERT INTO books (
                        isbn,
                        book_title,
                        author_name,
                        publication_year,
                        page_count,
                        genre,
                        book_status,
                        count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
        self.storage.execute(
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
        print("\nBook added successfully...\n")

    def delete_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name", "publication_year", "page_count", "genre", "book_status", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        
        query = f"""
                    DELETE FROM books
                    WHERE {column} = %s
                """
        
        self.storage.execute(query, (value,))
        print("\nBook deleted successfully...\n")