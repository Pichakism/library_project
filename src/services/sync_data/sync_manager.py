from src.services.repository_registry import get_book_repository, get_member_repository, get_loan_repository
from src.services.sync_data.sync_queue import SyncQueue
from src.utils.logger import write_sync_log
from src.models.books import Book
from src.models.members import Member
from src.models.loan import Loan
from src.models.status import (Book_Status, Physical_version, Digital_version, Member_Status)

def build_book_object(data):
    return Book(
        data["book_isbn"],
        data["book_title"],
        data["author_name"],
        data["publication_year"],
        data["page_count"],
        data["genre"],
        Book_Status(data["book_status"]),
        Physical_version(data["physical_version"]),
        Digital_version(data["digital_version"]),
        data["count"]
    )
def build_member_object(data):
    return Member(
        data["member_nID"],
        data["first_name"],
        data["last_name"],
        data["phone_number"],
        Member_Status(data["status"]),
        data["join_date"]
    )
def build_loan_object(data):
    return Loan(
        data["book_isbn"],
        data["member_nID"],
        data["loan_date"]
    )

def serialize_data(obj):
    if hasattr(obj, "__dict__"):
        data = obj.__dict__.copy()
        for k, v in data.items():
            if hasattr(v, "value"):
                data[k] = v.value
            else:
                data[k] = str(v)
        return data
    return obj

class SyncManager:
    def __init__(self):
        self.queue = SyncQueue()

    def execute_on_database(self, db_name, operation, data, from_queue=False):
        book_repo = get_book_repository(db_name)
        member_repo = get_member_repository(db_name)
        loan_repo = get_loan_repository(db_name)
        try:
            if operation == "insert_book":
                if isinstance(data, dict):
                    data = build_book_object(data)
                result = book_repo.insert_book(data)
                if not result:
                    raise Exception("insert_book failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "ok"}
            if operation == "insert_member":
                if isinstance(data, dict):
                    data = build_member_object(data)
                result = member_repo.insert_member(data)
                if not result:
                    raise Exception("insert_member failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "ok"}
            if operation == "insert_loan":
                if isinstance(data, dict):
                    data = build_loan_object(data)
                result = loan_repo.insert_loan(data)
                if not result:
                    raise Exception("insert_loan failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "ok"}
            
            elif operation == "delete_book":
                column = data["column"]
                value = data["value"]
                result = book_repo.delete_book(column, value)
                if not result:
                    raise Exception("delete_book failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "deleted"}
            elif operation == "delete_member":
                column = data["column"]
                value = data["value"]
                result = member_repo.delete_member(column, value)
                if not result:
                    raise Exception("delete_member failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "deleted"}
            elif operation == "delete_loan":
                column = data["column"]
                value = data["value"]
                result = loan_repo.delete_loan(column, value)
                if not result:
                    raise Exception("delete_loan failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "deleted"}
            
            elif operation == "update_book":
                column = data["column"]
                value = data["value"]
                updates = data["updates"]
                result = book_repo.update_book(column, value, updates)
                if not result:
                    raise Exception("update_book failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "updated"}
            elif operation == "update_member":
                column = data["column"]
                value = data["value"]
                updates = data["updates"]
                result = member_repo.update_member(column, value, updates)
                if not result:
                    raise Exception("update_member failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "updated"}
            elif operation == "update_loan":
                column = data["column"]
                value = data["value"]
                updates = data["updates"]
                result = loan_repo.update_loan(column, value, updates)
                if not result:
                    raise Exception("update_loan failed")
                return {"db": db_name,
                        "status": "success",
                        "message": "updated"}

        except Exception as e:
            if not operation.startswith("select_") and not from_queue:
                self.queue.add_operation(db_name, operation, serialize_data(data))
            return {
                "db": db_name,
                "status": "failed",
                "message": str(e)
            }
        

    def sync_all(self, operation, data):
        results = []
        for db_name in ["mysql", "postgresql", "sqlserver"]:
            result = self.execute_on_database(db_name, operation, data, from_queue=False)
            results.append(result)

            if result["status"] == "success":
                write_sync_log(f"[SYNC OK] for \"{db_name}\"")
            else:
                write_sync_log(f"[SYNC FAIL] {db_name} -> {result['message']}")
        return results