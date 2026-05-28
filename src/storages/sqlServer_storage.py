import pyodbc
from src.config import SqlServerConfig


class SqlServerStorage:
    def __init__(self):
        self.server = SqlServerConfig.DB_HOST
        self.port = SqlServerConfig.DB_PORT
        self.user = SqlServerConfig.DB_USER
        self.password = SqlServerConfig.DB_PASSWORD
        self.database = SqlServerConfig.DB_NAME
        self.driver = SqlServerConfig.DB_DRIVER

    def connect(self):
        return pyodbc.connect(
            f"DRIVER={{{self.driver}}};"
            f"SERVER={self.server},{self.port};"
            f"DATABASE={self.database};"
            f"UID={self.user};"
            f"PWD={self.password};"
            "TrustServerCertificate=yes;"
        )

    def execute(self, query, params=()):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
            connection.commit()

    def fetch_one(self, query, params=()):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def fetch_all(self, query, params=()):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()

    def create_tables(self):
        with self.connect() as connection:
            with connection.cursor() as cursor:

                cursor.execute("""
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='books' AND xtype='U')
                CREATE TABLE books (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    isbn NVARCHAR(50) UNIQUE NOT NULL,
                    book_title NVARCHAR(255) NOT NULL,
                    author_name NVARCHAR(255) NOT NULL,
                    publication_year INT,
                    page_count INT,
                    genre NVARCHAR(100),
                    book_status NVARCHAR(50) NOT NULL,
                    physical_version NVARCHAR(10) NOT NULL,
                    digital_version NVARCHAR(10) NOT NULL,
                    count INT
                )
                """)

                cursor.execute("""
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='members' AND xtype='U')
                CREATE TABLE members (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    first_name NVARCHAR(100) NOT NULL,
                    last_name NVARCHAR(100) NOT NULL,
                    phone_number NVARCHAR(20) UNIQUE,
                    status NVARCHAR(50),
                    join_date NVARCHAR(20)
                )
                """)

                cursor.execute("""
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='loans' AND xtype='U')
                CREATE TABLE loans (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    member_id INT NOT NULL,
                    book_id INT NOT NULL,
                    loan_date DATE,
                    FOREIGN KEY(member_id) REFERENCES members(id) ON DELETE CASCADE,
                    FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE
                )
                """)

                cursor.execute("""
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='app_metadata' AND xtype='U')
                CREATE TABLE app_metadata (
                    key_name NVARCHAR(50) PRIMARY KEY,
                    value NVARCHAR(MAX) NOT NULL
                )
                """)

            connection.commit()

    def is_setup_completed(self):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT value
                    FROM app_metadata
                    WHERE key_name = 'setup_completed'
                """)
                row = cursor.fetchone()
                return row is not None and row[0] == "true"

    def mark_setup_completed(self):
        with self.connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO app_metadata (key_name, value)
                    VALUES ('setup_completed', 'true')
                """)
            connection.commit()


# start = SqlServerStorage()
# start.creat_tables()