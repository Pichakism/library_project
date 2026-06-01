from src.repositories.sqlite_repository import LoanRepository
from src.services.sync_data.sync_manager import SyncManager
from src.services.sync_data.sync_serrvice import SyncDBForLoan
import threading
class LoanService:
    def __init__(self):
        self.sqlite_repo = LoanRepository()
        self.sync_manager = SyncManager()

    def insert_loan(self, loan):
        self.sqlite_repo.insert_loan(loan)
        threading.Thread(
            target=SyncDBForLoan(self.sync_manager).sync_insert,
            args=(loan,),
            daemon=True
        ).start()

    def select_loan(self, column, value):
        rows = self.sqlite_repo.select_loan(column, value)
        return [
            {
                "id": row[0],
                "book_isbn": row[1],
                "member_nID": row[2],
                "loan_date": row[3],
            }
            for row in rows
        ]

    def update_loan(self, column, value, updates):
        self.sqlite_repo.update_loan(column, value, updates)
        threading.Thread(
            target=SyncDBForLoan(self.sync_manager).sync_update,
            args=(column, value, updates),
            daemon=True
        ).start()
    def delete_loan(self, column, value):
        self.sqlite_repo.delete_loan(column, value)
        threading.Thread(
            target=SyncDBForLoan(self.sync_manager).sync_delete,
            args=(column, value),
            daemon=True
        ).start()