class Loan:
    def __init__(self, book_isbn, member_id, date):
        # self.id = id
        self.book_isbn = book_isbn
        self.member_id = member_id
        self.date = date

    def __str__(self):
        return(
            # f"ID = {self.id}\n"
            f"Book ISBN = {self.isbn}\n"
            f"Member ID = {self.book_title}\n"
            f"Date of loan = {self.auther_name}\n"
        )