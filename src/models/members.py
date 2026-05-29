# Represents a Member entity in the system
# - Stores personal and membership-related information
# - Used for creating member objects before saving
class Member:
    def __init__(self, member_nID, first_name, last_name, phone_number, status, join_date):
        self.member_nID = member_nID
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.status = status
        self.join_date = join_date
    
    # Returns a formatted string representation of a Member object
    # - Used for displaying member information
    def __str__(self):
        return(
            f"member_nID = {self.member_nID}\n"
            f"First name = {self.first_name}\n"
            f"Last name = {self.last_name}\n"
            f"Phone number = {self.phone_number}\n"
            f"Status = {self.member_status}\n"
            f"Date of join = {self.join_date}"
        )