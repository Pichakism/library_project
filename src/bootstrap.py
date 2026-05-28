import mysql.connector

class Bootstrap:
    def __init__(self, mysql_storage, psql_storage, sqlite_storage, sqlServer_storage):

        self.mysql = mysql_storage
        self.psql = psql_storage
        self.sqlite = sqlite_storage
        self.sqlServer = sqlServer_storage
        self.mysql_storage = None
        self.psql_storage = None
        self.sqlite_storage = None
        self.sqlServer_storage = None


    def get_storage(self):
        try:
            self.mysql.connect()
            self.mysql_storage = self.mysql
            print("[OK] MySQL Load...")
        except Exception as e:
            print("[WARN] MySQL Load failed!!!")
            self.mysql_storage = None
        try:
            self.psql.connect()
            self.psql_storage = self.psql
            print("[OK] PostgreSQL Load...")
        except Exception as e:
            print("[WARN] PostgreSQL Load failed!!!")
            self.psql_storage = None
        try:
            self.sqlite.connect()
            self.sqlite_storage = self.sqlite
            print("[OK] SqLite Load...")
        except Exception as e:
            print("[WARN] SqLite Load failed!!!")
            self.sqlite_storage = None
        try:
            self.sqlServer.connect()
            self.sqlServer_storage = self.sqlServer
            print("[OK] SQL Server Load...")
        except Exception as e:
            print("[WARN] SQl Server Load failed!!!")
            self.sqlServer_storage = None


    def first_mySql_setup(self):
        self.mysql.ensure_metadata_table()
        try:
            if self.mysql.is_setup_completed():
                print("[OK] MySQL Setup already completed.")
                return
            print("[INFO] Running first setup...")
            self.mysql.create_tables()
            self.mysql.mark_setup_completed()
            print("[OK] *MySQL* Setup completed.")
        except Exception as e:
            print("\nERROR: ", e)

    def first_pSql_setup(self):
        self.psql.ensure_metadata_table()
        try:
            if self.psql.is_setup_completed():
                print("[OK] PostgreSQL Setup already completed.")
                return
            print("[INFO] Running first setup...")
            self.psql.create_tables()
            self.psql.mark_setup_completed()
            print("[OK] *PostgreSQL* Setup completed.")
        except Exception as e:
            print("\nERROR: ", e)

    def first_sqLite_setup(self):
        self.sqlite.ensure_metadata_table()
        try:
            if self.sqlite.is_setup_completed():
                print("[OK] SqLite Setup already completed.")
                return
            print("[INFO] Running first setup...")
            self.sqlite.create_tables()
            self.sqlite.mark_setup_completed()
            print("[OK] *SqLite* Setup completed.")
        except Exception as e:
            print("\nERROR: ", e)

    def first_sqlServer_setup(self):
        self.sqlServer.ensure_metadata_table()
        try:
            if self.sqlServer.is_setup_completed():
                print("[OK] SQl Server Setup already completed.")
                return
            print("[INFO] Running first setup...")
            self.sqlServer.create_tables()
            self.sqlServer.mark_setup_completed()
            print("[OK] *SQl Server* Setup completed.")
        except Exception as e:
            print("\nERROR: ", e)


    def run(self):
        self.get_storage()

        if self.mysql_storage is None:
            print("mySQL storage NOT available")
        else:
            self.first_mySql_setup()

        if self.psql_storage is None:
            print("postgreSQL storage NOT available")
        else:
            self.first_pSql_setup()

        if self.sqlite_storage is None:
            print("SqLite storage NOT available")
        else:
            self.first_sqLite_setup()

        if self.sqlServer_storage is None:
            print("SQl Server storage NOT available")
        else:
            self.first_sqlServer_setup()

        return