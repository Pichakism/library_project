# -------------------------
# MEMBER SERVICE LAYER
# -------------------------
# This service acts as a bridge between controller and repository layer
# It contains no user interaction logic
# It only delegates operations to repository and formats raw database output
class MemberService:
    def __init__(self, repo, storage):
        # Repository is responsible for all database operations
        # Storage is injected for abstraction and future extensibility (not used directly yet)
        self.repo = repo
        self.storage = storage

    # -------------------------
    # INSERT MEMBER
    # -------------------------
    # Sends member object to repository to be stored in database
    def insert_member(self, book):
        return self.repo.insert_member(book)

    # -------------------------
    # SELECT MEMBER
    # -------------------------
    # Retrieves raw rows from repository and converts them into structured dictionaries
    # to make them usable in controller/UI layer
    def select_member(self, column, value):
        rows = self.repo.select_member(column, value)
        return [
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "phone_number": row[3],
                "status": row[4],
                "join_date": row[5],
            }
            for row in rows
        ]

    # -------------------------
    # UPDATE MEMBER
    # -------------------------
    # Sends update request to repository with filter and new values
    def update_member(self, column, value, updates):
        return self.repo.update_member(column, value, updates)

    # -------------------------
    # DELETE MEMBER
    # -------------------------
    # Deletes member records based on given condition
    def delete_member(self, column, value):
        return self.repo.delete_member(column, value)