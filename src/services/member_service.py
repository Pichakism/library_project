class MemberService:
    def __init__(self, repo, storage):
        self.repo = repo
        self.storage = storage

    def insert_member(self, book):
        return self.repo.insert_member(book)

    def select_member(self, column, value):
        rows = self.repo.select_member(column, value)
        return [
            {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "phone_number": row[3],
                "status": row[4],
                "join_date": row[5],
            }
            for row in rows
        ]

    def update_member(self, column, value, updates):
        return self.repo.update_member(column, value, updates)

    def delete_member(self, column, value):
        return self.repo.delete_member(column, value)

    # def loan_book(self, book_search, member_search):
    #     return self.repo.loan_book(
    #         book_search[0],
    #         book_search[1],
    #         member_search[0],
    #         member_search[1]
    #     )