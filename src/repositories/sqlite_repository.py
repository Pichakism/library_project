from src.storages.sqlite_storage import SqliteStorage

class BookRepository:
    def __init__(self):
        self.storage = SqliteStorage()

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
        print("\nBook added successfully...\n")

    # TODO :                                                                                    
    def update_book(self):
        ...

    def delete_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name", "publication_year", "page_count", "genre", "book_status", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    DELETE FROM books
                    WHERE {column} = ?
                """
        results = self.storage.execute_row(query, (value,))
        print("\nBook deleted successfully...\n")

class MemberRepository:
    def __init__(self):
        self.storage = SqliteStorage()

    def search_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    SELECT *
                    FROM members
                    WHERE {column} LIKE ?
                """
        results = self.storage.fetch_all(query, (f"%{value}%",))
        print(results)

    def save_member(self, member):
        query = """
                    INSERT INTO members (
                        first_name,
                        last_name,
                        phone_number,
                        status,
                        join_date) VALUES (?, ?, ?, ?, ?)
                """
        self.storage.execute_row(
            query,
            (
                member.first_name,
                member.last_name,
                member.phone_number,
                member.member_status.name,
                member.date
            )
        )
        print("\nMember added successfully...\n")

    # TODO :                                                                                    
    def update_member(self):
        ...

    def delete_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    DELETE FROM members
                    WHERE {column} = ?
                """
        results = self.storage.execute_row(query, (value,))
        print("\nMember deleted successfully...\n")

class LoanRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # TODO :                                                                                    
    def search_loan(self):
        ...

    def save_loan(self):
        ...
    
    def update_loan(self):
        ...

    def delete_loan(self):
        ...