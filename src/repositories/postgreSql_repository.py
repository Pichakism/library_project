from src.storages.postgreSql_storage import PostgreSqlStorage

class BookRepository:
    def __init__(self):
        self.storage = PostgreSqlStorage()

    def select_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]
        numeric_columns = ["id", "publication_year", "page_count", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        if column in numeric_columns:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} = %s
            """
            params = (value,)
        else:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} LIKE %s
            """
            params = (f"%{value}%",)
        
        try:
            results = self.storage.fetch_all(query, params)
            return results
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def insert_book(self, book):
        query = """
            INSERT INTO books (
                book_isbn,
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
                    book.book_isbn,
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
            # print("SQL ERROR:", e)
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]
        numeric_columns = ["id", "publication_year", "page_count", "count"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...")
        
        if column in numeric_columns:
            query = f"""
                DELETE FROM books
                WHERE {column} = %s
            """
            params = (value,)
        else:
            query = f"""
                DELETE FROM books
                WHERE {column} LIKE %s
            """
            params = (f"%{value}%",)
        try:
            self.storage.execute(query, params)
            return "\nBook deleted successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
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
            # print("SQL ERROR:", e)
            raise

class MemberRepository:
    def __init__(self):
        self.storage = PostgreSqlStorage()

    def select_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name", "phone_number", "status", "join_date"]

        if column not in allowed_column:
            raise ValueError("Invalide value...!")
        
        if column == "id":
            query = f"""
                        SELECT *
                        FROM members
                        WHERE {column} = %s
                    """
            params = (value,)
        else:
            query = f"""
                        SELECT *
                        FROM members
                        WHERE {column} LIKE %s
                    """
            params = (f"%{value}%",)
        
        try:
            result = self.storage.fetch_all(query, params)
            return result
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def insert_member(self, member):
        query = """
            INSERT INTO members (
                member_nID,
                first_name,
                last_name,
                phone_number,
                status,
                join_date) VALUES (%s, %s, %s, %s, %s, %s)
        """
        try:
            self.storage.execute(
                query,
                (
                    member.member_nID,
                    member.first_name,
                    member.last_name,
                    member.phone_number,
                    member.status.name,
                    member.join_date
                )
            )
            return "\nMember added successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def delete_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name", "phone_number", "status", "join_date"]
        print(column, type(column))
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
            # print("SQL ERROR:", e)
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
            # print("SQL ERROR:", e)
            raise
        
    # TODO :                                                                                    
class LoanRepository:
    def __init__(self):
        self.storage = PostgreSqlStorage()

    def select_loan(self, column, value):
        allowed_column = ["id", "book_isbn", "member_nID", "loan_date"]

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
            # print("SQL ERROR:", e)
            raise

    def insert_loan(self, loan):
        query = """
            INSERT INTO loans(
            book_isbn,
            member_nID,
            loan_date) VALUES (%s, %s, %s)
        """
        try:
            self.storage.execute(
                query,
                (
                    loan.book_isbn,
                    loan.member_nID,
                    loan.loan_date
                )
            )
            return "\nloan added successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise
    
    def update_loan(self):
        ...

    def delete_loan(self, column, value):
        allowed_column = ["id", "book_isbn", "member_nID", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalide Value...!")
        
        query = f"""
            DELETE
            FROM loans
            WHERE {column} = ?
        """
        try:
            results = self.storage.execute(query, (value,))
            return results
        except Exception as e:
            # print("SQL ERROR:", e)
            raise