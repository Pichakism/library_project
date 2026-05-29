def get_book_repository(db_name: str):
    if db_name == "mysql":
        from src.repositories.mysql_repository import BookRepository
        return BookRepository()

    if db_name == "postgresql":
        from src.repositories.postgreSql_repository import BookRepository
        return BookRepository()

    if db_name == "sqlite":
        from src.repositories.sqlite_repository import BookRepository
        return BookRepository()

    if db_name == "sqlserver":
        from src.repositories.sqlServer_repository import BookRepository
        return BookRepository()

    return None

def get_member_repository(db_name: str):
    if db_name == "mysql":
        from src.repositories.mysql_repository import MemberRepository
        return MemberRepository()

    if db_name == "postgresql":
        from src.repositories.postgreSql_repository import MemberRepository
        return MemberRepository()

    if db_name == "sqlite":
        from src.repositories.sqlite_repository import MemberRepository
        return MemberRepository()

    if db_name == "sqlserver":
        from src.repositories.sqlServer_repository import MemberRepository
        return MemberRepository()

    return None

def get_loan_repository(db_name: str):
    if db_name == "mysql":
        from src.repositories.mysql_repository import LoanRepository
        return LoanRepository()

    if db_name == "postgresql":
        from src.repositories.postgreSql_repository import LoanRepository
        return LoanRepository()

    if db_name == "sqlite":
        from src.repositories.sqlite_repository import LoanRepository
        return LoanRepository()

    if db_name == "sqlserver":
        from src.repositories.sqlServer_repository import LoanRepository
        return LoanRepository()

    return None