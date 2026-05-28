class Loan:
    def __init__(self, book_id, member_id, loan_date):
        # self.id = id
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date

    def __str__(self):
        return(
            # f"ID = {self.id}\n"
            f"Book ISBN = {self.book_id}\n"
            f"Member ID = {self.member_id}\n"
            f"Date of loan = {self.loan_date}\n"
        )