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

    # TODO :                                                                                    
    def update_book(self, column, value, updates):
        set_clause = ", ".join(
            f"{column} = %s"
            for column in updates
        )
        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = %s
        """
        params = (tuple(updates.values()) + (value,))
        self.storage.execute(query, params)

class MemberRepository:
    def __init__(self):
        self.storage = MySqlStorage()

    def search_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "status", "join_date"]

        if column not in allowed_column:
            raise ValueError("Invalide value...!")
        
        query = f"""
                    SELECT *
                    FROM members
                    WHERE {column} LIKE %s
                """
        
        result = self.storage.fetch_all(query, (f"%{value}%",))
        print(result)

    def save_member(self, member):
        query = """
                    INSERT INTO members (
                        first_name,
                        last_name,
                        phone_number,
                        status,
                        join_date) VALUES (%s, %s, %s, %s, %s)
                """
        self.storage.execute(
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

    def delete_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "status", "join_date"]

        if column not in allowed_column:
            raise ValueError("Invalide value...!")
        
        query = f"""
                    DELETE FROM members
                    WHERE {column} = %s
                """

        self.storage.execute(query, (value,))
        print("\nMember deleted successfully...\n")

    # TODO :                                                                                    
    def update_member(self, column, value, updates):
        set_clause = ", ".join(
            f"{column} = %s"
            for column in updates
        )
        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = %s
        """
        params = (tuple(updates.values()) + (value,))
        self.storage.execute(query, params)
        
    # TODO :                                                                                    
class LoanRepository:
    def __init__(self):
        self.storage = MySqlStorage()

    def search_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    SELECT *
                    FROM loans
                    WHERE {column} LIKE ?
                """
        results = self.storage.fetch_all(query, (f"%{value}%",))
        print(results)

    def save_loan(self, loan):
        query = """INSERT INTO loans(
                    member_id,
                    book_id,
                    loan_date) VALUES (%s, %s, %s)
                """
        self.storage.execute_row(
            query,
            (
                loan.member_id,
                loan.book_id,
                loan.loan_date
            )
        )
        print("\nloan added successfully...\n")
    
    def update_loan(self):
        ...

    def delete_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
                    DELETE
                    FROM loans
                    WHERE {column} = ?
                """
        results = self.storage.fetch_all(query, (value,))
        print(results)