from src.storages.mysql_storage import MySqlStorage

class BookRepository:
    def __init__(self):
        self.storage = MySqlStorage()

    def select_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        
        query = f"""
            SELECT *
            FROM books
            WHERE {column} LIKE %s
        """
        try:
            results = self.storage.fetch_all(query, (f"%{value}%",))
            return results
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def insert_book(self, book):
        
        query = """
            INSERT INTO books (
                isbn,
                book_title,
                author_name,
                publication_year,
                page_count,
                genre,
                book_status,
                physical_version,
                digital_version,
                count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.storage.execute(
                query,
                (
                    book.isbn,
                    book.book_title,
                    book.author_name,
                    book.publication_year,
                    book.page_count,
                    book.genre,
                    book.book_status.name,
                    book.physical_version.name,
                    book.digital_version.name,
                    book.count
                )
            )
            return "\nBook added successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        
        query = f"""
            DELETE FROM books
            WHERE {column} = %s
        """
        try:
            self.storage.execute(query, (value,))
            return "\nBook deleted successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def update_book(self, column, value, updates):
        set_clause = ", ".join(f"{field} = %s" for field in updates)

        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = %s
        """
        params = (tuple(updates.values()) + (value,))

        try:
            self.storage.execute(query, params)
            return "\nBook updated successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

class MemberRepository:
    def __init__(self):
        self.storage = MySqlStorage()

    def select_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "status", "join_date"]

        if column not in allowed_column:
            raise ValueError("Invalide value...!")
        
        query = f"""
            SELECT *
            FROM members
            WHERE {column} LIKE %s
        """
            
        try:
            result = self.storage.fetch_all(query, (f"%{value}%",))
            return result
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def insert_member(self, member):
        query = """
            INSERT INTO members (
                first_name,
                last_name,
                phone_number,
                status,
                join_date) VALUES (%s, %s, %s, %s, %s)
        """
        try:
            self.storage.execute(
                query,
                (
                    member.first_name,
                    member.last_name,
                    member.phone_number,
                    member.member_status.name,
                    member.join_date
                )
            )
            return "\nMember added successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def delete_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name", "phone_number", "status", "join_date"]

        if column not in allowed_column:
            raise ValueError("Invalide value...!")
        
        query = f"""
            DELETE FROM members
            WHERE {column} = %s
        """

        try:
            self.storage.execute(query, (value,))
            return "\nMember deleted successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise

    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{field} = %s" for field in updates)

        query = f"""
            UPDATE members
            SET {set_clause}
            WHERE {column} = %s
        """
        params = (tuple(updates.values()) + (value,))

        try:
            self.storage.execute(query, params)
            return "\nMember updated successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise
        
    # TODO :                                                                                    
class LoanRepository:
    def __init__(self):
        self.storage = MySqlStorage()

    def select_loan(self, column, value):
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
            print("SQL ERROR:", e)
            raise

    def insert_loan(self, loan):
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
            return "\nLoan added successfully...\n"
        except Exception as e:
            print("SQL ERROR:", e)
            raise
    
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
            print("SQL ERROR:", e)
            raise