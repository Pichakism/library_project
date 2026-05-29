from src.storages.sqlServer_storage import SqlServerStorage


class BookRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def select_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version",
                          "digital_version", "count"]

        numeric_columns = ["id", "publication_year", "page_count", "count"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...")

        if column in numeric_columns:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} = ?
            """
            params = (value,)
        else:
            query = f"""
                SELECT *
                FROM books
                WHERE {column} LIKE ?
            """
            params = (f"%{value}%",)
        try:
            results = self.storage.fetch_all(query, params)
            return results
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def insert_book(self, book, from_queue=False):
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
                count
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            # print("SQL ERROR:", e)
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version",
                          "digital_version", "count"]

        numeric_columns = ["id", "publication_year", "page_count", "count"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...")

        if column in numeric_columns:
            query = f"""
                DELETE FROM books
                WHERE {column} = ?
            """
            params = (value,)
        else:
            query = f"""
                DELETE FROM books
                WHERE {column} LIKE ?
            """
            params = (f"%{value}%",)

        try:
            self.storage.execute(query, params)
            return "\nBook deleted successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def update_book(self, column, value, updates):
        set_clause = ", ".join(f"{field} = ?" for field in updates)

        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = ?
        """

        params = tuple(updates.values()) + (value,)
        try:
            self.storage.execute(query, params)
            return "\nBook deleted successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise
        
class MemberRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def select_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name",
                          "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalid value...!")

        if column == "id":
            query = f"""
                SELECT *
                FROM members
                WHERE {column} = ?
            """
            params = (value,)
        else:
            query = f"""
                SELECT *
                FROM members
                WHERE {column} LIKE ?
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
                first_name,
                last_name,
                phone_number,
                status,
                join_date
            ) VALUES (?, ?, ?, ?, ?)
        """

        try:
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
            return "\nMember added successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def delete_member(self, column, value):
        allowed_column = ["id", "first_name", "last_name",
                          "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalid value...!")

        query = f"""
            DELETE FROM members
            WHERE {column} = ?
        """

        try:
            self.storage.execute(query, (value,))
            return "\nMember deleted successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{field} = ?" for field in updates)

        query = f"""
            UPDATE members
            SET {set_clause}
            WHERE {column} = ?
        """

        params = tuple(updates.values()) + (value,)
        try:
            self.storage.execute(query, params)
            return "\nMember updated successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

class LoanRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def select_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...!")

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
            INSERT INTO loans (
                member_id,
                book_id,
                loan_date
            ) VALUES (?, ?, ?)
        """

        try:
            self.storage.execute(
                query,
                (
                    loan.member_id,
                    loan.book_id,
                    loan.loan_date
                )
            )
            return "\nLoan added successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def delete_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...!")

        query = f"""
            DELETE FROM loans
            WHERE {column} = ?
        """

        try:
            self.storage.execute(query, (value,))
            return "\nLoan deleted successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise