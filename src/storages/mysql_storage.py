import mysql.connector
from src.config import MySqlConfig

class MySqlStorage:
    def __init__(self):
        self.host = MySqlConfig.DB_HOST
        self.port = MySqlConfig.DB_PORT
        self.user = MySqlConfig.DB_USER
        self.password = MySqlConfig.DB_PASSWORD
        self.database = MySqlConfig.DB_NAME

    def connect(self):
        return mysql.connector.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            database = self.database
        )

    def execute(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        affected = cursor.rowcount
        cursor.close()
        connection.close()
        return affected

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
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_isbn VARCHAR(50) UNIQUE NOT NULL,
                book_title VARCHAR(255) NOT NULL,
                author_name VARCHAR(255) NOT NULL,
                publication_year INT,
                page_count INT,
                genre VARCHAR(100),
                book_status VARCHAR(50) NOT NULL,
                physical_version VARCHAR(10) NOT NULL,
                digital_version VARCHAR(10) NOT NULL,
                count INT
        )
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS members (
                id INT AUTO_INCREMENT PRIMARY KEY,
                member_nID VARCHAR(20) UNIQUE NOT NULL,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(20) UNIQUE,
                status VARCHAR(50),
                join_date DATE
        )
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS loans (
                id INT AUTO_INCREMENT PRIMARY KEY,
                book_isbn VARCHAR(50) NOT NULL,
                member_nID VARCHAR(20) NOT NULL,
                loan_date DATE,
                FOREIGN KEY(member_nID)
                    REFERENCES members(member_nID)
                    ON DELETE CASCADE,
                FOREIGN KEY(book_isbn)
                    REFERENCES books(book_isbn)
                    ON DELETE CASCADE
        )
        """
        )
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS app_metadata (
                key_name VARCHAR(50) PRIMARY KEY,
                value TEXT NOT NULL
        )
        """
        )
        connection.commit()
        connection.close()
    
    def is_setup_completed(self):
        try:
            connection = self.connect()
            cursor = connection.cursor()
            cursor.execute(
            """
                SELECT value
                FROM app_metadata
                WHERE key_name = 'setup_completed'
            """)
            row = cursor.fetchone()
            connection.close()
            return row is not None and row[0] == "true"
        except:
            return False
        
    def mark_setup_completed(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
        """
            INSERT INTO app_metadata (key_name, value)
            VALUES ('setup_completed', 'true')
            ON DUPLICATE KEY UPDATE value = 'true'
        """)
        connection.commit()
        connection.close()

    def ensure_metadata_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS app_metadata (
                key_name VARCHAR(50) PRIMARY KEY,
                value TEXT NOT NULL
            )
        """)

        connection.commit()
        connection.close()


# start = MySqlStorage()
# start.creat_tables()