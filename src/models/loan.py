class Loan:
    def __init__(self, book_isbn, member_nID, loan_date):
        # self.id = id
        self.book_isbn = book_isbn
        self.member_nID = member_nID
        self.loan_date = loan_date

    def __str__(self):
        return(
            # f"ID = {self.id}\n"
            f"Book ISBN = {self.book_isbn}\n"
            f"Member ID = {self.member_nID}\n"
            f"Date of loan = {self.loan_date}\n"
        )