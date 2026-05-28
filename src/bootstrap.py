from src.storages.sqlite_storage import SqliteStorage
from src.storages.mysql_storage import MySqlStorage
from src.storages.postgreSql_storage import PostgreSqlStorage
from src.storages.sqlServer_storage import SqlServerStorage
from src.storages.sqlite_storage import SqliteStorage
class Bootstrap:
    def __init__(self):
        # -------------------------
        # REGISTER ALL DATABASES
        # -------------------------
        # Central place for all database implementations
        self.storages = {
            "MySQL": MySqlStorage(),
            "PostgreSQL": PostgreSqlStorage(),
            "SQLite": SqliteStorage(),
            # "SQLServer": SqlServerStorage()
        }

        # active databases that successfully connected
        self.active_storages = {}

    # -------------------------
    # CONNECT DATABASES
    # -------------------------
    # Try to connect all registered databases
    # Only working ones will be activated
    def get_storage(self):
        for name, storage in self.storages.items():
            try:
                storage.connect()
                self.active_storages[name] = storage
                print(f"[OK] {name} Load...")
            except Exception as e:
                print(f"[WARN] {name} Load failed!!!")

    # -------------------------
    # GENERIC FIRST-TIME SETUP
    # -------------------------
    # Runs initial setup only once per database
    def first_setup(self, name, storage):
        try:
            storage.ensure_metadata_table()

            if storage.is_setup_completed():
                print(f"[OK] {name} Setup already completed.")
                return

            print(f"[INFO] Running first setup... {name}")
            storage.create_tables()
            storage.mark_setup_completed()

            print(f"[OK] *{name}* Setup completed.")

        except Exception as e:
            print(f"[ERROR] {name} setup failed:", e)

    # -------------------------
    # RUN BOOTSTRAP PROCESS
    # -------------------------
    def run(self):
        # Step 1: connect all databases
        self.get_storage()

        # Step 2: setup only active databases
        for name, storage in self.active_storages.items():
            self.first_setup(name, storage)

        # Step 3: report inactive ones
        for name in self.storages:
            if name not in self.active_storages:
                print(f"[INFO] {name} storage NOT available")