import psycopg2
from src.config import PostgreSqlConfig

class PostgreSqlStorage:
    def __init__(self):
        self.host = PostgreSqlConfig.DB_HOST
        self.port = PostgreSqlConfig.DB_PORT
        self.user = PostgreSqlConfig.DB_USER
        self.password = PostgreSqlConfig.DB_PASSWORD
        self.database = PostgreSqlConfig.DB_NAME

    def connect(self):
        return psycopg2.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            dbname = self.database
        )
    
    def execute(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()

    def fetch_one(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        connection.close()
        return row
    
    def fetch_all(self, query, params=()):
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
        """
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                isbn TEXT UNIQUE NOT NULL,
                book_title TEXT NOT NULL,
                author_name TEXT NOT NULL,
                publication_year INTEGER,
                page_count INTEGER,
                genre TEXT,
                book_status TEXT NOT NULL,
                physical_version TEXT NOT NULL,
                digital_version TEXT NOT NULL,
                count INTEGER
        )
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS members (
                id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT UNIQUE,
                status TEXT,
                date DATE
        )
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS loans (
                id SERIAL PRIMARY KEY,
                member_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                loan_date DATE,
                FOREIGN KEY(member_id)
                    REFERENCES members(id)
                    ON DELETE CASCADE,
                FOREIGN KEY(book_id)
                    REFERENCES books(id)
                    ON DELETE CASCADE
        )        
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS app_metadata (
                key_name TEXT PRIMARY KEY,
                value TEXT NOT NULL
        )
        """
        )
        connection.commit()
        connection.close()

    def is_setup_completed(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
        """
            SELECT value
            FROM app_metadata
            WHERE key_name = 'setup_completed'
        """)
        row = cursor.fetchone()
        return row is not None and row[0] == "true"
        
    def mark_setup_completed(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
        """
            INSERT INTO app_metadata (key_name, value)
            VALUES ('setup_completed', 'true')
            ON CONFLICT (key_name) DO UPDATE SET value = 'true'
        """)
        connection.commit()
        connection.close()