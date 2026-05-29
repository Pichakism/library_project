import sqlite3

class SqliteStorage:

    def __init__(self):
        self.sqLite_db_path = "D:\\code\\Python\\library_project\\data\\sqLite.db"

    def connect(self):
        return sqlite3.connect(self.sqLite_db_path)
    
    def execute_row(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def fetch_one(self, query, params):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        connection.close()
        return row

    def fetch_all(self, query, params):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        connection.close()
        return rows

    def create_tables(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT UNIQUE NOT NULL,
                book_title TEXT NOT NULL,
                author_name TEXT NOT NULL,
                publication_year INTEGER,
                page_count INTEGER,
                genre TEXT,
                book_status TEXT NOT NULL,
                physical_version TEXT NOT NULL,
                digital_version VTEXT NOT NULL,
                count INTEGER)"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT UNIQUE,
                status TEXT,
                join_date DATE)"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                loan_date DATE,
                FOREIGN KEY(member_id)
                    REFERENCES members(id),
                FOREIGN KEY(book_id)
                    REFERENCES books(id))"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS app_metadata (
                key_name VARCHAR(50) PRIMARY KEY,
                value TEXT NOT NULL)"""
        )
        connection.commit()
        connection.close()

    def is_setup_completed(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT value
            FROM app_metadata
            WHERE key_name = 'setup_completed'
        """)
        row = cursor.fetchone()
        connection.close()

        return row is not None and row[0] == "true"
        
    def mark_setup_completed(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO app_metadata (key_name, value)
            VALUES ('setup_completed', 'true')
        """)
        connection.commit()
        connection.close()

    def ensure_metadata_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_metadata (
                key_name TEXT PRIMARY KEY,
                value TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()

# start = SqliteStorage()
# start.mark_setup_completed()