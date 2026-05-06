from models.book_status import Book_Status
class Member:
    def __init__(self, id, first_name, last_name, phone_number, member_status, date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.member_status = member_status
        self.date = date