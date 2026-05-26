from src.storages.sqlServer_storage import SqlServerStorage


class BookRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def search_book(self, column, value):
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

        results = self.storage.fetch_all(query, params)
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
                physical_version,
                digital_version,
                count
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                book.physical_version.name,
                book.digital_version.name,
                book.count
            )
        )
        print("\nBook added successfully...\n")

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

        self.storage.execute(query, params)
        print("\nBook deleted successfully...\n")

    def update_book(self, column, value, updates):
        set_clause = ", ".join(f"{field} = ?" for field in updates)

        query = f"""
            UPDATE books
            SET {set_clause}
            WHERE {column} = ?
        """

        params = tuple(updates.values()) + (value,)
        self.storage.execute(query, params)


# ==========================

class MemberRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def search_member(self, column, value):
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

        result = self.storage.fetch_all(query, params)
        print(result)

    def save_member(self, member):
        query = """
            INSERT INTO members (
                first_name,
                last_name,
                phone_number,
                status,
                join_date
            ) VALUES (?, ?, ?, ?, ?)
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
        allowed_column = ["id", "first_name", "last_name",
                          "phone_number", "member_status", "date"]

        if column not in allowed_column:
            raise ValueError("Invalid value...!")

        query = f"""
            DELETE FROM members
            WHERE {column} = ?
        """

        self.storage.execute(query, (value,))
        print("\nMember deleted successfully...\n")

    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{field} = ?" for field in updates)

        query = f"""
            UPDATE members
            SET {set_clause}
            WHERE {column} = ?
        """

        params = tuple(updates.values()) + (value,)
        self.storage.execute(query, params)


# ==========================

class LoanRepository:
    def __init__(self):
        self.storage = SqlServerStorage()

    def search_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...!")

        query = f"""
            SELECT *
            FROM loans
            WHERE {column} LIKE ?
        """

        results = self.storage.fetch_all(query, (f"%{value}%",))
        print(results)

    def save_loan(self, loan):
        query = """
            INSERT INTO loans (
                member_id,
                book_id,
                loan_date
            ) VALUES (?, ?, ?)
        """

        self.storage.execute(
            query,
            (
                loan.member_id,
                loan.book_id,
                loan.loan_date
            )
        )
        print("\nLoan added successfully...\n")

    def delete_loan(self, column, value):
        allowed_column = ["id", "book_id", "member_id", "loan_date"]

        if column not in allowed_column:
            raise ValueError("Invalid Value...!")

        query = f"""
            DELETE FROM loans
            WHERE {column} = ?
        """

        self.storage.execute(query, (value,))
        print("\nLoan deleted successfully...\n")