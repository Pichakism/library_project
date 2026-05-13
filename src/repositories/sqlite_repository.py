from storages.sqlite_storage import SqliteStorage

class BookRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # NOTE: book func...:
    def search_book(self):
        ...

    def save_book(self):
        ...

    def update_book(self):
        ...

    def delete_book(self):
        ...

class MemberRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # NOTE: member func...:
    def search_member(self):
        ...

    def save_member(self):
        ...

    def update_member(self):
        ...

    def delete_member(self):
        ...

class LoanRepository:
    def __init__(self, sqlite_storage):
        self.storage = sqlite_storage

    # NOTE: loan func...:
    def search_loan(self):
        ...

    def save_loan(self):
        ...
    
    def update_loan(self):
        ...

    def delete_loan(self):
        ...