from src.repositories.sqlite_repository import MemberRepository
from src.services.sync_data.sync_manager import SyncManager
from src.services.sync_data.sync_serrvice import SyncDBForMember
import threading

class MemberService:
    def __init__(self):
        self.sqlite_repo = MemberRepository()
        self.sync_manager = SyncManager()

    def insert_member(self, member):
        self.sqlite_repo.insert_member(member)
        threading.Thread(
            target=SyncDBForMember(self.sync_manager).sync_insert,
            args=(member,),
            daemon=True
        ).start()

    def select_member(self, column, value):
        rows = self.sqlite_repo.select_member(column, value)
        return [
            {
                "id": row[0],
                "member_nID": row[1],
                "first_name": row[2],
                "last_name": row[3],
                "phone_number": row[4],
                "status": row[5],
                "join_date": row[6],
            }
            for row in rows
        ]

    def update_member(self, column, value, updates):
        self.sqlite_repo.update_member(column, value, updates)
        threading.Thread(
            target=SyncDBForMember(self.sync_manager).sync_update,
            args=(column, value, updates),
            daemon=True
        ).start()

    def delete_member(self, column, value):
        self.sqlite_repo.delete_member(column, value)
        threading.Thread(
            target=SyncDBForMember(self.sync_manager).sync_delete,
            args=(column, value),
            daemon=True
        ).start()