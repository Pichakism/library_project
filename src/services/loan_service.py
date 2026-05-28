class LoanService:
    def __init__(self, repo, storage):
        self.repo = repo
        self.storage = storage

    # INSERT
    def insert_loan(self, loan):
        return self.repo.insert_loan(loan)

    # SELECT
    def select_loan(self, column, value):
        rows = self.repo.select_loan(column, value)
        return [
            {
                "id": row[0],
                "book_id": row[1],
                "member_id": row[2],
                "loan_date": row[3],
            }
            for row in rows
        ]

    # DELETE
    def delete_loan(self, column, value):
        return self.repo.delete_loan(column, value)

    # UPDATE (فعلاً اگر نداری)
    def update_loan(self, column, value, updates):
        return self.repo.update_loan(column, value, updates)