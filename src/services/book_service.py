from src.repositories.sqlite_repository import BookRepository
from src.services.sync_manager import SyncManager
from src.services.sync_serrvice import SyncDB
import threading

class BookService:
    def __init__(self):
        self.sqlite_repo = BookRepository()
        self.sync_manager = SyncManager()

    def insert_book(self, book):
        self.sqlite_repo.insert_book(book)
        threading.Thread(
            target=SyncDB(self.sync_manager).sync_insert,
            args=(book,),
            daemon=True
        ).start()

    def select_book(self, column, value):
        rows = self.sqlite_repo.select_book(column, value)
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

    def update_book(self, column, value, updates):
        self.sqlite_repo.update_book(column, value, updates)
        threading.Thread(
            target=SyncDB(self.sync_manager).sync_update,
            args=(column, value, updates),
            daemon=True
        ).start()

    def delete_book(self, column, value):
        self.sqlite_repo.delete_book(column, value)
        threading.Thread(
            target=SyncDB(self.sync_manager).sync_delete,
            args=(column, value),
            daemon=True
        ).start()