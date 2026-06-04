import os
from dotenv import load_dotenv

load_dotenv()

class MySqlConfig:
    DB_HOST = os.getenv("MYSQL_DB_HOST")
    DB_PORT = int(os.getenv("MYSQL_DB_PORT"))
    DB_USER = os.getenv("MYSQL_DB_USER")
    DB_PASSWORD = os.getenv("MYSQL_DB_PASSWORD")
    DB_NAME = os.getenv("MYSQL_DB_NAME")

class PostgreSqlConfig:
    DB_HOST = os.getenv("POSTGRES_DB_HOST")
    DB_PORT = int(os.getenv("POSTGRES_DB_PORT"))
    DB_USER = os.getenv("POSTGRES_DB_USER")
    DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD")
    DB_NAME = os.getenv("POSTGRES_DB_NAME")

class SqlServerConfig:
    DB_HOST = os.getenv("SqlSERVER_DB_HOST")
    DB_PORT = os.getenv("SqlSERVER_DB_PORT")
    DB_USER = os.getenv("SqlSERVER_DB_USER")
    DB_PASSWORD = os.getenv("SqlSERVER_DB_PASSWORD")
    DB_NAME = os.getenv("SqlSERVER_DB_NAME")
    DB_DRIVER = os.getenv("SqlSERVER_DB_DRIVER")

class OracleConfig:
    DB_HOST = os.getenv("ORACLE_DB_HOST")
    DB_PORT = os.getenv("ORACLE_DB_PORT")
    DB_USER = os.getenv("ORACLE_DB_USER")
    DB_PASSWORD = os.getenv("ORACLE_DB_PASSWORD")
    DB_SERVICE = os.getenv("ORACLE_DB_SERVICE") 