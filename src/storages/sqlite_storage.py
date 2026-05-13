import sqlite3


class SqliteStorage:

    def __init__(self):
        self.sqLite_db_path = "../../data/sqLite.db"

    def connect(self):
        return sqlite3.connect(self.sqLite_db_path)
    
    def execute(self, query, params=()):
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

    def creat_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL,
                author_name TEXT NOT NULL,
                publication_year INTEGER,
                page_count INTEGER,
                genre TEXT,
                status TEXT NOT NULL)"""
        )
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                phone_number TEXT UNIQUE,
                status TEXT,
                join_date TEXT)"""
        )
        cursor.execute(
            """CREATE TABLE loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                member_id INTEGER NOT NULL,
                book_id INTEGER NOT NULL,
                loan_date TEXT,
                FOREIGN KEY(member_id)
                    REFERENCES members(id),
                FOREIGN KEY(book_id)
                    REFERENCES books(id))"""
        )

start = SqliteStorage()
start.creat_table()