from src.storages.oracle_storage import OracleStorage
class BookRepository:
    def __init__(self):
        self.storage = OracleStorage()

    def select_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre", "book_status",
                          "physical_version", "digital_version", "count"]
        numeric_columns = ["id", "publication_year", "page_count", "count"]
        if column not in allowed_column:
            raise ValueError("Invalid Value...")
        if column in numeric_columns:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} = :1
            """
            params = (value,)
        else:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} LIKE :1
            """
            params = (f"%{value}%",)
        try:
            results = self.storage.fetch_all(query, params)
            return results
        except Exception as e:
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
                count
            ) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)
        """
        try:
            affected = self.storage.execute(
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
            if affected == 0:
                raise Exception("[ORACLE] BOOK INSERT FAILED")
            return affected
        except Exception as e:
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre", "book_status",
                          "physical_version", "digital_version", "count"]
        numeric_columns = ["id", "publication_year", "page_count", "count"]
        if column not in allowed_column:
            raise ValueError("Invalid Value...")
        if column in numeric_columns:
            query = f"""
                DELETE FROM books
                WHERE {column} = :1
            """
            params = (value,)
        else:
            query = f"""
                DELETE FROM books
                WHERE {column} LIKE :1
            """
            params = (f"%{value}%",)
        try:
            affected = self.storage.execute(query, params)
            if affected == 0:
                raise Exception("[ORACLE] BOOK DELETE FAILED")
            return affected
        except Exception as e:
            raise

    def update_book(self, column, value, updates):
        set_clause = ", ".join(f"{field} = :{i}" for i, field in enumerate(updates.keys(), start=1))
        where_placeholder = len(updates) + 1
        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = :{where_placeholder}
        """
        params = tuple(updates.values()) + (value,)
        try:
            affected = self.storage.execute(query, params)
            if affected == 0:
                raise Exception("[ORACLE] BOOK UPDATE FAILED")
            return affected
        except Exception as e:
            raise

class MemberRepository:
    def __init__(self):
        self.storage = OracleStorage()

    def select_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name",
                          "phone_number", "status", "date"]
        if column not in allowed_column:
            raise ValueError("Invalid value...!")
        if column == "id":
            query = f"""
                SELECT *
                FROM members
                WHERE {column} = :1
            """
            params = (value,)
        else:
            query = f"""
                SELECT *
                FROM members
                WHERE {column} LIKE :1
            """
            params = (f"%{value}%",)
        try:
            result = self.storage.fetch_all(query, params)
            return result
        except Exception:
            raise

    def insert_member(self, member):
        query = """
            INSERT INTO members (
                member_nID,
                first_name,
                last_name,
                phone_number,
                status,
                join_date
            ) VALUES (:1, :2, :3, :4, :5, TO_DATE(:6, 'YYYY-MM-DD'))
        """
        try:
            affected = self.storage.execute(
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
            if affected == 0:
                raise Exception("[ORACLE] MEMBER INSERT FAILED")
            return affected
        except Exception:
            raise

    def delete_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name",
                          "phone_number", "status", "date"]
        if column not in allowed_column:
            raise ValueError("Invalid value...!")
        query = f"""
            DELETE FROM members
            WHERE {column} = :1
        """
        try:
            affected = self.storage.execute(query, (value,))
            if affected == 0:
                raise Exception("[ORACLE] MEMBER DELETE FAILED")
            return affected
        except Exception:
            raise

    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{field} = :{i+1}" for i, field in enumerate(updates))
        query = f"""
            UPDATE members
            SET {set_clause}
            WHERE {column} = :{len(updates)+1}
        """
        params = tuple(updates.values()) + (value,)
        try:
            affected = self.storage.execute(query, params)
            if affected == 0:
                raise Exception("[ORACLE] MEMBER UPDATE FAILED")
            return affected
        except Exception:
            raise
        
class LoanRepository:
    def __init__(self):
        self.storage = OracleStorage()

    def select_loan(self, column, value):
        allowed_column = ["id", "book_isbn", "member_nID", "loan_date"]
        if column not in allowed_column:
            raise ValueError("Invalid Value...!")
        query = f"""
            SELECT *
            FROM loans
            WHERE {column} LIKE :1
        """
        try:
            results = self.storage.fetch_all(query, (f"%{value}%",))
            return results
        except Exception:
            raise

    def insert_loan(self, loan):
        query = """
            INSERT INTO loans (
                book_isbn,
                member_nID,
                loan_date
            ) VALUES (:1, :2, :3)
        """
        try:
            affected = self.storage.execute(
                query,
                (
                    loan.book_isbn,
                    loan.member_nID,
                    loan.loan_date
                )
            )
            if affected == 0:
                raise Exception("[ORACLE] LOAN INSERT FAILED")
            return affected
        except Exception:
            raise

    def update_loan(self, column, value, updates):
        set_clause = ", ".join(f"{field} = :{i+1}" for i, field in enumerate(updates))
        query = f"""
            UPDATE loans
            SET {set_clause}
            WHERE {column} = :{len(updates)+1}
        """
        params = tuple(updates.values()) + (value,)
        try:
            affected = self.storage.execute(query, params)
            if affected == 0:
                raise Exception("[ORACLE] LOAN UPDATE FAILED")
            return affected
        except Exception:
            raise

    def delete_loan(self, column, value):
        allowed_column = ["id", "book_isbn", "member_nID", "loan_date"]
        if column not in allowed_column:
            raise ValueError("Invalid Value...!")
        query = f"""
            DELETE FROM loans
            WHERE {column} = :1
        """
        try:
            affected = self.storage.execute(query, (value,))
            if affected == 0:
                raise Exception("[ORACLE] LOAN DELETE FAILED")
            return affected
        except Exception:
            raise