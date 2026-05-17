import mysql.connector

class Bootstrap:
    def __init__(self, mysql_storage):

        self.mysql = mysql_storage
        # self.sqlite = sqlite_storage
        self.storage = None


    def get_storage(self):
        try:
            self.mysql.connect()
            self.storage = self.mysql
            print("[OK] MySQL selected.")
        except Exception as e:
            print("[WARN] MySQL failed, using SQLite")
            # self.storage = self.sqlite
            self.storage = None


    def first_setup(self):
        if self.storage.is_setup_completed():
            print("[OK] Setup already completed.")
            return

        print("[INFO] Running first setup...")
        self.storage.creat_tables()
        self.storage.mark_setup_completed()
        print("[OK] Setup completed.")


    def run(self):
        self.get_storage()

        if self.storage is None:
            raise Exception("No storage available")

        self.first_setup()
        return self.storage