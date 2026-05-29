from src.services.book_service import BookService
from src.services.member_service import MemberService
from src.services.loan_service import LoanService
from src.services.sync_manager import SyncManager

def get_book_service():
    try:
        return BookService()
    except:
        return None
    
def get_member_service():
    try:
        return MemberService()
    except:
        return None

def get_loan_service():
    try:
        return LoanService()

    except:
        return None