class SyncDBForBook:
    def __init__(self, sync_manager):
        self.sync = sync_manager

    def sync_insert(self, book):
        self.sync.sync_all(
            operation="insert_book",
            data=book
        )

    def sync_select(self, column, value):
        pass

    def sync_update(self, column, value, updates):
        self.sync.sync_all(
            operation="update_book",
            data={
                "column": column,
                "value": value,
                "updates": updates
            }
        )

    def sync_delete(self, column, value):
        self.sync.sync_all(
            operation="delete_book",
            data={
                "column": column,
                "value": value
            }
        )

class SyncDBForMember:
    def __init__(self, sync_manager):
        self.sync = sync_manager

    def sync_insert(self, book):
        self.sync.sync_all(
            operation="insert_member",
            data=book
        )

    def sync_select(self, column, value):
        pass

    def sync_update(self, column, value, updates):
        self.sync.sync_all(
            operation="update_member",
            data={
                "column": column,
                "value": value,
                "updates": updates
            }
        )

    def sync_delete(self, column, value):
        self.sync.sync_all(
            operation="delete_member",
            data={
                "column": column,
                "value": value
            }
        )

