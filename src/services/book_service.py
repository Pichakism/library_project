# -------------------------
# BOOK SERVICE LAYER
# -------------------------
# This service acts as a bridge between controller and repository layer
# It does NOT handle user input/output logic
# It only delegates operations to repository and formats raw data if needed
class BookService:
    def __init__(self, repo, storage):
        # Repository handles database operations
        # Storage is injected for future abstraction (not directly used here yet)
        self.repo = repo
        self.storage = storage

    # -------------------------
    # INSERT BOOK
    # -------------------------
    # Sends Book object to repository for insertion
    def insert_book(self, book):
        return self.repo.insert_book(book)

    # -------------------------
    # SELECT BOOK
    # -------------------------
    # Retrieves raw rows from repository and converts them into dictionary format
    # to make data easier for controller/UI layer
    def select_book(self, column, value):
        rows = self.repo.select_book(column, value)
        return [
            {
                "id": row[0],
                "isbn": row[1],
                "book_title": row[2],
                "author_name": row[3],
                "publication_year": row[4],
                "page_count": row[5],
                "genre": row[6],
                "book_status": row[7],
                "physical_version": row[8],
                "digital_version": row[9],
                "count": row[10],
            }
            for row in rows
        ]

    # -------------------------
    # UPDATE BOOK
    # -------------------------
    # Sends update request to repository with selected filters and new values
    def update_book(self, column, value, updates):
        return self.repo.update_book(column, value, updates)

    # -------------------------
    # DELETE BOOK
    # -------------------------
    # Deletes book records matching given condition
    def delete_book(self, column, value):
        return self.repo.delete_book(column, value)

    # -------------------------
    # LOAN BOOK
    # -------------------------
    # Delegates loan operation between book and member to repository layer
    def loan_book(self, book_search, member_search):
        return self.repo.loan_book(
            book_search[0],
            book_search[1],
            member_search[0],
            member_search[1]
        )