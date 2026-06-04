from src.storages.sqlite_storage import SqliteStorage

class BookRepository:
    def __init__(self):
        self.storage = SqliteStorage()

    def select_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]
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
                count) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            self.storage.execute_row(
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
            # print("SQL ERROR:", e)
            raise

    def delete_book(self, column, value):
        allowed_column = ["id", "book_isbn", "book_title", "author_name",
                          "publication_year", "page_count", "genre",
                          "book_status", "physical_version", "digital_version", "count"]
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
            # print("SQL ERROR:", e)
            raise

class MemberRepository:
    def __init__(self):
        self.storage = SqliteStorage()

    def select_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name", "phone_number", "status", "join_date"]
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
                join_date) VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.storage.execute_row(
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

    def update_member(self, column, value, updates):
        set_clause = ", ".join(f"{column} = ?" for column in updates)
        query = f"""
            UPDATE members
            SET {set_clause}
            WHERE {column} = ?
        """
        params = (tuple(updates.values()) + (value,))
        try:
            self.storage.execute_row(query, params)
            return "\nMember updated successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

    def delete_member(self, column, value):
        allowed_column = ["id", "member_nID", "first_name", "last_name", "phone_number", "status", "join_date"]
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
            # print("SQL ERROR:", e)
            raise

class LoanRepository:
    def __init__(self):
        self.storage = SqliteStorage()

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
            loan_date) VALUES (?, ?, ?)
        """
        try:
            self.storage.execute_row(
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
    
    def update_loan(self, column, value, updates):
        set_clause = ", ".join(f"{field} = %s" for field in updates)
        query = f"""
            UPDATE loans
            SET {set_clause}
            WHERE {column} = ?
        """
        params = (tuple(updates.values()) + (value,))
        try:
            self.storage.execute_row(query, params)
            return "\nMember updated successfully...\n"
        except Exception as e:
            # print("SQL ERROR:", e)
            raise

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
            results = self.storage.execute_row(query, (value,))
            print("ROWCOUNT =", results)
            return results
        except Exception as e:
            # print("SQL ERROR:", e)
            raise