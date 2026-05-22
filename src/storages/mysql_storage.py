import mysql.connector
from src.config import Config

class MySqlStorage:
    def __init__(self):
        self.host = Config.DB_HOST
        self.port = Config.DB_PORT
        self.user = Config.DB_USER
        self.password = Config.DB_PASSWORD
        self.database = Config.DB_NAME
        self.creat_tables()

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
        cursor.execute(
            query,
            params
        )
        connection.commit()
        connection.close()

    def fetch_one(self, query, params=()):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            query,
            params
        )
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
    
    def creat_tables(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INT AUTO_INCREMENT PRIMARY KEY,
                isbn VARCHAR(50) UNIQUE NOT NULL,
                book_title VARCHAR(255) NOT NULL,
                author_name VARCHAR(255) NOT NULL,
                publication_year INT,
                page_count INT,
                genre VARCHAR(100),
                book_status VARCHAR(50) NOT NULL,
                count INTEGER
            )
            """
        )
        cursor.execute(
             """
            CREATE TABLE IF NOT EXISTS members (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(100) NOT NULL,
                last_name VARCHAR(100) NOT NULL,
                phone_number VARCHAR(20) UNIQUE,
                status VARCHAR(50),
                join_date VARCHAR(20)
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS loans (
                id INT AUTO_INCREMENT PRIMARY KEY,
                member_id INT NOT NULL,
                book_id INT NOT NULL,
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
                key_name VARCHAR(50) PRIMARY KEY,
                value TEXT NOT NULL
            )
            """
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
            INSERT INTO app_metadata (key_name, value)
            VALUES ('setup_completed', 'true')
            ON DUPLICATE KEY UPDATE value = 'true'
        """)
        connection.commit()
        connection.close()


start = MySqlStorage()
start.creat_tables()