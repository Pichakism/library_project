from src.services.book_service import BookService
from src.services.member_service import MemberService
from src.repositories import (
    sqlite_repository,
    mysql_repository,
    postgreSql_repository,
    sqlServer_repository,
    csv_repository
)
from src.storages.sqlite_storage import SqliteStorage
from src.storages.mysql_storage import MySqlStorage
from src.storages.postgreSql_storage import PostgreSqlStorage
from src.storages.sqlServer_storage import SqlServerStorage

# -------------------------
# BOOK SERVICE FACTORY
# -------------------------
# Returns proper service based on selected database
# - CSV returns repository directly
# - Other databases return BookService with injected repo + storage
def get_book_service(db_type: str):
    if db_type == "1":
        return "csv", csv_repository.BookRepository()

    if db_type == "2":
        return BookService(sqlite_repository.BookRepository(), SqliteStorage())

    if db_type == "3":
        return BookService(mysql_repository.BookRepository(), MySqlStorage())

    if db_type == "4":
        return BookService(postgreSql_repository.BookRepository(), PostgreSqlStorage())

    if db_type == "5":
        return BookService(sqlServer_repository.BookRepository(), SqlServerStorage())

    return None

# -------------------------
# MEMBER SERVICE FACTORY
# -------------------------
# Returns proper service based on selected database
# - CSV returns repository directly
# - Other databases return MemberService with injected repo + storage
def get_member_service(db_type: str):
    if db_type == "1":
        return "csv", csv_repository.MemberRepository()

    if db_type == "2":
        return MemberService(sqlite_repository.MemberRepository(), SqliteStorage())

    if db_type == "3":
        return MemberService(mysql_repository.MemberRepository(), MySqlStorage())

    if db_type == "4":
        return MemberService(postgreSql_repository.MemberRepository(), PostgreSqlStorage())

    if db_type == "5":
        return MemberService(sqlServer_repository.MemberRepository(), SqlServerStorage())

    return None