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

        try:
            results = self.storage.fetch_all(query, (f"%{value}%",))
            return results
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def save_book(self, book):
        query = """
            INSERT INTO books (
                isbn,
                book_title,
                author_name,
                publication_year,
                page_count,
                genre,
                status,
                count) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        try:
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
            return "\nBook added successfully...\n"
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    # TODO :                                                                                    
    def update_book(self, column, value, updates):
        set_clause = ", ".join(f"{field} = ?" for field in updates)
        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = ?
        """
        params = (tuple(updates.values()) + (value,))
        try:
            self.storage.execute_row(query, params)
            return "\nBook updated successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name", "publication_year", "page_count", "genre", "book_status", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
            DELETE FROM books
            WHERE {column} = ?
        """
        try:
            self.storage.execute_row(query, (value,))
            return "\nBook deleted successfully...\n"
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

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
        try:
            results = self.storage.fetch_all(query, (f"%{value}%",))
            return results
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    def save_member(self, member):
        query = """
            INSERT INTO members (
                first_name,
                last_name,
                phone_number,
                status,
                join_date) VALUES (?, ?, ?, ?, ?)
        """
        try:
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
            return "\nMember added successfully...\n"
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    # TODO :                                                                                    
    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{column} = %s" for column in updates)
        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = %s
        """
        params = (tuple(updates.values()) + (value,))
        try:
            self.storage.execute_row(query, params)
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    def delete_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
            DELETE FROM members
            WHERE {column} = ?
        """
        try:
            self.storage.execute_row(query, (value,))
            return "\nMember deleted successfully...\n"
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    # TODO :                                                                                    
class LoanRepository:
    def __init__(self):
        self.storage = SqliteStorage()

    def search_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
            SELECT *
            FROM loans
            WHERE {column} LIKE ?
        """
        try:
            results = self.storage.fetch_all(query, (f"%{value}%",))
            return results
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")

    def save_loan(self, loan):
        query = """
            INSERT INTO loans(
            member_id,
            book_id,
            loan_date) VALUES (%s, %s, %s)
        """
        try:
            self.storage.execute_row(
                query,
                (
                    loan.member_id,
                    loan.book_id,
                    loan.loan_date
                )
            )
            return "\nloan added successfully...\n"
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")
    
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
        try:
            results = self.storage.fetch_all(query, (value,))
            return results
        except Exception as e:
            raise ConnectionError("ERROR: DB Connection Failed...!")