class Member:
    def __init__(self, id, first_name, last_name, phone_number, member_status, date):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.member_status = member_status
        self.date = date
    
    def __str__(self):
        return(
            f"ID = {self.id}\n"
            f"First name = {self.first_name}\n"
            f"Last name = {self.last_name}\n"
            f"Phone number = {self.phone_number}\n"
            f"Status = {self.member_status}\n"
            f"Date of join = {self.date}"
        )